Compreendido. Irei adicionar as alterações de hoje, que representam a estabilização da arquitetura *front-end* e correções críticas no *launcher* Python, sob a versão **v0.8**.

Aqui está o `Change Log` atualizado com a nova entrada:

## 📜 Nárëquenta — Contos do Esvanecer

**Change Log**

All notable changes to this project will be documented in this file.
The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

## [v0.1] — 2025-10-25 (Private Development)
**Status:** Prova de Origem
* **Added:** Estabelecido o mecanismo principal de auto-atrito: Ações consomem percentagens do Facet.
* **Added:** Definido o sistema de "Cicatrização" opcional que reduz o valor máximo em troca de eficiência.
* **Added:** Definido cinco Facetas do Ser: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
* **Added:** Adicionado Fase de Recuperação e regra de Fim de Jogo.

***

## [v0.2] — 2025-10-26 (Design Framework)
**Status:** Alpha Test Readiness
* **Changed:** Alterado a nomenclatura dos Facets para **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
* **Added:** Adicionado a separação crítica entre **Essência Máxima ($\mathbf{E_{max}}$)** e **Essência Atual ($\mathbf{E_{cur}}$)**.
* **Added:** Adicionado a **Waning Scale** (Escala do Esvanecer), onde $\mathbf{E_{max}}$ baixo concede bónus de **Eficiência ($\mathbf{A_{rate}}$)**.
* **Added:** Adicionado Resolução de Ação por **Rolagem Híbrida** ($\mathbf{E_P + E_S}$) e o sistema de Dano Mitigado por $\mathbf{E_{max}}$.
* **Added:** Adicionado suporte Multilíngue (PT-PT / EN-US) e a lógica de automação da ficha.

***

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)
**Status:** Alpha Test Readiness
* **Removed:** Removido o custo de Atrição ($\mathbf{E_{cur}}$) para a maioria das ações fora de combate (Ex: Social, Investigação).
* **Added:** Adicionado regra de Custo Fixo de **$\mathbf{2\%}$** para situações de stress extremo fora de combate.
* **Added:** Adicionado a **Penalidade Simétrica ($\mathbf{10}$)** para NPCs, recompensando o bónus narrativo/tático do jogador em testes contestados.

***

## [v0.4] — 2025-10-26 (Final Progress Loop)
**Status:** Alpha Test Ready
* **Removed:** Removido o sistema de **Cicatrização por Marcos de Decadência** e a regra de Reafetação de 10% (obsoletos).
* **Changed:** Alterado a regra de progressão e decaimento para a **Rolagem do Esvanecer (Waning Roll)**.
* **Changed:** A Escolha de Proficiência passa a rolar $\mathbf{4\text{d}6}$ (maior risco de decaimento) em troca de **$\mathbf{2\text{d}10}$ Dados de Proficiência ($\mathbf{D_{prof}}$)** permanentes.
* **Fixed:** Corrigido o título do jogo para **Nárëquenta — Contos do Esvanecer**.

***

## [v0.5] — 2025-10-27 (Rolagens de Ataque e Contested Rolls)
**Status:** Alpha Test Ready - Ciclo de Combate Central Definido
* **Changed:** O sistema de Resolução de Ação passa a ser por **Rolagens Contestadas**.
* **Added:** Adicionado **Tiers de Proficiência e Mapeamento de Dados** que ligam o decaimento da $\mathbf{E_{max}}$ à aquisição de Dados de Proficiência ($\mathbf{D_{prof}}$).
* **Changed:** A **Rolagem do Esvanecer** é agora o principal mecanismo para converter a perda de $\mathbf{E_{max}}$ em $\mathbf{D_{prof}}$.
* **Added:** Adicionado Sistema de **Resultados Críticos** e **Mitigação de Proficiência** ($\mathbf{D_{prof}}$ subtrai do resultado do $\mathbf{d100}$).
* **Added:** Adicionado **Ataques Especiais** por troca de $\mathbf{D_{prof}}$.

***

## [v0.7] — 2025-11-14 (Precision Lethality & Tier-Neutral Balance)
**Status:** Alpha Test Ready - Core Ruleset Finalizado
* **Changed:** Aumento de Versão de v0.5 para v0.7 devido à **reestruturação completa da progressão e do combate**.
* **Added:** Adicionado a **Erosão Inicial ($\mathbf{1\text{d}10}$)** para todos os Essences na criação.
* **Added:** Adicionado o **Limite Máximo ($\mathbf{50\%}$)** para $\mathbf{E_{max}}$, definindo o teto de sucesso permanente.
* **Changed:** A **Tabela de Tier de Proficiência** foi alterada para **Progressão Uniforme ($\mathbf{1\text{d}10}$ por Tier)**, simplificando a escala e aumentando o poder.
* **Changed:** O papel de $\mathbf{D_{prof}}$ foi **Unificado** para: 1) Mitigação de Erro, 2) Redução de Atrição, e 3) **Dano Base Aditivo ($\mathbf{R_{prof}}$)**.
* **Added:** Adicionado a **Fórmula de Dano Aditiva** (Letalidade de Precisão): $\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defesa} + D_{Margin} + R_{prof}) \right)$.
* **Added:** Adicionado o **Multiplicador de Vantagem de Nível Defensivo ($\mathbf{M_{DTA}}$)** para reduzir o dano de inimigos de Tier inferior ($\Delta T \ge 1$).
* **Added:** Adicionado a **Progressão de Impulso de Ação (AS)**, ligando o número de Impulsos de Ação disponíveis ao Tier de Proficiência (até 4 AS no Tier V).
* **Changed:** O **Custo de Atrição** foi mitigado e simplificado para: $\mathbf{E_{cur} \text{ Perda}} = \max \left( 0, (7 - R_{prof}) \right)$.
* **Added:** Adicionado a regra de **Pares de Essência Motor/Qualidade** para determinar quais $\mathbf{E_{cur}}$ pools são gastos em combate.

***

## **[v0.8] — 2025-11-15 (SPA Migration & Launcher Stabilization)**
**Status:** Alpha Test Ready - Arquitetura Estabilizada
* **Added:** Implementação da arquitetura **Single Page Application (SPA)** no `index.html`, unificando as três fichas (`PC`, `NPC`, `GM_REF`) numa única página.
* **Added:** Integração completa da **Calculadora de Dano** na secção de Referência GM (`index.html`).
* **Added:** Todos os cabeçalhos e descrições da Referência GM agora suportam **Localização Multilíngue** (`data-lang`).
* **Removed:** Ficheiros HTML obsoletos (`pc_sheet.html`, `npc_sheet.html`, `gm_reference.html`).
* **Changed:** A navegação da ficha foi migrada do *reload* de página para **transições internas de *view* por JavaScript** (`showSheet()`), eliminando *glitches* de *threading* e aumentando a estabilidade da aplicação.
* **Fixed:** Corrigido o cálculo do **caminho de raiz** (*root\_dir*) no *launcher* Python (`sheet_gui.py`) para resolver o erro fatal de duplicação de caminho ao carregar os ficheiros JSON de localização.
* **Fixed:** Corrigida a lógica de *handling* de erros da API `pywebview` e de mapeamento de caminhos para o seletor de idioma, garantindo a inicialização robusta da língua.

***

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

© 2025 Serelith Varn — Nárëquenta: Contos do Esvanecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte LICENSE.md.

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under a Nárëquenta Limited Open License (v0.1). See LICENSE.md.




© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
