import webview
import http.server
import socketserver
import threading
import os
import sys
import json
import tkinter as tk
from tkinter import messagebox

# ============================================================
# CONFIGURAÇÃO DE CAMINHOS E MAPAS
# ============================================================

CONFIG_FILE = 'config.json'

# Mapeamento do nome da folha para o nome do arquivo HTML agnóstico ao idioma
SHEET_MAP_AGNOSTIC = {
    "PC": "assets/html/sheets/pc_sheet.html",
    "NPC": "assets/html/sheets/npc_sheet.html",
    "GM_REF": "assets/html/sheets/gm_reference.html"
}

# Variável para armazenar a configuração carregada
global_config = {}
# Variável global para armazenar a escolha da sheet feita na GUI
sheet_choice = None

# ============================================================
# LÓGICA DO SERVIDOR E CONFIG
# ============================================================
def load_config():
    """Carrega as configurações de porta e idioma do config.json."""
    global global_config
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, CONFIG_FILE)
        
        with open(config_path, 'r') as f:
            global_config = json.load(f)
        
        if 'SERVER_PORT' not in global_config: global_config['SERVER_PORT'] = 8000
        if 'DEFAULT_LANG' not in global_config: global_config['DEFAULT_LANG'] = 'en-us'
        if 'AVAILABLE_LANGS' not in global_config: global_config['AVAILABLE_LANGS'] = ['en-us', 'pt-pt']
        
        return global_config
    except Exception as e:
        print(f"FATAL: Não foi possível carregar ou analisar {CONFIG_FILE}. Erro: {e}", file=sys.stderr)
        sys.exit(1)
        
def start_server(root_dir, port):
    """Inicia um servidor HTTP simples na pasta raiz e retorna o HTTPD e a porta real."""
    os.chdir(root_dir) 
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        httpd = socketserver.TCPServer(("", port), Handler)
        actual_port = port
    except OSError as e:
        # Tenta uma porta alternativa se a original estiver em uso
        print(f"Erro ao iniciar o servidor na porta {port}: {e}")
        actual_port = port + 1
        print(f"Tentando a porta {actual_port}...")
        try:
            httpd = socketserver.TCPServer(("", actual_port), Handler)
        except Exception as e2:
            print(f"Erro ao tentar porta alternativa: {e2}")
            sys.exit(1)

    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    
    return httpd, actual_port

# ============================================================
# FUNÇÃO DE UTILIDADE DE IDIOMA (CORRIGIDA)
# ============================================================

def load_title_from_json(root_dir, lang_code, sheet_key):
    """
    Carrega o JSON para encontrar o título da janela, corrigindo o código de idioma
    e ajustando o caminho para o ficheiro 'assets/lang/'.
    """
    # 1. Normalização do Código de Idioma (ex: 'en' -> 'en-us')
    if lang_code == 'en':
        file_code = 'en-us'
    elif lang_code == 'pt':
        file_code = 'pt-pt'
    else:
        file_code = lang_code 

    file_name = f"{file_code}.json"

    # 2. Construção do Caminho (CORRIGIDO)
    # root_dir agora aponta para G:\Git\narequenta\.
    # O caminho deve ser construído a partir daí.
    lang_path = os.path.join(root_dir, 'assets', 'lang', file_name)
    lang_path = os.path.join(root_dir, 'lang', file_name)
    try:
        with open(lang_path, 'r', encoding='utf-8') as f:
            lang_data = json.load(f)
            
        title_key = f"{sheet_key}_SHEET_TITLE"
        return lang_data.get(title_key, f"Ficha de {sheet_key}")
        
    except FileNotFoundError:
        print(f"Aviso: Ficheiro de idioma não encontrado. Caminho tentado: {lang_path}", file=sys.stderr)
        return f"Ficha de {sheet_key}"
    
    except Exception as e:
        print(f"Aviso: Falha geral ao carregar título JSON: {e}", file=sys.stderr)
        return f"Ficha de {sheet_key}"
        
# ------------------------------------------------------------
# FUNÇÃO DE SELEÇÃO GRÁFICA (Tkiner)
# ------------------------------------------------------------

