# 📜 Nárëquenta Core Rules v0.8 (Tier Advantage Supplement)

## 1. What This Game Is 🧭

Nárëquenta is a TTRPG where heroes begin near their peak and end spent. Characters start defined by their initial **Erosion**. They do not gain levels. They are remembered for how beautifully they burn out. You are not trying to survive forever. You are deciding what parts of you are worth spending before you're gone.

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

- A **Current Value ($\mathbf{E_{cur}}$)** (how much of that part of you is still usable right now).
    
- A **Maximum Value ($\mathbf{E_{max}}$)** (the ceiling it can be restored to).
    
- **Limit:** $\mathbf{E_{max}}$ can never drop below **$50\%$**.
    

### Initial Erosion

At character creation, **Initial Erosion** is applied:

- For each of the five Essences 1, you **choose** which ones you want to roll for, subjecting them to the initial loss.
    
- Roll $\mathbf{1d10}$ for each Essence.
    
- This value is subtracted from **$100\%$**.
    
- The result sets both the initial **Current Value ($\mathbf{E_{cur}}$)** and **Maximum Value ($\mathbf{E_{max}}$)** for that Essence.

---

## 3. Acting in the World (Action Resolution: Precision Lethality) 🎯

Actions are resolved as **Contested Rolls**. Only the Attacker utilizes $\mathbf{D_{prof}}$ for offensive output.

### Action Resolution Flow

- The success threshold is defined as:
    
    $$\mathbf{d100 \le \mathbf{E_{cur}}} \text{}$$
    
    The roll of a one-hundred sided die must be less than or equal to the Current Value of the Essence.
    
- **Attacker Rolls:** A rolls $\mathbf{d100}$ and their **Proficiency Dice ($\mathbf{D_{prof}}$)**. The result is $\mathbf{R_{prof}}$.
    
- **Attacker Mitigates:** A **subtracts the $\mathbf{R_{prof}}$ from the $\mathbf{d100}$ roll** (Error Mitigation). If the resulting roll is $\le$ the Attacker's $\mathbf{E_{cur}}$, the attack hits.
    
- **Defender Rolls:** D rolls $\mathbf{d100 \le \mathbf{E_{cur}}}$ to determine the **Defender's Margin ($\mathbf{D_{Margin}}$)** (Sec. 6).
    

### Attrition Cost

Cost is applied to the **Motor Essence ($\mathbf{E_{P}}$)** and **Quality Essence ($\mathbf{E_{S}}$)**.

- $\mathbf{E_{P}}$ Loss (Motor):
    
    $$\mathbf{D_{Loss} = \max \left(0, (7-R_{prof}) \right)} \text{}$$
    
    The loss is the maximum value between zero and the result of seven minus the Attacker's Proficiency Roll ($\mathbf{R_{prof}}$).
    
    - This loss pays the mitigated cost.
        

| Scenario                        | $\mathbf{R_{prof}}$ Example | Calculation                                   | Resulting $\mathbf{E_{P}}$ Loss |
| :------------------------------ | :-------------------------- | :-------------------------------------------- | :-----------------------------: |
| **High Loss** (Low Skill)       | **3** (e.g., Tier I roll)   | $\max(0, (7 - 3)) = 4$                        | **$4\%$**                       |
| **Mitigated Loss** (High Skill) | **18** (e.g., Tier IV roll) | $\max(0, (7 - 18)) = 0$<br>$\max(0, -11) = 0$ | **$0\%$**                       |

* **$\mathbf{E_{S}}$ Loss (Quality):** $1\%$ (Pays a minor fixed cost).
---

## 4. Refinement Cycle (The Waning Roll) 🌘

Refinement and Decay occur at the conclusion of every major milestone. The Proficiency Tier is determined by the total $\mathbf{E_{max}}$ loss.

### 4.1. The Proficiency Choice & Waning Roll

- Non-Chosen Essences:
    
    $$\mathbf{2d6} \text{}$$
    
    Roll two six-sided dice, and the result is permanently subtracted from $\mathbf{E_{max}}$.
    
- Chosen Essence (Focus):
    
    $$\mathbf{4d6} \text{}$$
    
    Roll four six-sided dice, and the result is permanently subtracted from $\mathbf{E_{max}}$, granting an increase in the $\mathbf{D_{prof}}$ Pool.
    

### 4.2. Using Proficiency (Uniform Tier System)

The $\mathbf{D_{prof}}$ gained is converted into a pool of:

$$\mathbf{1d10} \text{ per Tier}$$

One ten-sided die per Proficiency Tier (max $\mathbf{5d10}$ at Tier V).

---
## 5. Damage & Health (Tier-Neutral Lethality) 💥

All characters have a base of $100$ HP.

### Damage Formula

Damage is calculated using the Attacker's Full Potential Margin ($\mathbf{A_{FP}}$) and modified by the Defender's Tier Advantage ($\mathbf{M_{DTA}}$).

