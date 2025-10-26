# Nárëquenta — Contos do Esvanecer

Change Log

All notable changes to this project will be documented in this file.
The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

## [v0.1] — 2025-10-25

**Status:** Private Development (Prova de Origem)
**Highlights**
- **Estabelecido** o mecanismo principal de auto-atrito: Ações consomem percentagens do Facet.
- **Definido** o sistema de "Cicatrização" opcional que reduz o valor máximo em troca de eficiência.
- **Definido** cinco Facetas do Ser: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
- **Adicionado** Fase de Recuperação e regra de Fim de Jogo.

**Estrutura**
/rules/core_rules_v0.1.md
/playtest/character_sheet_v0.1.md
/playtest/gm_reference_v0.1.md

---

## [v0.2] — 2025-10-26 (Design Framework)

**Status:** Alpha Test Readiness
**Highlights**
- **Alterado** a nomenclatura dos Facets para **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
- **Adicionado** a separação crítica entre **Essência Máxima ($\mathbf{E_{max}}$)** e **Essência Atual ($\mathbf{E_{cur}}$)**.
- **Adicionado** a **Waning Scale** (Escala do Esvanecer), onde $\mathbf{E_{max}}$ baixo concede bónus de **Eficiência ($\mathbf{A_{rate}}$)**.
- **Adicionado** Resolução de Ação por **Rolagem Híbrida** (E_P + E_S) e o sistema de Dano Mitigado por $\mathbf{E_{max}}$.
- **Adicionado** suporte Multilíngue (PT-PT / EN-US) e a lógica de automação da ficha.

---

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)

**Status:** Alpha Test Readiness
**Highlights**
- **Removido** o custo de Atrição ($\mathbf{E_{cur}}$) para a maioria das ações fora de combate (Ex: Social, Investigação).
- **Adicionado** regra de Custo Fixo de **$\mathbf{2\%}$** para situações de stress extremo fora de combate.
- **Adicionado** a **Penalidade Simétrica ($\mathbf{10}$)** para NPCs, recompensando o bónus narrativo/tático do jogador em testes contestados.

---

## [v0.4] — 2025-10-26 (Final Progress Loop)

**Status:** Alpha Test Ready
**Highlights**
- **Removido** o sistema de **Cicatrização por Marcos de Decadência** e a regra de Reafetação de 10% (obsoletos).
- **Adicionado** a nova regra de progressão e decaimento: **A Rolagem do Esvanecer (Waning Roll)**.
    - **Decaimento Universal:** $\mathbf{2\text{d}6}$ subtraídos da $\mathbf{E_{max}}$ no final de cada capítulo.
    - **Escolha de Proficiência:** O PC rola $\mathbf{4\text{d}6}$ (maior risco de decaimento) em troca de **$\mathbf{2\text{d}10}$ Dados de Proficiência ($\mathbf{D_{prof}}$)** permanentes, aumentando a fiabilidade.
- **Corrigido** o título do jogo para **Nárëquenta — Contos do Esvanecer**.

---

🧾 Version Key

Type | Meaning
:---|:---
**Added**| Novo recurso ou mecânica
**Changed**| Regra ajustada ou reequilibrada
**Removed**| Mecânica ou ficheiro removido
**Fixed**| Correção ou erro tipográfico

🪶 Credits

Design & Writing — Serelith Varn
System Development & Documentation — GPT-5 (Liora Vex Framework)
“Somos lembrados pela forma elegante como nos desvanecemos.”

© 2025 Serelith Varn — Nárëquenta: Contos do Escurecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte LICENSE.md.

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
