# 📜 Nárëquenta — Contos do Declínio

**Registo de Alterações (Change Log)**

Todas as alterações notáveis a este projeto serão documentadas neste ficheiro.

O formato é inspirado em Keep a Changelog, e adere ao Versionamento Semântico quando aplicável.

---

## [v0.9.64] — 2025-12-01 (Recuperação Unificada)
**Status:** Refinamento Beta - Ajuste de Ciclo de Jogo
- **Changed:** Alterada a regra de **Renovação de Foco (Descanso Longo)**. A restauração de $\mathbf{E_{cur}}$ agora vai até **100%** (Zona de Pico), não sendo mais limitada pelo valor atual de $\mathbf{E_{max}}$. O limite de $\mathbf{E_{max}}$ aplica-se apenas a testes de dificuldade.
- **Added:** Definida a fórmula de **Descanso Curto** como a **Soma dos resultados de $\mathbf{D_{prof}}$** (ou 1d10 para Tier 0).
- **Added:** Adicionada a mecânica de **Recuperação de Emergência (Fôlego Rápido)**, permitindo gastar uma ação completa para realizar um Descanso Curto quando o Vigor atinge zero.
- **Fixed:** Consolidação dos ficheiros de Regras Centrais e Rituais num único fluxo lógico para facilitar a consulta.

---

## [v0.9.6] — 2025-11-28 (Letalidade de Precisão & Zonas de Tensão)
**Status:** Refinamento Beta - Atualização Matemática Central
- **Changed:** **Limiar de Sucesso** alterado. O sucesso é agora $\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalidade}})$. A Essência Atual ($\mathbf{E_{cur}}$) determina apenas a Zona.
- **Added:** **Zonas de Tensão** definidas: **Pico** (-0), **Minguante** (-10), **Desvanecente** (-20) e **Vazio** (-30).
- **Changed:** **Fórmula de Atrição** atualizada para refletir o Peso do Equipamento.
    - Antigo: $\max(0, 7 - R_{prof})$.
    - Novo: $\max(0, \mathbf{Peso} - \lfloor R_{prof}/2 \rfloor)$.
- **Added:** **Classes de Peso** definidas como Leve (**10%**), Médio (**15%**) e Pesado (**20%**).
- **Changed:** **Fórmula de Dano** atualizada para incluir um **Piso Rígido**. O dano já não pode ser reduzido abaixo do resultado bruto de $\mathbf{R_{prof}}$ pela mitigação (antes dos Multiplicadores de Tier).
- **Fixed:** Ficheiros de localização (`pt.json`) atualizados para refletir as novas fórmulas de Atrição e Sucesso.

---

## [v0.9] — 2025-11-17 (Maestria Progressiva & Controlo de Atrição)
**Status:** Lógica de Progressão Finalizada
- **Changed:** A progressão por perda de $\mathbf{E_{max}}$ é agora estritamente sequencial (um Tier de cada vez).
- **Added:** Regra de Sincronização de Tier para Rolagens do Esvanecer.
- **Added:** Mecânica de **Refocus (Descanso Curto)** para restaurar $\mathbf{E_{cur}}$.
- **Added:** Ação de emergência **Centelha Final** ($\mathbf{E_{cur}=0\%}$).

---

## [v0.8] — 2025-11-15 (Migração SPA & Estabilização)
**Status:** Arquitetura Estabilizada
- **Added:** Implementação da arquitetura **Single Page Application (SPA)**.
- **Added:** Integração completa da **Calculadora de Dano** na secção de Referência GM.
- **Fixed:** Correções críticas no *launcher* Python e lógica de localização.

---

