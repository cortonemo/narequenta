# Ficheiro: Tools/run_sheet.py (Substitui run_sheet_gui.py)

import os
import sys
import webview

# Importar os nossos módulos. Assumindo que estão na mesma pasta 'Tools'
from . import config
from . import server
from . import api_bridge

# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def main():
    # 1. Caminhos
    # O script está em Tools/run_sheet.py.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Subir um diretório para chegar ao ROOT do repositório (G:\Git\narequenta)
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    # 2. Iniciar HTTP server
    # O servidor serve o 'root_dir' na 'config.PORT'
    http_server_instance = server.start_server(root_dir, config.PORT)
    if not http_server_instance:
        print("Falha ao iniciar o servidor HTTP. Encerrando.")
        sys.exit(1)

    # 3. Construir URL inicial: http://localhost:PORT/html/index.html
    first_url = f"http://localhost:{config.PORT}/{config.LANDING_PAGE_PATH}"
    base_url = f"http://localhost:{config.PORT}"

    # 4. Criar janela
    window = webview.create_window(
        title="Nárëquenta - Início da Ficha",
        url=first_url, # Carrega a Landing Page
        width=1000,
        height=700,
        resizable=True,
    )

    # 5. Expor funções (API Bridge)
    # Expor a função de obter idiomas (usada dentro das fichas finais)
    window.expose(api_bridge.make_get_languages())
    
    # Expor a função de trocar de idioma (usada dentro das fichas finais)
    # NOTA: O JS dentro da ficha final terá de saber o seu próprio tipo/classe para chamar esta função.
    window.expose(api_bridge.make_switch_language(window, base_url))
    
    # Expor a NOVA função de carregamento da ficha inicial (usada no index.html)
    window.expose(api_bridge.make_load_sheet(window, base_url))

    # 6. Lançar o loop da GUI (bloqueia até fechar)
    webview.start()

    # 7. Encerrar
    server.stop_server(http_server_instance)
    sys.exit(0)


if __name__ == "__main__":
    # É fundamental que este script seja executado como um pacote:
    # python -m Tools.run_sheet
    # Isto garante que as imports relativas funcionem corretamente.
    main()
