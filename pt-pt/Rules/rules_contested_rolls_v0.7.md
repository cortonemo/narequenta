# ⚔️ Nárëquenta: Regras de Combate e Proficiência (v0.7)

Este documento detalha as mecânicas finais de **Letalidade de Precisão** e o uso da Proficiência em Nárëquenta.

## 1. Tiers de Proficiência e Mapeamento de Dados

O **Tier de Proficiência** é determinado pela $\mathbf{E_{max}}$ atual da Essência. A proficiência é **Unificada** para $\mathbf{1\text{d}10}$ por Tier.

| Tier | Perda $E_{max}$ Total | $E_{max}$ Restante (%) | Dados de Proficiência ($\mathbf{D_{prof}}$) | Benefício Médio ($\bar{M}$) |
| :--- | :--- | :--- | :--- | :--- |
| **0** | $0-9\%$ | $100-91\%$ | Nenhum | $0.0$ |
| **I** | $10-19\%$ | $90-81\%$ | $\mathbf{1\text{d}10}$ | $5.5$ |
| **II** | $20-29\%$ | $80-71\%$ | $\mathbf{2\text{d}10}$ | $11.0$ |
| **III** | $30-39\%$ | $70-61\%$ | $\mathbf{3\text{d}10}$ | $16.5$ |
| **IV** | $40-49\%$ | $60-51\%$ | $\mathbf{4\text{d}10}$ | $22.0$ |
| **V (Pináculo)** | $\mathbf{50\%}$ | $\mathbf{50\%}$ | $\mathbf{5\text{d}10}$ | $\mathbf{27.5}$ |

## 2. Uso da Proficiência ($\mathbf{R_{prof}}$ Unificado)

O resultado da rolagem de $\mathbf{D_{prof}}$ ($\mathbf{R_{prof}}$) é usado para três efeitos simultâneos: Mitigação, Atrição e Dano Base.

### A. Mitigação de Erro (Rolagens Contestadas)

O Atacante rola os seus $\mathbf{D_{prof}}$ e **subtrai o $\mathbf{R_{prof}}$ da rolagem $\mathbf{d100}$**. Esta é a forma de aumentar a chance de sucesso (Mitigação de Erro).

### B. Redução de Atrição (Custo de Energia)

O $\mathbf{R_{prof}}$ é usado para mitigar o custo de $\mathbf{E_{cur}}$ das Essências Motor ($\mathbf{E_{P}}$) e Qualidade ($\mathbf{E_{S}}$):

- **$E_{P}$ Loss (Motor):** $\mathbf{D_{Loss} = \max \left( 0, (7 - R_{prof}) \right)}$
- **$E_{S}$ Loss (Qualidade):** **$1\%$**

### C. Dano Base Aditivo
O $\mathbf{R_{prof}}$ é adicionado ao cálculo final do dano como base de poder (consulte a Secção 3).

### D. Ataques Especiais (Regra Opcional)
Jogadores podem temporariamente sacrificar $\mathbf{D_{prof}}$ do seu *pool* para realizar ações aprimoradas. Personagens sem Proficiência não podem realizar estas ações aprimoradas.

## 3. Fórmula de Dano Final (Letalidade de Precisão)

O dano é Tier-Neutro na Ofensa e Defesa, calculado pelas Margens e modificado pela Vantagem de Nível.

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$$

| Componente | Cálculo | Nota v0.7 |
| :--- | :--- | :--- |
| **$A_{FP}$ (Margem Potencial Total)** | $100 - (d100 - R_{prof})$ | **Tier-Neutro** (Baseado no 100%, não no $E_{cur}$ do Atacante). |
| **$\bar{M}_{Defense}$** | Valor Médio $\bar{M}$ do $\mathbf{D_{prof}}$ do Defensor. | O Defensor reduz o dano devido à sua Proficiência. |
| **$D_{Margin}$ (Margem do Defensor)** | $d100_D - D_{Ecur}$ | Positivo no falhanço, negativo na defesa. |
| **$R_{prof}$ (Dano Aditivo)** | Resultado do $\mathbf{D_{prof}}$ do Atacante. | Dano garantido e base ofensiva. |
| **$M_{DTA}$ (Vantagem de Nível)** | Multiplicador ($\times 0.75$ a $\times 0.25$) | Reduz o dano se o Defensor for de Tier superior. |

## 4. Dano, Saúde e Desgaste de Energia

* Todas as personagens têm uma base de **100 HP**.
* **Dano Bónus de Rolagem** e **Teto de Desgaste de Energia por Dano** (Regras v0.5) são **REMOVIDOS**, pois a $\mathbf{D_{Final}}$ e a Atrição Mitigada (Secção 2) gerem agora o ritmo de jogo.

---
© 2025 Serelith Varn — Nárëquenta: Contos do Esvanecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte [LICENSE.md](license.md).

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.