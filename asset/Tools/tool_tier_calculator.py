import webview
import http.server
import socketserver
import threading
import os
import sys

# Porta do servidor que será usada para servir os assets
SERVER_PORT = 8001
# Idioma padrão
DEFAULT_LANG = 'pt-pt' 

# ============================================================
# LÓGICA DO SERVIDOR PYWEBVIEW
# ============================================================

def start_server(root_dir, port):
    """Inicia um servidor HTTP simples na pasta raiz para servir assets."""
    # Muda o diretório de trabalho para a raiz do projeto antes de iniciar o servidor
    os.chdir(root_dir) 
    
    Handler = http.server.SimpleHTTPRequestHandler
    try:
        httpd = socketserver.TCPServer(("", port), Handler)
    except OSError as e:
        print(f"Erro ao iniciar o servidor na porta {port}: {e}")
        new_port = port + 1
        print(f"Tentando a porta {new_port}...")
        try:
            httpd = socketserver.TCPServer(("", new_port), Handler)
            global SERVER_PORT
            SERVER_PORT = new_port
        except Exception as e2:
            print(f"Erro ao tentar porta alternativa: {e2}")
            sys.exit(1)


    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True 
    thread.start()
    return httpd

# ============================================================
# DADOS DE REGRA (v0.7)
# ============================================================
TIER_MAP = {
    0: {'tier': '0', 'dice': 'None', 'avg': 0.0},
    10: {'tier': 'I', 'dice': '1d10', 'avg': 5.5},
    20: {'tier': 'II', 'dice': '2d10', 'avg': 11.0},
    30: {'tier': 'III', 'dice': '3d10', 'avg': 16.5},
    40: {'tier': 'IV', 'dice': '4d10', 'avg': 22.0},
    50: {'tier': 'V', 'dice': '5d10', 'avg': 27.5}
}

# ============================================================
# API EXPONDO A LÓGICA DE CÁLCULO AO JAVASCRIPT
# ============================================================
class TierCalculatorAPI:
    def calculate_tier(self, e_max_percent):
        """
        Calcula o Tier de Proficiência com base no E_max. Chamado por JS.
        """
        # 1. Aplicar o Limite Fixo (Hard Floor)
        if e_max_percent < 50:
            e_max_percent = 50.0

        # 2. Calcular a Perda (Attritio)
        loss = 100 - e_max_percent
        
        # 3. Mapear o Tier
        tier_data = TIER_MAP[0] 
        for min_loss in sorted(TIER_MAP.keys(), reverse=True):
            if loss >= min_loss:
                tier_data = TIER_MAP[min_loss]
                break
                
        # Retorna um dicionário que o JS pode processar
        return {
            "E_max (%)": f"{e_max_percent:.1f}%",
            "Perda Total (%)": f"{loss:.1f}%",
            "TIER": tier_data['tier'],
            "D_PROF Pool": tier_data['dice'],
            "M_AVG_Value": f"{tier_data['avg']:.1f}"
        }

# ============================================================
# PRINCIPAL
# ============================================================
def main():
    # O script está agora em 'assets/tools/'. Precisamos subir dois níveis para a raiz.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir)) 

    # 1. Inicia o Servidor na Raiz (root_dir)
    httpd = start_server(root_dir, SERVER_PORT)

    # 2. Constrói o URL do HTML (o caminho é relativo à raiz do servidor)
    # O HTML está em 'assets/html/tools/tier_calculator_gui.html'
    html_asset_path = 'assets/html/tools/tier_calculator_gui.html'
    base_url = f"http://localhost:{SERVER_PORT}"
    
    # Passamos o idioma inicial como um parâmetro de URL
    first_url = f"{base_url}/{html_asset_path}?lang={DEFAULT_LANG}"

    # 3. Cria a janela
    api = TierCalculatorAPI()

    window = webview.create_window(
        title="Nárëquenta Tier Calculator",
        url=first_url,
        js_api=api,
        width=450,
        height=600,
        resizable=False
    )
    
    # 4. Inicia o pywebview
    webview.start()

    # 5. Para o servidor
    httpd.shutdown()

if __name__ == "__main__":
    main()