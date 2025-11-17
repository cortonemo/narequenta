#  ⚔️ Nárëquenta: Regras de Combate e Proficiência (v0.9)

Este documento detalha as mecânicas finais de **Letalidade de Precisão** e o uso de Proficiência em Nárëquenta, sincronizadas com o sistema de Mitigação de Degradação.

## 1. Níveis de Proficiência e Mapeamento de Dados

O **Nível de Proficiência** é determinado pela $\mathbf{E_{max}}$ atual da Essência.
A Proficiência é **Unificada** para $\mathbf{1\text{d}10}$ por Nível.

| Nível | Perda Total $E_{max}$ | $E_{max}$ Remanescente (%) | Dados de Proficiência ($\mathbf{D_{prof}}$) | Benefício Médio ($\bar{M}$) | **Ataques Súbitos (AS)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | $0-9\%$ | $100-91\%$ | Nenhum | $0.0$ | **0** |
| **I** | $10-19\%$ | $90-81\%$ | $\mathbf{1\text{d}10}$ | $5.5$ | **1** |
| **II** | $20-29\%$ | $80-71\%$ | $\mathbf{2\text{d}10}$ | $11.0$ | **2** |
| **III** | $30-39\%$ | $70-61\%$ | $\mathbf{3\text{d}10}$ | $16.5$ | **3** |
| **IV** | $40-49\%$ | $60-51\%$ | $\mathbf{4\text{d}10}$ | $22.0$ | **4** |
| **V (Pináculo)** | $\mathbf{50\%}$ | $\mathbf{50\%}$ | $\mathbf{5\text{d}10}$ | $\mathbf{27.5}$ | **5** |

## 2. Uso da Proficiência ($\mathbf{R_{prof}}$ Unificado)

O resultado da jogada $\mathbf{D_{prof}}$ ($\mathbf{R_{prof}}$) é usado para três efeitos simultâneos: Mitigação, Atrição e Dano Base.

### A. Mitigação de Erro (Jogadas Contestadas)

O Atacante rola a sua $\mathbf{D_{prof}}$ e **subtrai o $\mathbf{R_{prof}}$ da jogada de $\mathbf{d100}$**.
Este é o método para aumentar a hipótese de sucesso (Mitigação de Erro).

### B. Redução de Atrição (Custo de Energia)

O $\mathbf{R_{prof}}$ é usado para mitigar o custo de $\mathbf{E_{cur}}$ da Essência Motor ($\mathbf{E_{P}}$) e da Essência Qualidade ($\mathbf{E_{S}}$):

* **Perda $E_{P}$ (Motor):** $\mathbf{D_{Perda} = \max \left( 0, (7 - R_{prof}) \right)}$
* **Perda $E_{S}$ (Qualidade):** **$\mathbf{1\%}$**

### C. Dano Base Aditivo
O $\mathbf{R_{prof}}$ é adicionado ao cálculo final de dano como a base de poder (ver Secção 3).

### D. Ataques Especiais (Regra Opcional)
Os Jogadores podem sacrificar temporariamente $\mathbf{D_{prof}}$ da sua *reserva* para realizar ações melhoradas.
Personagens sem Proficiência não podem realizar estas ações melhoradas.

## 3. Fórmula de Dano Final (Letalidade de Precisão)

O Dano é Neutro em Nível na Ofensa e na Defesa, calculado por Margens e modificado pela Vantagem de Nível.

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$$

| Componente | Cálculo | Nota v0.9 |
| :--- | :--- | :--- |
| **$A_{FP}$ (Margem de Potencial Pleno)** | $100 - (d100 - R_{prof})$ | **Neutro em Nível** (Baseado em 100%, não no $E_{cur}$ do Atacante). |
| **$\bar{M}_{Defense}$** | $\bar{M}$ médio da $\mathbf{D_{prof}}$ do Defensor. | O Defensor reduz o dano devido à sua Proficiência. |
| **$D_{Margin}$ (Margem do Defensor)** | $d100_D - D_{Ecur}$ | Positiva em caso de falha, negativa em defesa bem-sucedida. |
| **$R_{prof}$ (Dano Aditivo)** | Resultado da jogada $\mathbf{D_{prof}}$ do Atacante. | Dano garantido e base ofensiva. |
| **$M_{DTA}$ (Vantagem de Nível)** | Multiplicador ($\times 0.75$ a $\times 2.00$) | Reduz o dano se o Defensor for de Nível superior, aumenta o dano se o Atacante for de Nível superior. |

## 4. Dano, Vida e Esgotamento de Energia

* Todos os personagens têm uma base de **100 PV**.
* A **Jogada de Dano Bónus** e o **Limite de Esgotamento de Energia** (Regras v0.5) são **REMOVIDOS**, pois $\mathbf{D_{Final}}$ e Atrição Mitigada (Secção 2) governam agora o ritmo do jogo.

---
© 2025 Serelith Varn — Nárëquenta: Contos do Minguante.
Licenciado para jogo não comercial e conteúdo de fãs sob a Licença Aberta Limitada Nárëquenta (v0.1). Ver [LICENSE.md](license.md).

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).