$$\mathbf{D_{Final}} = \max \left(0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}$$

The Final Damage is the maximum value between zero and the sum of the Full Potential Margin, minus the Defender's Average Mitigation, plus the Defender's Margin, plus the Attacker's Proficiency Roll, all multiplied by the Defensive Tier Advantage Multiplier.

| **Component** | **Formula** | **Transcription** |
| :--- | :--- | :--- |
| **$\mathbf{A_{FP}}$ (Full Potential Margin)** | $\mathbf{100 - (d100-R_{prof})}$ | One hundred minus the result of the $\mathbf{d100}$ roll minus the Proficiency Roll ($\mathbf{R_{prof}}$). |
| **$\mathbf{D_{Margin}}$ (Defender Margin)** | $\mathbf{d100_D-D_{Ecur}}$ | The Defender's $\mathbf{d100}$ roll minus the Defender's Current Essence ($\mathbf{E_{cur}}$). |

---

### Numerical Examples for Damage Components

To calculate $\mathbf{D_{Final}}$, we use the following fixed scenario values:

* **Attacker $\mathbf{R_{prof}}$ (Additive Damage):** **15** (Result of $3\text{d}10$).
* **Attacker $\mathbf{d100}$ Roll:** **50**.
* **Defender Tier:** III.
* **Defender $\mathbf{\bar{M}_{Defense}}$ (Average Mitigation):** **16.5**.
* **Defender $\mathbf{E_{cur}}$:** **70%**.
* **Defender $\mathbf{d100_D}$ Roll:** **80**.
* **$\mathbf{M_{DTA}}$:** **1.0** (Assuming TIII Attacker vs. TIII Defender, where there is no Tier Advantage).

#### A. Attacker's Full Potential Margin ($\mathbf{A_{FP}}$)

This value represents the Attacker's inherent power based on how well they mitigated their own $\mathbf{d100}$ roll.

$$\mathbf{A_{FP}} = \mathbf{100 - (50 - 15)}$$
$$\mathbf{A_{FP}} = 100 - 35 = \mathbf{65}$$
* **Interpretation:** The Attacker hits with a Full Potential Margin of **65**.

#### B. Defender's Margin ($\mathbf{D_{Margin}}$)

This value determines if the Defender successfully defended ($\mathbf{D_{Margin}}$ is negative) or failed to defend ($\mathbf{D_{Margin}}$ is positive).

$$\mathbf{D_{Margin}} = \mathbf{80 - 70}$$
$$\mathbf{D_{Margin}} = \mathbf{+10}$$
* **Interpretation:** The Defender failed their roll ($80 > 70$), resulting in a positive Margin of **+10**, which increases the damage taken.

#### C. Calculating Final Damage ($\mathbf{D_{Final}}$)

We plug all results into the main formula:

$$\mathbf{D_{Final}} = \max \left(0, (65 - 16.5 + 10 + 15) \right) \times 1.0$$
$$\mathbf{D_{Final}} = \max \left(0, (73.5) \right) \times 1.0$$
$$\mathbf{D_{Final}} = \mathbf{73} \text{ HP (Rounded Down)}$$
* **Interpretation:** The base damage was 73 HP. The Defender's failure ($\mathbf{D_{Margin}}=+10$) increased the damage, but the Defender's innate skill ($\mathbf{\bar{M}_{Defense}}=16.5$) successfully reduced it from the Attacker's full potential.

---

## 6. Proficiency Tiers and $\mathbf{M_{DTA}}$ Multipliers 🛡️

### Proficiency Tiers

The Proficiency Tier is determined by the current $\mathbf{E_{max}}$ of the Essence. $\mathbf{\bar{M}_{Defense}}$ is the Defender's Average $\mathbf{R_{prof}}$.

| $\mathbf{E_{max}}$ Loss | Remaining $\mathbf{E_{max}}$ (%) | Tier | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Defense Mitigation) | **Action Surges (AS)** |
| :--: | :---:| :--: | :--: | :--: | :--: |
| $0-9\%$ | $100-91\%$ | **0** | None | $0.0$ | **0** |
| $10-19\%$ | $90-81\%$ | **I** | $\mathbf{1d10}$ | $5.5$ | **1** |
| $20-29\%$ | $80-71\%$ | **II** | $\mathbf{2d10}$ | $11.0$ | **2** |
| $30-39\%$ | $70-61\%$ | **III** | $\mathbf{3d10}$ | $16.5$ | **3** |
| $40-49\%$ | $60-51\%$ | **IV** | $\mathbf{4d10}$ | $22.0$ | **4** |
| $\mathbf{50\%}$ | $\mathbf{50\%}$ | **V (Pinnacle)** | $\mathbf{5d10}$ | $\mathbf{27.5}$ | **5** |

### Tier Advantage Multiplier ($\mathbf{M_{DTA}}$) - Supplement v0.8

The $\mathbf{M_{DTA}}$ multiplier now covers both damage reduction (Defense Advantage) and damage increase (Offense Advantage) based on the Tier difference.

