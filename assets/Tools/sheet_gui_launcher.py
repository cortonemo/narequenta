import webview
import os
import json

# --- PATH CONFIGURATION ---
# BASE_DIR is the directory containing the script: .../narequenta-main/assets/Tools/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Get the path to 'assets':
# .../narequenta-main/assets/Tools/ -> .../narequenta-main/assets/
ASSETS_DIR = os.path.dirname(BASE_DIR)

# 2. Get the project root 'narequenta-main':
# .../narequenta-main/assets/ -> .../narequenta-main/
PROJECT_ROOT = os.path.dirname(ASSETS_DIR)

# Recalculate paths starting from the PROJECT_ROOT.

# LANG_DIR remains the same as it's correctly under 'assets/lang'
LANG_DIR = os.path.join(PROJECT_ROOT, 'assets', 'lang')

# MODULES_DIR must now include the 'assets' directory in its path.
# Corrected path: PROJECT_ROOT / assets / Templates / modules
MODULES_DIR = os.path.join(PROJECT_ROOT, 'assets', 'Templates', 'modules')

# --- NÁRËQUENTA STATIC DATA ---
# (Used for Tier lookups; these should align with the GM Reference table)
TIER_DATA = {
    'V': {'dice': '5d10', 'avg': 27.5, 'as': 5}, 'IV': {'dice': '4d10', 'avg': 22.0, 'as': 4},
    'III': {'dice': '3d10', 'avg': 16.5, 'as': 3}, 'II': {'dice': '2d10', 'avg': 11.0, 'as': 2},
    'I': {'dice': '1d10', 'avg': 5.5, 'as': 1}, '0': {'dice': 'None', 'avg': 0.0, 'as': 0}
}
# Set Base Language to English (en-us)
DEFAULT_LANG = 'en-us'

# --- DATA LOADING FUNCTIONS ---