## [v0.7] — 2025-11-14 (Letalidade de Precisão)
**Status:** Regras Base Finalizadas
- **Changed:** Reestruturação completa da progressão e combate.
- **Added:** **Erosão Inicial ($\mathbf{1\text{d}10}$)** na criação de personagem.
- **Added:** **Limite Máximo ($\mathbf{50\%}$)** para $\mathbf{E_{max}}$.
- **Changed:** Tabela de Tier de Proficiência alterada para **Progressão Uniforme ($\mathbf{1\text{d}10}$ por Tier)**.
- **Added:** Fórmula de Dano Aditiva e Multiplicador de Vantagem de Tier ($\mathbf{M_{DTA}}$).
- **Added:** Regra de Pares de Essência Motor/Qualidade.

---

## [v0.5] — 2025-10-27 (Rolagens de Ataque & Combate)
**Status:** Pronto para Teste Alpha
- **Changed:** O sistema de Resolução de Ação passa a ser por **Rolagens Contestadas**.
- **Added:** Tiers de Proficiência e Mapeamento de Dados.
- **Added:** Sistema de Resultados Críticos e Mitigação de Proficiência.

---

## [v0.4] — 2025-10-26 (Ciclo de Progresso Final)
**Status:** Pronto para Teste Alpha
- **Removed:** Removidas regras obsoletas de Cicatrização.
- **Changed:** Alterada a regra de progressão para a **Rolagem do Esvanecer** (Waning Roll).
- **Changed:** A Escolha de Proficiência rola $\mathbf{4\text{d}6}$ em troca de **$\mathbf{2\text{d}10}$ Dados de Proficiência ($\mathbf{D_{prof}}$)**.
- **Fixed:** Corrigido o título do jogo para **Nárëquenta — Contos do Declínio**.

---

## [v0.3] — 2025-10-26 (Refinamento do Escopo de Atrição)
**Status:** Prontidão para Teste Alpha
- **Removed:** Removido o custo de Atrição ($\mathbf{E_{cur}}$) para a maioria das ações fora de combate.
- **Added:** Adicionada regra de Custo Fixo de **$\mathbf{2\%}$** para situações de stress extremo fora de combate.
- **Added:** Adicionada **Penalidade Simétrica ($\mathbf{10}$)** para NPCs.

---

## [v0.2] — 2025-10-26 (Estrutura de Design)
**Status:** Prontidão para Teste Alpha
- **Changed:** Alterada a nomenclatura das Facetas para **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
- **Added:** Adicionada a separação crítica entre **Essência Máxima ($\mathbf{E_{max}}$)** e **Essência Atual ($\mathbf{E_{cur}}$)**.
- **Added:** Adicionada a **Escala Minguante**, onde $\mathbf{E_{max}}$ baixo concede bónus de Eficiência.
- **Added:** Adicionada Resolução de Ação por Rolagem Híbrida e sistema de Dano Mitigado por $\mathbf{E_{max}}$.
- **Added:** Adicionado suporte Multilíngue (PT-PT / EN-US) e lógica de automação da ficha.

---

## [v0.1] — 2025-10-25 (Desenvolvimento Privado)
**Status:** Prova de Origem
- **Added:** Estabelecido o mecanismo principal de auto-atrito: Ações consomem percentagens da Faceta.
- **Added:** Definido o sistema opcional de "Cicatrização" que reduz o valor máximo em troca de eficiência.
- **Added:** Definidas cinco Facetas do Eu: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
- **Added:** Adicionada Fase de Recuperação e regra de Fim de Jogo.

***

🧾 Chave de Versão

|**Tipo**|**Significado**|
|---|---|
|**Added**|Nova funcionalidade ou mecânica|
|**Changed**|Regra ajustada ou reequilibrada|
|**Removed**|Mecânica ou ficheiro removido|
|**Fixed**|Correção ou erro tipográfico|

---
🪶 Créditos

Design & Escrita — Serelith Varn
Desenvolvimento de Sistema & Documentação — GPT-5 (Liora Vex Framework)

“Somos lembrados pela forma elegante como nos desvanecemos.”

---
© 2025 Serelith Varn — Nárëquenta: Contos do Declínio.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Ver [LICENSE.md](license.md).