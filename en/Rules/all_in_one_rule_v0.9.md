

## ⚔️ Nárëquenta System Reference: Precision Lethality (v0.9)


---

### I. Index of Variables (Sigla)

This index translates the mathematical symbols (sigla) used in the formulas into their full English equivalents and describes their role in the game.

| Symbol | Definition in English | System Role |
| :--- | :--- | :--- |
| $\mathbf{E_{max}}$ | **Maximum Essence** (Soul's Peak) | Permanent potential limit. Determines the Proficiency Tier (Hard Floor **50%**). |
| $\mathbf{E_{cur}}$ | **Current Essence** (Active Vigor) | Usable energy. Defines the success threshold. |
| $\mathbf{D_{prof}}$ | **Proficiency Dice** (Waning Yield Pool) | The pool of $\mathbf{1d10}$ dice per Tier. |
| $\mathbf{R_{prof}}$ | **Proficiency Roll Result** (Waning Yield Result) | The total sum rolled on the Attacker's $\mathbf{D_{prof}}$ pool. Used for Error Mitigation and Damage Base. |
| $\mathbf{E_{P}}$ | **Motor Essence** (Primary Essence) | The Essence driving the action (takes variable loss). |
| $\mathbf{E_{S}}$ | **Quality Essence** (Secondary Essence) | The Essence defining the quality/style (takes fixed loss). |
| $\mathbf{D_{Loss}}$ | **Motor Essence Loss** | The calculated reduction to the $\mathbf{E_{cur}}$ of the Motor Essence ($\mathbf{E_{P}}$). |
| $\mathbf{d100}$ | **Contested Roll Die** | The roll used for the success check. |
| $\mathbf{A_{FP}}$ | **Full Potential Margin** (Attacker Potential) | The effective success margin relative to maximum power ($\mathbf{100}$). |
| $\mathbf{\bar{M}_{Defense}}$ | **Average Mitigation** (Waning Yield Average) | The Defender's passive damage reduction, equal to the average of their $\mathbf{D_{prof}}$ pool. |
| $\mathbf{D_{Margin}}$ | **Defender Margin** (Defense Vulnerability) | Measures how much the Defender failed their defense roll relative to their $\mathbf{E_{cur}}$. |
| $\mathbf{d100_D}$ | **Defender's Defense Roll** | The roll made by the Defender to resist damage. |
| $\mathbf{M_{DTA}}$ | **Tier Advantage Multiplier** (Damage Scaling) | A multiplier based on the difference between Attacker Tier and Defender Tier. |
| $\mathbf{D_{Final}}$ | **Final Damage** (Lethality Output) | The final amount of HP lost by the Defender. |

---

### II. Action Resolution and Attrition

Actions succeed if the **Contested Roll Die ($\mathbf{d100}$)** roll, reduced by the **Proficiency Roll Result ($\mathbf{R_{prof}}$)**, is less than or equal to the Essence's **Current Essence ($\mathbf{E_{cur}}$)**.

#### A. Motor Essence Attrition Cost ($\mathbf{E_{P}}$)

$$\mathbf{D_{Loss} = \max \left(0, (7-R_{prof}) \right)} \text{}$$

**Explanation:** The **Motor Essence Loss ($\mathbf{D_{Loss}}$)**, which reduces the **Current Essence ($\mathbf{E_{cur}}$)**, is calculated by taking the value $\mathbf{7}$ and subtracting the **Proficiency Roll Result ($\mathbf{R_{prof}}$)**. This result is capped at $\mathbf{0}$ (cannot be negative). A higher $\mathbf{R_{prof}}$ roll efficiently mitigates the $\mathbf{E_{cur}}$ loss, reflecting skilled execution.

#### B. Quality Essence Attrition Cost ($\mathbf{E_{S}}$)

The **Quality Essence ($\mathbf{E_{S}}$)** loss is a fixed:
$$\mathbf{1\%} \text{ (Fixed Cost)} \text{}$$

**Explanation:** The loss to the **Quality Essence ($\mathbf{E_{S}}$)** is a non-mitigable $\mathbf{1\%}$ fixed cost to its **Current Essence ($\mathbf{E_{cur}}$)**. This represents the inherent strain on the quality/finesse aspect of the action, regardless of skill.

---

### III. Refinement Cycle Formulas (The Waning Roll)

The Waning Roll permanently reduces the **Maximum Essence ($\mathbf{E_{max}}$)** (Soul's Peak) to advance the character's Proficiency Tier.

#### A. Universal Decay (Non-Chosen Essences)

$$\mathbf{1d6} \text{}$$

**Explanation:** Non-Chosen Essences lose $\mathbf{1d6}$ permanently from their **Maximum Essence ($\mathbf{E_{max}}$)** (Soul's Peak), down to the $\mathbf{50\%}$ Hard Floor.

#### B. Refinement Focus (Chosen Essence)

$$\mathbf{2d6} \text{}$$

**Explanation:** The Chosen Essence (Refinement Focus) loses $\mathbf{2d6}$ permanently from its **Maximum Essence ($\mathbf{E_{max}}$)** (Soul's Peak), granting an increase in the **Proficiency Dice ($\mathbf{D_{prof}}$)** pool (Tier Advancement).

---

### IV. Final Damage Formula (Precision Lethality)

This formula determines the **Final Damage ($\mathbf{D_{Final}}$)** (HP loss) dealt to the Defender. All characters have a base of $\mathbf{100}$ HP.

$$\mathbf{D_{Final}} = \max \left(0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}$$

**Explanation:** The **Final Damage ($\mathbf{D_{Final}}$)** is the product of two main terms:
1.  **The Base Damage Margin:** This is calculated by taking the **Full Potential Margin ($\mathbf{A_{FP}}$)**, subtracting the Defender's **Average Mitigation ($\mathbf{\bar{M}_{Defense}}$)**, adding the **Defender Margin ($\mathbf{D_{Margin}}$)** (which increases damage on defense failure), and adding the **Proficiency Roll Result ($\mathbf{R_{prof}}$)** (guaranteed damage base). This result is capped at $\mathbf{0}$.
2.  **The Tier Scaling Multiplier:** This base margin is then multiplied by the **Tier Advantage Multiplier ($\mathbf{M_{DTA}}$)**, which scales the final damage based on the difference in Tiers between Attacker and Defender.

#### Component Breakdowns:

1.  **Full Potential Margin ($\mathbf{A_{FP}}$)**:
    $$\mathbf{A_{FP}} = \mathbf{100 - (d100-R_{prof})} \text{}$$

    **Explanation:** This component calculates the Attacker's raw power relative to a perfect $\mathbf{100}$ base. It takes the modified **Contested Roll Die ($\mathbf{d100}$)** ($\mathbf{d100} - \mathbf{R_{prof}}$) and subtracts it from $\mathbf{100}$. A lower modified $\mathbf{d100}$ roll yields a higher $\mathbf{A_{FP}}$, indicating effective offense.

2.  **Defender Margin ($\mathbf{D_{Margin}}$)**:
    $$\mathbf{D_{Margin}} = \mathbf{d100_D-D_{Ecur}} \text{}$$

    **Explanation:** This measures the Defender's vulnerability. It is the **Defender's Defense Roll ($\mathbf{d100_D}$)** minus their **Current Essence ($\mathbf{D_{Ecur}}$)** (Active Vigor). A positive $\mathbf{D_{Margin}}$ means the Defender failed their defense, increasing the **Final Damage ($\mathbf{D_{Final}}$)**, while a negative $\mathbf{D_{Margin}}$ means the Defender successfully defended, reducing the damage base.