#### Defensive Tier Advantage (Tier I Attacker Reference)

| **Attacker Tier** | **Defender Tier** | **Tier Difference (ΔT)** |  **MDTA​ (Reduction)**   |
| :---------------: | :---------------: | :----------------------: | :----------------------: |
|       **I**       |       **I**       |       $\mathbf{0}$       |     $\mathbf{1.00}$      |
|       **I**       |      **II**       |      $\mathbf{+1}$       |     $\mathbf{0.75}$      |
|       **I**       |      **III**      |      $\mathbf{+2}$       |     $\mathbf{0.50}$      |
|       **I**       |      **IV**       |      $\mathbf{+3}$       |     $\mathbf{0.25}$      |
|       **I**       |       **V**       |      $\mathbf{+4}$       | $\mathbf{0.25}$ (Capped) |

#### Offensive Tier Advantage (Tier V Attacker Reference)

|**Attacker Tier**|**Defender Tier**|**Tier Difference (ΔT)**|**MDTA​ (Offense Bonus)**|
|:---:|:---:|:---:|:---:|
|**V**|**V**|$\mathbf{0}$|$\mathbf{1.00}$|
|**V**|**IV**|$\mathbf{-1}$|$\mathbf{1.25}$|
|**V**|**III**|$\mathbf{-2}$|$\mathbf{1.50}$|
|**V**|**II**|$\mathbf{-3}$|$\mathbf{1.75}$|
|**V**|**I**|$\mathbf{-4}$|$\mathbf{2.00}$|
## ⚔️ Complete $\mathbf{M_{DTA}}$ Grid (Attacker vs. Defender)

The $\mathbf{M_{DTA}}$ is determined by the difference in Tiers ($\Delta T = T_{Defender} - T_{Attacker}$). Values below $1.00$ are **Defensive Reductions**, and values above $1.00$ are **Offensive Bonuses**.

| Attacker Tier $\downarrow$ vs. Defender Tier $\rightarrow$ | **I** ($\mathbf{E_{max}} \mathbf{90-81\%}$) | **II** ($\mathbf{E_{max}} \mathbf{80-71\%}$) | **III** ($\mathbf{E_{max}} \mathbf{70-61\%}$) | **IV** ($\mathbf{E_{max}} \mathbf{60-51\%}$) | **V** ($\mathbf{E_{max}} \mathbf{50\%}$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **I** | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ | $\mathbf{0.25}$ (Capped) |
| **II** | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ |
| **III** | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ | $\mathbf{0.50}$ |
| **IV** | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) | $\mathbf{0.75}$ |
| **V** | $\mathbf{2.00}$ (Max Bonus) | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutral) |

This comprehensive $\mathbf{M_{DTA}}$ table provides the multiplier for any Attacker vs. Defender Tier combination based on the established progressive rule.

## ⚔️ Numerical Examples for $\mathbf{M_{DTA}}$

We will use the fixed damage component from the previous example:
* **Base Damage Sum (Before $\mathbf{M_{DTA}}$):** $A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof} = 36 \text{ (Assumed for clean example)}$.

| Case   | Scenario                                                         | $\Delta T$ ($T_{Def} - T_{Att}$) | $\mathbf{M_{DTA}}$ (Multiplier) | $\mathbf{D_{Final}}$ Calculation | $\mathbf{D_{Final}}$ Result |
| :----- | :--------------------------------------------------------------- | :------------------------------- | :------------------------------ | :------------------------------- | :-------------------------- |
| **1.** | **Max Offensive Bonus** (Level 5 PC attacks Level 1 Goblin)      | $\mathbf{-4}$                    | $\mathbf{2.00}$                 | $36 \times 2.00$                 | **72 HP**                   |
| **2.** | **Neutral Combat** (Level 2 Attacker attacks Level 2 Defender)   | $\mathbf{0}$                     | $\mathbf{1.00}$                 | $36 \times 1.00$                 | **36 HP**                   |
| **3.** | **Max Defensive Mitigation** (Level 1 Goblin attacks Level 4 PC) | $\mathbf{+3}$                    | $\mathbf{0.25}$                 | $36 \times 0.25$                 | **9 HP**                    |

---
## 7. Recovery and Endgame ⏳

* **Recovery Phase** restores the $\mathbf{E_{cur}}$ up to the current $\mathbf{E_{max}}$ value.
* **Action Surge Progression:** The AS pool (granting extra attacks per Recovery cycle) scales with Tier, compensating for the low $\mathbf{E_{max}}$ ceiling. (Tier V grants 5 AS).
* **Survival:** By late play, your Efficiencies and $\mathbf{D_{prof}}$ make you incredibly lethal, despite having a low $\mathbf{E_{cur}}$ ceiling.

---
## 8. End of the Game

In the end, you retire hollowed and legendary.

The campaign is the record of **how you chose to fade**.

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