def load_language_data(lang_code):
    """Loads the JSON language file."""
    try:
        # NOTE: Using a relative path for demonstration. In a real setup, 
        # the structure needs to be respected (e.g., 'assets/lang/en-us.json').
        lang_path = os.path.join(LANG_DIR, f'{lang_code}.json')
        with open(lang_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        # Fallback for missing language files
        print(f"Error loading language {lang_code}: {e}")
        return {
            "GAME_TITLE": "Nárëquenta: Tales of the Waning",
            "SHEET_SUBTITLE": "Sheet Selection (EN-US Fallback)",
            "PC_SHEET_TITLE": "Character Sheet",
            "NPC_SHEET_TITLE": "Adversary Reference",
            "GM_REF_SHEET_TITLE": "GM Rules Reference"
            # Add other required keys here for robustness
        }

def load_template_fragment(filename):
    """Loads an HTML fragment from the modules directory."""
    try:
        path = os.path.join(MODULES_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        # Fallback if the template is not found (Crucial for the skeleton)
        print(f"WARNING: Could not load module {filename}. Using skeleton content.")
        return f'<div id="FALLBACK_ERROR">ERROR: Module {filename} not found. Ensure the directory {MODULES_DIR} exists.</div>'

# --- TEMPLATE ASSEMBLY FUNCTION (FINAL WORKING VERSION) ---

def assemble_sheet(sheet_key, lang_data):
    """Assembles the final HTML sheet based on the key and language data."""
    
    # 1. Load Base Template (Must contain the HTML wrapper and placeholders)
    base_html = load_template_fragment('base_template.html')
    
    # 2. Determine Content Module and Title Key
    if sheet_key == 'PC':
        content_module = 'pc_view_content.html'
        title_key = 'PC_SHEET_TITLE'
    elif sheet_key == 'NPC':
        content_module = 'npc_view_content.html'
        title_key = 'NPC_SHEET_TITLE'
    elif sheet_key == 'GM_REF':
        content_module = 'gm_ref_content.html'
        title_key = 'GM_REF_SHEET_TITLE'
    else: # SELECTION
        content_module = 'selection_view_content.html'
        title_key = 'SHEET_SUBTITLE'

    # 3. Load Additional Fragments
    content_html = load_template_fragment(content_module)
    # The navigation bar is replaced by a single space if it's the selection screen.
    nav_html = load_template_fragment('navigation_bar.html') if sheet_key != 'SELECTION' else ' '
    
    # 4. Data Injection and Assembly (Controlled Replacement)
    
    # Language Data Lookup
    game_title = lang_data.get('GAME_TITLE', 'Nárëquenta: Tales of the Waning')
    sheet_title = lang_data.get(title_key, sheet_key)
    
    # NOTE: The final_html variable should be initialized to ensure replacement chains correctly.
    final_html = base_html

    # 4.1. Inject Titles and Navigation 
    final_html = final_html.replace('{{SHEET_TITLE}}', sheet_title)
    final_html = final_html.replace('{{GAME_TITLE}}', game_title)
    final_html = final_html.replace('{{NAV_BAR}}', nav_html) 

    # 4.2. Inject Main Content
    final_html = final_html.replace('{{VIEW_CONTENT}}', content_html)
    
    # --- START NEW SECTION 4.3: INJECT INLINE STYLES ---
    # This assumes PROJECT_ROOT is defined in the module scope
    STYLE_PATH = os.path.join(PROJECT_ROOT, 'assets', 'css', 'style.css') 
    
    try:
        with open(STYLE_PATH, 'r', encoding='utf-8') as f:
            style_css = f.read()
        # Replace the style placeholder (e.g., {{INLINE_STYLE}}) in base_html
        final_html = final_html.replace('{{INLINE_STYLE}}', f'<style>{style_css}</style>')
    except FileNotFoundError:
        # Lumenroot directive: Ensure execution blocks only if essential. 
        # For non-critical resources like styles, minimize blocking.
        print(f"Lumenroot WARNING: CSS file not found at {STYLE_PATH}. Proceeding without inline styles.")
        final_html = final_html.replace('{{INLINE_STYLE}}', '') # Clear placeholder
    # --- END NEW SECTION 4.3 ---

    # 4.4. Inject Language Data for Frontend JS (Original 4.3)
    lang_json_str = json.dumps(lang_data)
    final_html = final_html.replace('// LANGUAGE_DATA_JS_PLACEHOLDER', f'const currentLanguage = {lang_json_str};')

    # 4.5. Set Initial Frontend Logic (Cleanup remaining placeholders) (Original 4.4)
    if sheet_key != 'SELECTION':
        js_func_call = "document.getElementById('sheet-title-display').textContent = currentLanguage['" + title_key + "'];"
        final_html = final_html.replace('// INIT_FRONTEND_LOGIC_PLACEHOLDER', js_func_call)
    else:
          final_html = final_html.replace('// INIT_FRONTEND_LOGIC_PLACEHOLDER', '')

    return final_html

# --- API AND MAIN LOGIC (FINAL REVISION) ---

class NarequentaAPI:
    """API that exposes Python methods to JavaScript via pywebview."""
    
    # We simplify __init__ since window is not strictly needed for assembly
    def __init__(self, lang_data):
        self.lang_data = lang_data
    
    def load_sheet(self, sheet_key):
        """Method called by JavaScript to request a new sheet."""
        print(f"API: Requested sheet: {sheet_key}")
        
        # Assemble the new sheet
        assembled_html = assemble_sheet(sheet_key, self.lang_data)
        
        # Returns the HTML string to the frontend (which needs JS logic to handle it)
        return assembled_html

# --- API AND MAIN LOGIC (FINAL REVISION WITH DEBUG) ---

def start_gui():
    """Starts the pywebview application."""
    
    # 1. Load language data and assemble the initial sheet
    lang_data = load_language_data(DEFAULT_LANG)
    
    # 2. Assemble the initial SELECTION view
    initial_html = assemble_sheet('SELECTION', lang_data)
    
    # DEBUG STEP: Print the entire assembled HTML string to the console
    # print("\n--- DEBUG: INITIAL ASSEMBLED HTML CONTENT START ---")
    # print(initial_html)
    # print("--- DEBUG: INITIAL ASSEMBLED HTML CONTENT END ---\n")
    
    # 3. Create API instance
    api = NarequentaAPI(lang_data)
    
    # 4. Initialize the Window
    window_title = lang_data.get('GAME_TITLE', 'Nárëquenta')
    window = webview.create_window(
        window_title, 
        html=initial_html, 
        width=1000, 
        height=1100
    )
    
    # 5. Expose only the necessary method and start the GUI
    window.expose(api.load_sheet)
    
    webview.start() 

# --- EXECUTION ---
if __name__ == '__main__':
    print(f"Nárëquenta Launcher Initialized (Base Language: {DEFAULT_LANG}).")
    print(f"Templates Directory (Must Exist): {MODULES_DIR}")
    
    # Run the GUI
    start_gui()