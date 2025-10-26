# Ficheiro: Tools/api_bridge.py

# Nota: As importações relativas assumem que todos os módulos estão
# dentro da mesma pasta de 'Tools' e são executados como um pacote.

from . import config

# ============================================================
# FUNÇÕES EXPOSTAS AO JAVASCRIPT
# ============================================================

def make_get_languages():
    """Factory para criar a função getLanguages que o JS chamará."""
    def get_languages():
        """Retorna a lista de idiomas disponíveis ao JavaScript."""
        return config.get_available_languages()
    return get_languages


def make_switch_language(window, base_url):
    """
    Factory para criar a função switchLanguage que o JS chamará.
    Esta função só é chamada *DEPOIS* da ficha ser carregada.
    """
    def switch_language(lang_code, sheet_type, sheet_class):
        """
        Navega o webview para a folha de idioma selecionada,
        mantendo o tipo (PC/NPC) e a classe/modelo.
        """
        try:
            # Encontra o caminho relativo usando a configuração guardada
            rel_path = config.SHEET_CONFIG[sheet_type][sheet_class][lang_code]
        except KeyError:
            print(f"Erro: Combinação de idioma/ficha inválida: {lang_code}/{sheet_type}/{sheet_class}")
            return None

        new_url = f"{base_url}/{rel_path}"
        window.evaluate_js(f'window.location.href = "{new_url}";')
        return None

    return switch_language


def make_load_sheet(window, base_url):
    """
    Factory para criar a NOVA função loadSheet(type, class) que o JS chamará.
    Isto é chamado a partir do index.html.
    """
    def load_sheet(sheet_type, sheet_class):
        """
        Calcula o caminho da ficha com base no tipo (pc/npc) e na classe/modelo,
        usando o idioma por defeito.
        """
        # Sempre usa o idioma por defeito (config.DEFAULT_LANG) para a navegação inicial
        try:
            rel_path = config.SHEET_CONFIG[sheet_type][sheet_class][config.DEFAULT_LANG]
        except KeyError:
            print(f"Erro: Configuração de ficha inválida: {sheet_type}/{sheet_class}")
            return None

        # Constrói o URL
        new_url = f"{base_url}/{rel_path}"

        # Navega para a ficha final
        window.evaluate_js(f'window.location.href = "{new_url}";')
        return None

    return load_sheet