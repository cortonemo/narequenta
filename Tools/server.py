# Ficheiro: Tools/server.py
import http.server
import socketserver
import threading
import os
import sys
import webview

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Manipulador para silenciar o 'spam' da consola padrão do servidor."""
    def log_message(self, format, *args):
        pass

def start_server(directory, port):
    """
    Serve o diretório raiz via um servidor HTTP local num thread em background.
    Retorna a instância do servidor.
    """
    # Adiciona o diretório do script ao PATH para que as imports relativas funcionem
    if directory not in sys.path:
        sys.path.append(directory)
        
    # Salva o diretório de trabalho atual e move-se para o root do repo para servir ficheiros
    original_cwd = os.getcwd()
    try:
        os.chdir(directory)
        handler = SilentHTTPRequestHandler
        
        # TCPServer em vez de HTTPServer (mais simples para uso local)
        httpd = socketserver.TCPServer(("", port), handler)
        
        # Inicia o servidor num thread demon
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        
        return httpd
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
        # Volta ao diretório original em caso de falha
        os.chdir(original_cwd)
        return None

def stop_server(server_instance):
    """Encerra o servidor HTTP."""
    if server_instance:
        server_instance.shutdown()
