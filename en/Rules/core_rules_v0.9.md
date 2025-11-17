# 📜 Nárëquenta Core Rules v0.9 (Decay Mitigation)

## 1. What This Game Is 🧭

Nárëquenta is a TTRPG where heroes begin near their peak and end spent. Progression is the **defining of character through loss**. Power is a finite resource. **Proficiency Compensates for Decline**.

---

## 2. Facets of the Self (Essences) ✨

Each character is defined by five Essences. Each Essence starts at **$100\%$**, subject to Initial Erosion.

- **VITALIS** — body, endurance, force, presence
- **MOTUS** — movement, finesse, agility, grace
- **SENSUS** — awareness, instinct, focus, perception
- **VERBUM** — intellect, logic, structure, speech
- **ANIMA** — conviction, will, faith, sacrifice

### Essence Values

Each Facet has:

- A **Current Value ($\mathbf{E_{cur}}$)** (usable energy).
- A **Maximum Value ($\mathbf{E_{max}}$)** (permanent limit).
- **Limit:** $\mathbf{E_{max}}$ can never drop below **$50\%$** (Hard Floor).

### Initial Erosion (v0.9 Update)

At character creation, **Initial Erosion** is applied:

- For each of the five Essences, roll $\mathbf{1d10}$. This value is subtracted from **$100\%$**, setting the initial $\mathbf{E_{cur}}$ and $\mathbf{E_{max}}$.
- **Tier I Guarantee:** The player may designate one Essence to have its $\mathbf{E_{max}}$ set precisely to **$90\%$** after the roll, guaranteeing **Tier I** status and $\mathbf{1d10}$ $\mathbf{D_{prof}}$ immediately.

---

## 3. Acting in the World (Action Resolution: Precision Lethality) 🎯

Actions are resolved as **Contested Rolls**.

### Action Resolution Flow

- The success threshold is defined as: $\mathbf{d100 \le \mathbf{E_{cur}}}$.
- **Attacker Mitigates:** The Attacker subtracts their Proficiency Roll ($\mathbf{R_{prof}}$) from the $\mathbf{d100}$ roll (Error Mitigation).

### Attrition Cost

Cost is applied to the **Motor Essence ($\mathbf{E_{P}}$)** and **Quality Essence ($\mathbf{E_{S}}$)**.

- **$\mathbf{E_{P}}$ Loss (Motor):** $\mathbf{D_{Loss} = \max \left(0, (7-R_{prof}) \right)}$.
- **$\mathbf{E_{S}}$ Loss (Quality):** $1\%$ (Fixed Cost).

---

## 4. Refinement Cycle (The Waning Roll) 🌘 (v0.9 Decay Mitigation)

Refinement and Decay occur at the conclusion of every major milestone. The Proficiency Tier is determined by the total $\mathbf{E_{max}}$ loss.

### 4.1. The Proficiency Choice & Waning Roll

- **Universal Decay (Non-Chosen Essences):**
    $$\mathbf{1d6} \text{}$$
    Roll one six-sided die, and the result is permanently subtracted from $\mathbf{E_{max}}$ (down to the $50\%$ Hard Floor).
- **Refinement Focus (Chosen Essence):**
    $$\mathbf{2d6} \text{}$$
    Roll two six-sided dice, and the result is permanently subtracted from $\mathbf{E_{max}}$, granting an increase in the $\mathbf{D_{prof}}$ Pool (Tier Advancement).

### 4.2. Using Proficiency (Uniform Tier System)

The $\mathbf{D_{prof}}$ pool is defined as:
$$\mathbf{1d10} \text{ per Tier}$$

---
## 5. Damage & Health (Tier-Neutral Lethality) 💥

All characters have a base of $100$ HP.

### Damage Formula

$$\mathbf{D_{Final}} = \max \left(0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}$$

| **Component** | **Formula** |
| :--- | :--- |
| **$\mathbf{A_{FP}}$ (Full Potential Margin)** | $\mathbf{100 - (d100-R_{prof})}$ |
| **$\mathbf{D_{Margin}}$ (Defender Margin)** | $\mathbf{d100_D-D_{Ecur}}$ |

---

## 6. Proficiency Tiers and $\mathbf{M_{DTA}}$ Multipliers 🛡️

### Proficiency Tiers (v0.9 AS Correction)

The Proficiency Tier is determined by the $\mathbf{E_{max}}$ of the Essence.

| $\mathbf{E_{max}}$ Loss | Remaining $\mathbf{E_{max}}$ (%) |       Tier       | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Defense Mitigation) | **Action Surges (AS)** |
| :---------------------: | :------------------------------: | :--------------: | :-----------------: | :-------------------------------------: | :--------------------: |
|         $0-9\%$         |            $100-91\%$            |      **0**       |        None         |                  $0.0$                  |         **0**          |
|        $10-19\%$        |            $90-81\%$             |      **I**       |   $\mathbf{1d10}$   |                  $5.5$                  |         **1**          |
|        $20-29\%$        |            $80-71\%$             |      **II**      |   $\mathbf{2d10}$   |                 $11.0$                  |         **2**          |
|        $30-39\%$        |            $70-61\%$             |     **III**      |   $\mathbf{3d10}$   |                 $16.5$                  |         **3**          |
|        $40-49\%$        |            $60-51\%$             |      **IV**      |   $\mathbf{4d10}$   |                 $22.0$                  |         **4**          |
|     $\mathbf{50\%}$     |         $\mathbf{50\%}$          | **V (Pinnacle)** |   $\mathbf{5d10}$   |             $\mathbf{27.5}$             |        5 (Max)         |

### Tier Advantage Multiplier ($\mathbf{M_{DTA}}$)

| Attacker Tier $\downarrow$ vs. Defender Tier $\rightarrow$ | **I** | **II** | **III** | **IV** | **V** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **I** | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ | $\mathbf{0.25}$ |
| **II** | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ |
| **III** | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ |
| **IV** | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ |
| **V** | $\mathbf{2.00}$ (Max Bonus) | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) |

---

## 7. Recovery and Endgame ⏳

* **Recovery Phase** restores the $\mathbf{E_{cur}}$ up to the current $\mathbf{E_{max}}$ value.
* **Action Surge Progression:** The AS pool scales with Tier, up to 5 AS.
* **Endgame:** The campaign is the record of **how you chose to fade**.

---
## 8. End of the Game

In the end, you retire hollowed and legendary.

The campaign is the record of **how you chose to fade**.

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).