def select_sheet():
    """Abre uma janela Tkinter para selecionar o tipo de sheet."""
    global sheet_choice 

    def set_choice(key):
        global sheet_choice
        sheet_choice = key
        root.destroy()

    root = tk.Tk()
    root.title("Nárëquenta: Seleção de Ficha")
    root.geometry("300x200")
    root.resizable(False, False)
    
    tk.Label(root, text="Escolha a Ficha para Iniciar:", font=('Arial', 12, 'bold')).pack(pady=10)
    
    tk.Button(root, text="1. Ficha de PC", command=lambda: set_choice('PC'), width=20, bg='#d4edda').pack(pady=5)
    tk.Button(root, text="2. Referência NPC", command=lambda: set_choice('NPC'), width=20, bg='#f8d7da').pack(pady=5)
    tk.Button(root, text="3. Referência GM", command=lambda: set_choice('GM_REF'), width=20, bg='#ffeeba').pack(pady=5)
    
    root.mainloop()
    
    return sheet_choice if sheet_choice else 'PC'
    
# ============================================================
# API PYTHON PARA JAVASCRIPT
# ============================================================
class Api:
    """Expõe funções ao JavaScript para controlo da aplicação."""
    def __init__(self, window, config, sheet_map):
        self.window = window
        self.config = config
        self.sheet_map = sheet_map
        self.base_url = f"http://localhost:{config['SERVER_PORT']}"

    def get_languages(self):
        """Chamado pelo JS para obter as línguas disponíveis e a padrão."""
        return {
            'available_langs': self.config['AVAILABLE_LANGS'],
            'default_lang': self.config['DEFAULT_LANG']
        }

    def switch_sheet(self, lang_code, sheet_key):
        """
        Chamado pelo JS para carregar uma nova folha HTML internamente.
        """
        if sheet_key not in self.sheet_map:
            print(f"Erro: Chave de folha desconhecida: {sheet_key}")
            return False

        sheet_path = self.sheet_map[sheet_key]
        new_url = f"http://localhost:{self.config['SERVER_PORT']}/{sheet_path}?lang={lang_code}"
        
        self.window.load_url(new_url)
        return True


# ============================================================
# PRINCIPAL
# ============================================================

def main():
    # 1. Carregar Configuração
    config = load_config()    
    
    # 2. Seleção de Ficha pelo Utilizador (GUI Tkinter)
    sheet_key = select_sheet()
    
    # 3. Caminhos e Servidor
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    # SUBSTITUA PELA LÓGICA DE SUBIR DOIS NÍVEIS:
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    
    # 4. Inicia o Servidor e recebe a porta real utilizada
    httpd, actual_port = start_server(root_dir, config['SERVER_PORT'])
    config['SERVER_PORT'] = actual_port
    
    # 5. NOVO: Carregar Título da Janela do JSON
    window_title_suffix = load_title_from_json(
        root_dir, 
        config['DEFAULT_LANG'], 
        sheet_key
    )
    full_window_title = f"Nárëquenta: {window_title_suffix}"
    
    # 6. Constrói o URL
    initial_sheet_path = SHEET_MAP_AGNOSTIC[sheet_key] # Usa a chave escolhida
    base_url = f"http://localhost:{config['SERVER_PORT']}"
    
    first_url = f"{base_url}/{initial_sheet_path}?lang={config['DEFAULT_LANG']}"

    # 7. Cria a API e a janela
    api = Api(window=None, config=config, sheet_map=SHEET_MAP_AGNOSTIC)

    window = webview.create_window(
        title=full_window_title, # CORREÇÃO: Usa o título completo do JSON
        url=first_url,
        width=1000,
        height=1100,
        resizable=True,
        js_api=api # Expõe a API para a navegação interna
    )
    
    # Atribui a referência da janela ao objeto API para que a API possa controlá-la
    api.window = window

    # 8. Inicia o pywebview
    webview.start()

    # 9. Encerramento limpo
    httpd.shutdown()
    sys.exit(0)


if __name__ == "__main__":
    main()