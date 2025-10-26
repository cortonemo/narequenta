# Ficheiro: Tools/config.py

# ============================================================
# CONFIGURAÇÃO DE AMBIENTE E SERVIDOR
# ============================================================
PORT = 8000
DEFAULT_LANG = "pt" # Definido para português (pt-pt) por defeito
LANDING_PAGE_PATH = "html/index.html" # NOVO CAMINHO: dentro da pasta 'html/'

# ============================================================
# CONFIGURAÇÃO DE FICHAS E CLASSES
# Os caminhos são relativos ao ROOT do repositório (G:\Git\narequenta)
# ============================================================

SHEET_CONFIG = {
    # Fichas de Personagem Jogável (PC)
    "pc": {
        "warrior": {
            "en": "en-us/playtest/sheets/pc_sheet_v0.2.html",
            "pt": "pt-pt/playtest/sheets/pc_sheet_v0.2.html",
        },
        "mage": {
            # Assumindo que criará ficheiros específicos para outras classes
            "en": "en-us/playtest/sheets/pc_sheet_mage.html",
            "pt": "pt-pt/playtest/sheets/pc_sheet_v0.2t.html", # Usando o template existente
        },
        "rogue": {
            "en": "en-us/playtest/sheets/pc_sheet_rogue.html",
            "pt": "pt-pt/playtest/sheets/pc_sheet_rogue.html",
        },
    },
    # Fichas de Personagem Não-Jogável (NPC)
    "npc": {
        # NPCs usam um modelo 'default' simples
        "default": {
            "en": "en-us/playtest/sheets/npc_sheet_v0.2.html",
            "pt": "pt-pt/playtest/sheets/npc_sheet_v0.2.html",
        }
    }
}

# Definições de label de idioma (usadas pelo seletor de idioma dentro das fichas)
LANGUAGE_LABELS = {
    "en": "English (US)",
    "pt": "Português (PT)",
}

# Funções auxiliares para a API Bridge (usadas para trocar idioma dentro da ficha)
def get_available_languages():
    """Retorna os idiomas disponíveis (usamos as chaves pt/en de um PC, por exemplo)."""
    # Apenas retorna os idiomas que têm traduções no PC Warrior (ou o que for mais comum)
    return [
        {"code": code, "label": LANGUAGE_LABELS.get(code, code)}
        for code in SHEET_CONFIG["pc"]["warrior"].keys()
    ]
