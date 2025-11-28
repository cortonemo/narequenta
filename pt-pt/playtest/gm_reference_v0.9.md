# Referência do Mestre v0.9.6 (Letalidade de Precisão)

## I. FLUXO DA SESSÃO
1. **Briefing:** Estabelecer o que arriscam perder.
2. **Resolução de Ação:**
   - **Teste:** $\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalidade}})$.
   - **Atrição:** A ação queima $\mathbf{E_{cur}}$ com base no Peso do Item (Leve 10%, Med 15%, Pes 20%) menos $\lfloor R_{prof}/2 \rfloor$.
3. **Zonas de Tensão:** Garantir que os jogadores registam a sua penalidade de Zona atual.
   - **Pico (100-76%):** -0
   - **Minguante (75-51%):** -10
   - **Desvanecente (50-26%):** -20
   - **Vazio (25-0%):** -30.

## II. FÓRMULAS DE COMBATE
**O Piso de Dano:** O dano nunca desce abaixo de $\mathbf{R_{prof}}$ (antes do Multiplicador de Nível).

$$\mathbf{D_{Final}} = \max(\mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Def}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}})) \times \mathbf{M_{DTA}}$$

| Componente | Fórmula / Valor |
| :--- | :--- |
| **$\mathbf{A_{FP}}$** | $100 - (d100 - R_{prof})$ |
| **$\mathbf{D_{Margin}}$** | $Rolagem_{Def} - Defensor_{Ecur}$ |
| **$\mathbf{\bar{M}_{Def}}$** | $Defensor_{Nível} \times 5.5$ |

## III. MULTIPLICADOR DE VANTAGEM DE NÍVEL ($\mathbf{M_{DTA}}$)
Baseado em $\Delta T = T_{Defensor} - T_{Atacante}$.

| Atacante vs Defensor | Multiplicador |
| :--- | :--- |
| **Nível Igual** | **x 1.00** |
| **Defensor +1 Nível** | **x 0.75** |
| **Defensor +2 Níveis** | **x 0.50** |
| **Atacante +1 Nível** | **x 1.25** |
| **Atacante +2 Níveis** | **x 1.50** |

## IV. RECUPERAÇÃO (RENOVAÇÃO)
- **Descanso Longo:** Restaura $\mathbf{E_{cur}}$ para 100% (ou $\mathbf{E_{max}}$ atual). **Não** recupera $\mathbf{E_{max}}$ perdido.
- **Rolagem do Esvanecer:** Ocorre em marcos. $\mathbf{1d6}$ (Universal) ou $\mathbf{2d6}$ (Foco).

---
© 2025 Serelith Varn.


© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
