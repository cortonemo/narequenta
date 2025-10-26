import http.server
import socketserver
import threading
import webbrowser
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# =====================================================
# CONFIG
# =====================================================

PORT = 8000

# Supported languages and their sheet paths.
# Key = label shown to player.
# Value = relative path to that locale's sheet HTML from project root.
SHEETS = {
    "English (US)": "en-us/playtest/sheets/pc_sheet_v0.2.html",
    "Português (PT)": "pt-pt/playtest/sheets/pc_sheet_v0.2.html",
    # Add more here later:
    # "Français (FR)": "fr-fr/playtest/sheets/pc_sheet_v0.2.html",
}

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # suppress console noise
        pass

def start_server(directory, port):
    """
    cd into the project root, start a background HTTP server there,
    and return the server object.
    """
    os.chdir(directory)
    handler = SilentHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)

    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd

def launch_browser(sheet_path, port, root_dir, server):
    """
    Open the chosen sheet in the user's browser and keep process alive.
    """
    sheet_url = f"http://localhost:{port}/{sheet_path}"

    print("======================================")
    print("Nárëquenta Playtest Sheet Launcher")
    print("======================================")
    print(f"Serving from: {root_dir}")
    print(f"Open in browser: {sheet_url}")
    print("Close this window / terminal to stop.")
    print("======================================")

    webbrowser.open(sheet_url)

    try:
        # Block forever until Ctrl+C or window close kills process
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")
        server.shutdown()
        sys.exit(0)

def main():
    # Resolve directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    # Build a tiny GUI to choose language
    root = tk.Tk()
    root.title("Nárëquenta Playtest Launcher")

    # Window sizing / no resize drama
    root.geometry("360x160")
    root.resizable(False, False)

    # Frame padding
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    # Title label
    title_label = ttk.Label(
        frame,
        text="Select your sheet language / Escolhe a tua língua:",
        wraplength=320,
        justify="center"
    )
    title_label.pack(pady=(0, 12))

    # Dropdown
    lang_var = tk.StringVar()
    # set default = first key in SHEETS
    first_lang = list(SHEETS.keys())[0]
    lang_var.set(first_lang)

    lang_dropdown = ttk.OptionMenu(frame, lang_var, first_lang, *SHEETS.keys())
    lang_dropdown.pack(pady=(0, 16))

    # Launch button logic
    def on_launch():
        chosen_label = lang_var.get()
        if chosen_label not in SHEETS:
            messagebox.showerror("Error", "Invalid selection.")
            return

        rel_sheet_path = SHEETS[chosen_label]

        # check file exists before spinning server
        full_sheet_path = os.path.join(root_dir, rel_sheet_path)
        if not os.path.isfile(full_sheet_path):
            messagebox.showerror(
                "File not found",
                f"Can't find:\n{rel_sheet_path}\n\nCheck your folder structure."
            )
            return

        # start server
        server = start_server(root_dir, PORT)

        # destroy GUI window so we don't keep two UIs alive
        root.destroy()

        # launch browser + hold
        launch_browser(rel_sheet_path, PORT, root_dir, server)

    # Button
    launch_btn = ttk.Button(frame, text="Launch Sheet", command=on_launch)
    launch_btn.pack()

    # Info footer
    footer_label = ttk.Label(
        frame,
        text=f"Port: {PORT}   •   This window will close after launch.",
        foreground="#555"
    )
    footer_label.pack(pady=(16, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
