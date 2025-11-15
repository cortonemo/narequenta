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

# Variável de controle de debug
DEBUG_MODE = True # Defina como False para desativar as mensagens de debug

# Mapeamento do nome da folha para o nome do arquivo HTML agnóstico ao idioma
SHEET_MAP_AGNOSTIC = {
    "PC": "assets/html/sheets/pc_sheet.html",
    "NPC": "assetshtml/sheets/npc_sheet.html",
    "GM_REF": "assetshtml/sheets/gm_reference.html"
}

# Variável para armazenar a configuração carregada
global_config = {}

# ============================================================
# FUNÇÃO DE DEBUG (NOVO)
# ============================================================

def debug_path(var_name, path):
    """Imprime o nome da variável e o caminho físico resultante se DEBUG_MODE for True."""
    if DEBUG_MODE:
        print(f"[DEBUG PATH] {var_name}: {path}", file=sys.stderr)

# ============================================================
# LÓGICA DO SERVIDOR E CONFIG
# ============================================================
def load_config():
    # ... (código load_config inalterado) ...
    # Assumimos que as dependências do config.json foram corrigidas para 'en-us'
    global global_config
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, CONFIG_FILE)
        
        # DEBUG: Mostrar onde o config.json é procurado
        debug_path("config_path", config_path) 
        
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
    
    # DEBUG: Mostrar onde o servidor está a iniciar a sua raiz
    debug_path("Server root_dir", root_dir) 
    
    os.chdir(root_dir) 
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        httpd = socketserver.TCPServer(("", port), Handler)
        actual_port = port
    except OSError as e:
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
# FUNÇÕES DE UTILIDADE DE IDIOMA (Para carregar o título)
# ============================================================

def load_title_from_json(root_dir, lang_code, sheet_key):
    """Carrega o JSON para encontrar o título de uma sheet específica."""
    
    # 1. Normalização do Código de Idioma (essencial para evitar 'en.json' vs 'en-us.json')
    if lang_code == 'en':
        file_code = 'en-us'
    elif lang_code == 'pt':
        file_code = 'pt-pt'
    else:
        file_code = lang_code 

    file_name = f"{file_code}.json"
    
    # [Project Root]/assets/lang/en-us.json
    # 2. Construção do Caminho (Onde o erro estava)
    lang_path = os.path.join(root_dir, 'assets', 'lang', file_name)
    
    # DEBUG: Mostrar o caminho do JSON antes de tentar abrir
    debug_path("lang_path (JSON)", lang_path)
    
    try:
        with open(lang_path, 'r', encoding='utf-8') as f:
            lang_data = json.load(f)
            
        title_key = f"{sheet_key}_SHEET_TITLE"
        
        # Tenta retornar o título encontrado, ou usa um fallback genérico
        return lang_data.get(title_key, f"Ficha de {sheet_key}")
        
    except FileNotFoundError:
        print(f"Aviso: Ficheiro de idioma não encontrado. Caminho tentado: {lang_path}", file=sys.stderr)
        return f"Ficha de {sheet_key}"
    
    except Exception as e:
        print(f"Aviso: Falha geral ao carregar título JSON: {e}", file=sys.stderr)
        return f"Ficha de {sheet_key}"

# ============================================================
# API PYTHON PARA JAVASCRIPT (Necessária para a navegação interna)
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
    
    # 2. SELEÇÃO DE FICHA REVERTIDA: Assumimos sempre PC Sheet no lançamento direto
    sheet_key = 'PC' 
    
    # 3. Caminhos e Servidor
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # SUBSTITUA PELA LÓGICA DE SUBIR DOIS NÍVEIS:
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    
    # 4. Inicia o Servidor e recebe a porta real utilizada
    httpd, actual_port = start_server(root_dir, config['SERVER_PORT'])
    config['SERVER_PORT'] = actual_port
    
    # 5. Carregar Título da Janela do JSON (para o título da janela)
    window_title_suffix = load_title_from_json(
        root_dir, 
        config['DEFAULT_LANG'], 
        sheet_key
    )
    full_window_title = f"Nárëquenta: {window_title_suffix}"
    
    # 6. Constrói o URL
    initial_sheet_path = SHEET_MAP_AGNOSTIC[sheet_key] # Caminho para a Ficha PC
    base_url = f"http://localhost:{config['SERVER_PORT']}"
    
    # O idioma é carregado do config['DEFAULT_LANG']
    first_url = f"{base_url}/{initial_sheet_path}?lang={config['DEFAULT_LANG']}"

    # 7. Cria a API e a janela
    api = Api(window=None, config=config, sheet_map=SHEET_MAP_AGNOSTIC)

    window = webview.create_window(
        title=full_window_title, # Usa o título multilíngue
        url=first_url,
        width=1000,
        height=1100,
        resizable=True,
        js_api=api # Expõe a API para a navegação interna
    )
    
    api.window = window

    # 8. Inicia o pywebview
    webview.start()

    # 9. Encerramento limpo
    httpd.shutdown()
    sys.exit(0)


if __name__ == "__main__":
    main()