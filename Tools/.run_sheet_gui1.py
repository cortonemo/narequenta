"""
Nárëquenta Sheet Viewer with in-window language switcher
Stable build for pywebview 6.1 (Edge/WebView2, Windows)

Changes from previous version:
- Uses window.expose() per method (6.x requirement)
- Keeps safe navigation via evaluate_js (no COM/thread errors)
- Returns None on JS-exposed functions to avoid callback crashes
"""

import http.server
import socketserver
import threading
import os
import sys
import webview


# ============================================================
# CONFIGURATION
# ============================================================

PORT = 8000

SHEETS = {
    "en": "en-us/playtest/sheets/pc_sheet_v0.2.html",
    "pt": "pt-pt/playtest/sheets/pc_sheet_v0.2.html",
}

DEFAULT_LANG = "en"


class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Silence default console spam."""
    def log_message(self, format, *args):
        pass


def start_server(directory, port):
    """Serve repo root via a tiny local HTTP server in a background thread."""
    os.chdir(directory)
    handler = SilentHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd


# ============================================================
# API METHODS (EXPOSED TO JS)
# ============================================================

def make_get_languages():
    """Factory so we can capture current SHEETS cleanly."""
    def get_languages():
        """Return list of available languages to JS."""
        return [
            {"code": code, "label": "English (US)" if code == "en" else "Português (PT)"}
            for code in SHEETS.keys()
        ]
    return get_languages


def make_switch_language(window, base_url):
    """Factory creating the JS-callable function to switch sheet."""
    def switch_language(lang_code):
        """Tell the webview to navigate to another sheet."""
        if lang_code not in SHEETS:
            return None

        rel_path = SHEETS[lang_code]
        new_url = f"{base_url}/{rel_path}"

        # Safe navigation: run inside the webview via evaluate_js
        window.evaluate_js(f'window.location.href = "{new_url}";')
        return None  # returning None avoids callback confusion

    return switch_language


# ============================================================
# MAIN
# ============================================================

def main():
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    # Start HTTP server
    server = start_server(root_dir, PORT)

    # Build initial URL
    first_url = f"http://localhost:{PORT}/{SHEETS[DEFAULT_LANG]}"

    # Create window
    window = webview.create_window(
        title="Nárëquenta - Character Sheet",
        url=first_url,
        width=1000,
        height=700,
        resizable=True,
    )

    # Expose functions (must be top-level callables for pywebview 6.x)
    base_url = f"http://localhost:{PORT}"
    window.expose(make_get_languages())
    window.expose(make_switch_language(window, base_url))

    # Launch GUI loop (blocks until closed)
    webview.start()

    # Clean shutdown
    server.shutdown()
    sys.exit(0)


if __name__ == "__main__":
    main()
