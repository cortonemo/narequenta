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

PORT = 8000  # Local TCP port we'll bind the HTTP server to (http://localhost:8000)

# Map of language labels shown in the UI -> relative path to the corresponding HTML sheet.
# These relative paths are resolved from the project root, not from this script's folder.
SHEETS = {
    "English (US)": "en-us/playtest/sheets/pc_sheet_v0.2.html",
    "Português (PT)": "pt-pt/playtest/sheets/pc_sheet_v0.2.html",
    # "Français (FR)": "fr-fr/playtest/sheets/pc_sheet_v0.2.html",
}


class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Standard SimpleHTTPRequestHandler, but with suppressed console logging.

    http.server.SimpleHTTPRequestHandler will normally print a line to stdout
    for every request it serves (GET /something ... 200). That gets noisy.

    Overriding log_message silences that.
    """

    def log_message(self, format, *args):
        # swallow logs, keep console clean
        pass


def start_server(directory, port):
    """
    Start a simple HTTP server that serves static files from `directory`
    (which should be the root of your project repo).

    Why:
    - The character sheet HTML likely references CSS/JS/assets with relative
      paths like /en-us/... or /lang/... etc.
    - Loading the HTML file directly with file:// won't resolve those cleanly.
    - So we spin up a tiny local web server and point pywebview at http://localhost.

    How:
    - We chdir() into `directory`, because SimpleHTTPRequestHandler serves
      relative to the current working directory.
    - We create a TCPServer bound to ("" , port) which means "listen on all
      interfaces on that port".
    - We run serve_forever() in a daemon thread so that the main thread can
      continue and open the GUI.

    Returns:
        httpd (TCPServer): We hand this back so we can later shut it down.
    """
    # Change working directory so relative paths inside HTML/CSS work properly
    os.chdir(directory)

    handler = SilentHTTPRequestHandler

    # Build the HTTP server on the requested port
    httpd = socketserver.TCPServer(("", port), handler)

    # Launch server in background thread so it doesn't block the GUI
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    return httpd


def open_sheet_in_window(sheet_url, server):
    """
    Open the chosen character sheet (HTML) in a desktop window using pywebview.

    Behavior:
    - Creates a browser-like window (no address bar, just content).
    - Blocks until that window is closed.
    - After the window closes, we shut down the HTTP server and exit the process.

    Args:
        sheet_url (str): Full http://localhost:PORT/... URL to the sheet HTML.
        server (TCPServer): The server we started, so we can cleanly shut it down.
    """

    # Create the embedded browser window
    window = webview.create_window(
        title="Nárëquenta - Character Sheet",  # Window title bar text
        url=sheet_url,                         # URL served by our local HTTP server
        width=900,                             # Initial window width in pixels
        height=700,                            # Initial window height in pixels
        resizable=True,                        # Allow manual resize
    )

    # webview.start() enters its own event loop and BLOCKS until all webview
    # windows are closed by the user.
    webview.start()

    # Once the user closes the sheet window, execution resumes here.

    # Cleanly stop the HTTP server so the port is freed.
    server.shutdown()

    # Exit the entire Python process so nothing keeps running in the background.
    sys.exit(0)


def main():
    """
    App entry point.

    High-level flow:
    1. Compute relevant paths (script dir and project root dir).
    2. Build a small Tkinter window that lets the user choose a language.
    3. When the user clicks "Launch Sheet":
        - Validate the HTML file exists.
        - Start the local HTTP server rooted at the project directory.
        - Kill the Tkinter picker window.
        - Open the pywebview window pointed at that sheet URL.
        - When that window is closed, shut everything down.
    """

    # -------------------------------------------------
    # Resolve filesystem layout
    # -------------------------------------------------

    # Absolute path to the folder where THIS .py script lives.
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Assume the project root is the parent directory of this script directory.
    # Example:
    #   repo/
    #     launcher/this_script.py   <- script_dir
    #     en-us/playtest/sheets/... <- root_dir is repo/
    #
    # We go "one up" so relative paths in SHEETS resolve correctly.
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    # -------------------------------------------------
    # Build the language picker GUI (Tkinter)
    # -------------------------------------------------

    root = tk.Tk()
    root.title("Nárëquenta Playtest Launcher")

    # Fixed size launcher window. You asked for ~600x300.
    root.geometry("600x300")
    root.resizable(False, False)

    # Main frame with padding so it doesn't feel cramped
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    # Instruction label, bilingual
    title_label = ttk.Label(
        frame,
        text="Select your sheet language / Escolhe a tua língua:",
        wraplength=360,     # Wrap text so it doesn't overflow horizontally
        justify="center"    # Center-align the wrapped lines
    )
    title_label.pack(pady=(0, 12))

    # lang_var will hold the dropdown selection (StringVar is Tk's reactive string container)
    lang_var = tk.StringVar()

    # Preselect the first language defined in SHEETS
    first_lang = list(SHEETS.keys())[0]
    lang_var.set(first_lang)

    # Dropdown (OptionMenu) populated with the keys from SHEETS
    lang_dropdown = ttk.OptionMenu(frame, lang_var, first_lang, *SHEETS.keys())
    lang_dropdown.pack(pady=(0, 16))

    # -------------------------------------------------
    # Launch button callback
    # -------------------------------------------------

    def on_launch():
        """
        Triggered when the user clicks "Launch Sheet".

        Steps:
        - Read the selected language.
        - Look up the relative HTML path from SHEETS.
        - Check that file exists on disk (helps with folder mistakes).
        - Spin up the HTTP server pointing at the project root.
        - Build a localhost URL to the chosen sheet.
        - Destroy the Tkinter picker window.
        - Hand off to pywebview to render the sheet.
        """

        # Which language did the user pick in the dropdown
        chosen_label = lang_var.get()

        # Get the relative HTML file path, like "en-us/playtest/sheets/pc_sheet_v0.2.html"
        rel_sheet_path = SHEETS.get(chosen_label)
        if not rel_sheet_path:
            # Defensive: if somehow lang doesn't map to a path
            messagebox.showerror("Error", "Invalid selection.")
            return

        # Build full absolute path on disk to confirm it's really there
        full_sheet_path = os.path.join(root_dir, rel_sheet_path)

        # Check it's an actual file. If not, inform the user.
        if not os.path.isfile(full_sheet_path):
            messagebox.showerror(
                "File not found",
                (
                    "Can't find:\n"
                    f"{rel_sheet_path}\n\n"
                    "Check your folder structure."
                )
            )
            return

        # Start the local HTTP server with project root as document root.
        # This allows relative includes in the sheet (CSS, JS, images) to load.
        server = start_server(root_dir, PORT)

        # The sheet will now be reachable via localhost on our chosen port.
        sheet_url = f"http://localhost:{PORT}/{rel_sheet_path}"

        # Close the language picker window before opening the sheet browser window.
        root.destroy()

        # Open the sheet in a pywebview window. This call will block until the
        # user closes that window. After it returns, we shut down the server.
        open_sheet_in_window(sheet_url, server)

    # -------------------------------------------------
    # Launch button itself
    # -------------------------------------------------

    launch_btn = ttk.Button(frame, text="Launch Sheet", command=on_launch)
    launch_btn.pack()

    # Small footer / hint text:
    # - Shows which port we're binding
    # - Explains that the next window IS the sheet, not "another menu"
    footer_label = ttk.Label(
        frame,
        text=f"Port: {PORT} • The next window IS the sheet.",  # hint
        foreground="#555"  # subtle gray
    )
    footer_label.pack(pady=(16, 0))

    # Enter Tkinter's event loop, so the window stays responsive
    root.mainloop()


# Standard Python entry point guard.
# This lets you import this file in another module without auto-running main().
if __name__ == "__main__":
    main()
