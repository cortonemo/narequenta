## ⚔️ Nárëquenta: Combat and Proficiency Rules (v0.9)

This document details the final mechanics of **Precision Lethality** and the use of Proficiency in Nárëquenta, synchronized with the Decay Mitigation system.

## 1. Proficiency Tiers and Dice Mapping

The **Proficiency Tier** is determined by the current $\mathbf{E_{max}}$ of the Essence.
Proficiency is **Unified** to $\mathbf{1\text{d}10}$ per Tier.

| Tier | Total $E_{max}$ Loss | Remaining $E_{max}$ (%) | Proficiency Dice ($\mathbf{D_{prof}}$) | Average Benefit ($\bar{M}$) | **Action Surges (AS)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | $0-9\%$ | $100-91\%$ | None | $0.0$ | **0** |
| **I** | $10-19\%$ | $90-81\%$ | $\mathbf{1\text{d}10}$ | $5.5$ | **1** |
| **II** | $20-29\%$ | $80-71\%$ | $\mathbf{2\text{d}10}$ | $11.0$ | **2** |
| **III** | $30-39\%$ | $70-61\%$ | $\mathbf{3\text{d}10}$ | $16.5$ | **3** |
| **IV** | $40-49\%$ | $60-51\%$ | $\mathbf{4\text{d}10}$ | $22.0$ | **4** |
| **V (Pinnacle)** | $\mathbf{50\%}$ | $\mathbf{50\%}$ | $\mathbf{5\text{d}10}$ | $\mathbf{27.5}$ | **5** |

## 2. Use of Proficiency ($\mathbf{R_{prof}}$ Unified)

The result of the $\mathbf{D_{prof}}$ roll ($\mathbf{R_{prof}}$) is used for three simultaneous effects: Mitigation, Attrition, and Base Damage.

### A. Error Mitigation (Contested Rolls)

The Attacker rolls their $\mathbf{D_{prof}}$ and **subtracts the $\mathbf{R_{prof}}$ from the $\mathbf{d100}$ roll**.
This is the method for increasing the chance of success (Error Mitigation).

### B. Attrition Reduction (Energy Cost)

The $\mathbf{R_{prof}}$ is used to mitigate the $\mathbf{E_{cur}}$ cost of the Motor Essence ($\mathbf{E_{P}}$) and Quality Essence ($\mathbf{E_{S}}$):

- **$E_{P}$ Loss (Motor):** $\mathbf{D_{Loss} = \max \left( 0, (7 - R_{prof}) \right)}$
- **$E_{S}$ Loss (Quality):** **$1\%$**

### C. Additive Base Damage
The $\mathbf{R_{prof}}$ is added to the final damage calculation as the base of power (see Section 3).

### D. Special Attacks (Optional Rule)
Players may temporarily sacrifice $\mathbf{D_{prof}}$ from their *pool* to perform enhanced actions.
Characters without Proficiency cannot perform these enhanced actions.

## 3. Final Damage Formula (Precision Lethality)

Damage is Tier-Neutral in Offense and Defense, calculated by Margins and modified by Tier Advantage.

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$$

| Component | Calculation | v0.9 Note |
| :--- | :--- | :--- |
| **$A_{FP}$ (Full Potential Margin)** | $100 - (d100 - R_{prof})$ | **Tier-Neutral** (Based on 100%, not Attacker's $E_{cur}$). |
| **$\bar{M}_{Defense}$** | Average $\bar{M}$ of Defender's $\mathbf{D_{prof}}$. | Defender reduces damage due to their Proficiency. |
| **$D_{Margin}$ (Defender Margin)** | $d100_D - D_{Ecur}$ | Positive on failure, negative on successful defense. |
| **$R_{prof}$ (Additive Damage)** | Result of Attacker's $\mathbf{D_{prof}}$ roll. | Guaranteed damage and offensive base. |
| **$M_{DTA}$ (Tier Advantage)** | Multiplier ($\times 0.75$ to $\times 2.00$) | Reduces damage if Defender is higher Tier, increases damage if Attacker is higher Tier. |

## 4. Damage, Health, and Energy Depletion

* All characters have a base of **100 HP**.
* **Bonus Damage Roll** and **Energy Depletion Cap** (v0.5 Rules) are **REMOVED**, as $\mathbf{D_{Final}}$ and Mitigated Attrition (Section 2) now govern the pace of the game.

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).
