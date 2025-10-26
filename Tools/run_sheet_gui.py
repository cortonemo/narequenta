import http.server
import socketserver
import threading
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import webview  # pip install pywebview

# =====================================================
# CONFIG
# =====================================================

PORT = 8000

SHEETS = {
    "English (US)": "en-us/playtest/sheets/pc_sheet_v0.2.html",
    "Português (PT)": "pt-pt/playtest/sheets/pc_sheet_v0.2.html",
    # "Français (FR)": "fr-fr/playtest/sheets/pc_sheet_v0.2.html",
}

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # don't spam console
        pass

def start_server(directory, port):
    """
    Serve the project root so /lang/... and /en-us/... resolve.
    Runs in background thread.
    """
    os.chdir(directory)
    handler = SilentHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd

def open_sheet_in_window(sheet_url, server):
    """
    Open the chosen sheet inside a pywebview window.
    Keep process alive until the user closes that window.
    """
    # Create the webview window
    window = webview.create_window(
        title="Nárëquenta - Character Sheet",
        url=sheet_url,
        width=900,
        height=700,
        resizable=True,
    )

    # This blocks until the window is closed
    webview.start()

    # After closing the sheet window, shut down server and exit
    server.shutdown()
    sys.exit(0)

def main():
    # figure out paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    # GUI 1: language picker
    root = tk.Tk()
    root.title("Nárëquenta Playtest Launcher")

    # Adjusted sizing per your ask
    root.geometry("400x200")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    title_label = ttk.Label(
        frame,
        text="Select your sheet language / Escolhe a tua língua:",
        wraplength=360,
        justify="center"
    )
    title_label.pack(pady=(0, 12))

    lang_var = tk.StringVar()
    first_lang = list(SHEETS.keys())[0]
    lang_var.set(first_lang)

    lang_dropdown = ttk.OptionMenu(frame, lang_var, first_lang, *SHEETS.keys())
    lang_dropdown.pack(pady=(0, 16))

    def on_launch():
        chosen_label = lang_var.get()

        rel_sheet_path = SHEETS.get(chosen_label)
        if not rel_sheet_path:
            messagebox.showerror("Error", "Invalid selection.")
            return

        full_sheet_path = os.path.join(root_dir, rel_sheet_path)
        if not os.path.isfile(full_sheet_path):
            messagebox.showerror(
                "File not found",
                f"Can't find:\n{rel_sheet_path}\n\nCheck your folder structure."
            )
            return

        # start HTTP server rooted at project root
        server = start_server(root_dir, PORT)

        # build URL for that sheet
        sheet_url = f"http://localhost:{PORT}/{rel_sheet_path}"

        # destroy the language picker window before opening the sheet window
        root.destroy()

        # now open pywebview window with the sheet embedded
        open_sheet_in_window(sheet_url, server)

    launch_btn = ttk.Button(frame, text="Launch Sheet", command=on_launch)
    launch_btn.pack()

    footer_label = ttk.Label(
        frame,
        text=f"Port: {PORT} • A nova janela já é a ficha.",
        foreground="#555"
    )
    footer_label.pack(pady=(16, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
