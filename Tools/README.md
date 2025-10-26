# Nárëquenta Playtest Launcher

This directory contains the necessary Python script to launch the HTML character sheets and the core logic required for future automation.

---

## 🚀 1. Run Sheet GUI (`run_sheet_gui.py`)

This script starts a local HTTP server and opens a GUI window to select the character sheet language. This is necessary because HTML sheets cannot load external JSON files (for language data) directly from the local file system due to browser security restrictions (CORS).

### Prerequisites

To run the script, you must have **Python 3.x** installed, along with two specific libraries:

1.  **pywebview:** Used to open the character sheet in a clean desktop window.
2.  **tkinter (usually included with Python):** Used for the initial language selection window.

Install the necessary external dependency via pip:

```bash
pip install pywebview