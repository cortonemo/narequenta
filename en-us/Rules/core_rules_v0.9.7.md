# 📜 Nárëquenta Core Rules v0.9.7 (Steel & Splinters)

## 1. What This Game Is 🧭

Nárëquenta is a TTRPG where heroes begin near their peak and end spent. Progression is the **defining of character through loss**. Power is a finite resource. **Proficiency Compensates for Decline**.
***

## 2. Facets of the Self (Essences) ✨

Each character is defined by five Essences. Each Essence starts at **$100\%$**, subject to Initial Erosion.

- **VITALIS** — body, endurance, force, presence
- **MOTUS** — movement, finesse, agility, grace
- **SENSUS** — awareness, instinct, focus, perception
- **VERBUM** — intellect, logic, structure, speech
- **ANIMA** — conviction, will, faith, sacrifice

### Essence Values

- **Maximum Value ($\mathbf{E_{max}}$):** Permanent limit. Can never drop below **$50\%$** (Hard Floor).
- **Current Value ($\mathbf{E_{cur}}$):** Usable energy. Determines your **Zone of Strain**.
***

## 3. Action Resolution: The Effective Roll 🎯

Success is determined by comparing the **Effective Roll** against the Permanent Capacity ($\mathbf{E_{max}}$), adjusted by fatigue.

### A. Lockout Condition (The Absolute Void)

Before any roll, the Current Value ($\mathbf{E_{cur}}$) is checked.

$$\text{If } \mathbf{E_{cur}} < 1 \rightarrow \text{Automatic Failure / Action Impossible}$$

> ==**If Active Vigor is less than 1, the action results in automatic failure.**==

**Emergency Recovery (The Quick Breath):** If you are at $0 \mathbf{E_{cur}}$, you may spend your entire turn to take a Quick Breath (Short Rest).

### B. The Effective Roll Formula

$$\mathbf{R_{Eff}} = \mathbf{d100} - \mathbf{R_{prof}}$$

> ==**The Effective Roll equals the Chaos Die ($\mathbf{d100}$) minus the Skill Result ($\mathbf{R_{prof}}$).==**

### C. The Success Check

$$\mathbf{R_{Eff}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalty}})$$

> ==**The action succeeds if the Effective Roll is less than or equal to your $\mathbf{E_{max}}$ minus the current Zone Penalty.==**

### D. Zones of Strain ($\mathbf{E_{cur}}$)

As $\mathbf{E_{cur}}$ depletes, you fall into lower Zones, increasing the difficulty of actions.

| **Range $\mathbf{E_{cur}}$** | **Zone Name** | **Penalty ($\mathbf{Z_{Penalty}}$)** |
| :--- | :--- | :--- |
| **100% – 76%** | **Peak** | **-0** |
| **75% – 51%** | **Waning** | **-10** |
| **50% – 26%** | **Fading** | **-20** |
| **25% – 0%** | **Hollow** | **-30** |
***

## 4. Attrition: The Cost of Action 🩸

Every action burns Essence. The cost is derived from the **Item Weight** and mitigated by **Skill**.

### Attrition Formula

$$\mathbf{Cost} = \max \left( 0, \mathbf{Weight} - \left\lfloor \frac{\mathbf{R_{prof}}}{2} \right\rfloor \right)$$

> **The Energy Cost equals the Weapon Weight minus half of the Proficiency Roll (rounded down).**

| **Weight Class** | **Base Cost** | **Examples** |
| :--- | :--- | :--- |
| **Light** | **10%** | Daggers, Shortbows |
| **Medium** | **15%** | Swords, Javelins |
| **Heavy** | **20%** | Mauls, Arbalests |

- **Critical Success (1-5):** Halve the final Cost.
- **Critical Failure (96-100):** Double the final Cost.
***

## 5. Combat: Precision Lethality ($\mathbf{D_{Final}}$) 💥

Damage calculation privileges Skill ($\mathbf{R_{prof}}$). The formula remains Additive, but Mitigation is now granular, composed of **Tier**, **Armor**, and **Active Parry**.

### Final Damage Formula

$$\mathbf{D_{Final}} = \max \left( \mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Total}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}}) \right) \times \mathbf{M_{DTA}}$$

> ==**Final Damage is the higher of the Proficiency Floor or the Calculated Margin, multiplied by the Tier Advantage.**==

| **Component** | **Definition** |
| :--- | :--- |
| **$\mathbf{R_{prof}}$ (Hard Floor)** | **Additive Base Damage.** The absolute minimum damage is your Proficiency Roll result. |
| **$\mathbf{A_{FP}}$** | **Full Force Potential.** $100 - (d100 - R_{prof})$. Modified by **Weapon Attack Bonus**. |
| **$\mathbf{\bar{M}_{Total}}$** | **Total Mitigation.** The sum of $\mathbf{\bar{M}_{Tier}} + \mathbf{\bar{M}_{Static}} + \mathbf{\bar{M}_{Parry}}$. |
| **$\mathbf{D_{Margin}}$ (Vulnerability)** | Defender's Defense Roll minus Defender's $\mathbf{E_{cur}}$. Positive values add damage. |
| **$\mathbf{M_{DTA}}$ (Tier Advantage)** | Multiplier scaling from $\times 0.75$ (Uphill) to $\times 2.00$ (Overpower). |

### A. The Three Layers of Mitigation ($\mathbf{\bar{M}_{Total}}$)

1.  **Reflex ($\mathbf{\bar{M}_{Tier}}$):** Your innate ability to roll with punches.
    * *Formula:* $\text{Tier} \times 5.5$.
2.  **Static ($\mathbf{\bar{M}_{Static}}$):** Physical barriers that function regardless of action.
    * *Source:* **Armor** (Worn) and **Shields** (Held).
    * *Always Active.*
3.  **Active Parry ($\mathbf{\bar{M}_{Parry}}$):** Using a weapon to deflect incoming blows.
    * *Source:* **Melee Weapons** (Swords, Spears, etc.).
    * *Restriction:* Only applies against **Melee Attacks**. If the enemy is Ranged (>5ft), you cannot parry the projectile effectively with a weapon (Shields still apply).

### B. Weapon Data (Attack & Parry)

Weapons are defined by their balance of Aggression (Attack Bonus) vs. Safety (Parry Bonus).

| Weapon Type | Attack Bonus (Add to $\mathbf{A_{FP}}$) | Parry Bonus (Add to $\mathbf{\bar{M}}$) | Tactical Note |
| :--- | :---: | :---: | :--- |
| **Unarmed** | +0 | +0 | Vulnerable. |
| **Monk Style** | +1 | +4 | Deflection techniques. |
| **Dagger** | +0 | +1 | Too small to guard effectively. |
| **Sword** | +2 | +3 | The perfect balance. |
| **Axe/Mace** | +4 | +1 | High impact, poor recovery. |
| **Spear** | +1 | +4 | Range keeps enemies away (High Mitigation). |
| **Bow** | +0 | +1 | Desperate blocking only. |
***

## 6. Rituals and Renewal (Recovery) 🕯️

Rituals close the game cycle (Spend → Fade → **Renew**), allowing the PC to manage their daily fatigue and accept their permanent loss.

### A. Focus Renewal (Long Rest) 🌙

This ritual allows the PC to recover their mental and physical focus, returning to their daily potential.

- **Trigger:** Long Rest (e.g., a safe night's sleep, minimum 6 hours).
- **Process:**
    1. **Vigor Restoration:** The **Current Value ($\mathbf{E_{cur}}$)** of all Essences resets to **100%**.
        > _Critical Rule:_ Recovery is **NOT** capped by $\mathbf{E_{max}}$. Even if your Soul Peak is degraded to 50%, your Active Vigor returns to 100%. You begin the day fully energized, in the **Peak Zone**.
    2. **Surge Restoration:** The **Action Surge (AS) Pool** is **fully restored** to the total determined by the character's Proficiency Tier.
- **Narrative Cost:** Time and safety.

### B. The Short Rest (Respite) 🍵

A brief pause to bind wounds, catch breath, and center the mind (15 minutes).

$$\mathbf{Recovery} = \text{Sum of } \mathbf{D_{prof}}$$

> ==**Recovery equals the sum of your Proficiency Dice pool results.**==

(Fallback: If Tier 0, roll 1d10).

### C. Emergency Recovery (The Quick Breath) 💨

A desperate attempt to center oneself in the heat of battle, usually triggered when hitting the Void ($0 \ \mathbf{E_{cur}}$).

- **Trigger:** Can be taken at any time during your turn, or forced when $\mathbf{E_{cur}} < 1$.
- **Cost:** **Entire Turn Action.** You cannot Move, Defend, Attack, or React until the start of your next turn.
- **Effect:** Immediately resolves as a **Short Rest** (Roll $\mathbf{D_{prof}}$ or 1d10 and recover that amount to $\mathbf{E_{cur}}$).

### D. Note on Permanent Loss 💀

The system distinguishes between **Fatigue** and **Decay**.

- **Renewable:** $\mathbf{E_{cur}}$ (**Active Vigor**) represents energy. It fluctuates constantly and recovers to **100%**.
- **Non-Renewable:** $\mathbf{E_{max}}$ (**Soul Peak**) represents the soul's structural integrity. The system **DOES NOT** restore $\mathbf{E_{max}}$ lost through the Waning Roll.
***

## 7. Progression: The Waning Roll 🌘

Progression occurs at narrative milestones by permanently reducing $\mathbf{E_{max}}$ to advance Proficiency Tiers.

- **Universal Decay (Non-Chosen):** Roll **1d6**. Subtract from $\mathbf{E_{max}}$.
- **Refinement Focus (Chosen):** Roll **2d6**. Subtract from $\mathbf{E_{max}}$ to gain $\mathbf{D_{prof}}$.

### Proficiency & Dice Mapping Table

| **Tier** | **Total $\mathbf{E_{max}}$ Loss** | **Remaining $\mathbf{E_{max}}$** | **$\mathbf{D_{prof}}$ Dice** | **Mitigation ($\mathbf{\bar{M}}$)** | **Action Surges** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | $0-9\%$ | $100-91\%$ | None | $0.0$ | **0** |
| **I** | $10-19\%$ | $90-81\%$ | $\mathbf{1\text{d}10}$ | $5.5$ | **1** |
| **II** | $20-29\%$ | $80-71\%$ | $\mathbf{2\text{d}10}$ | $11.0$ | **2** |
| **III** | $30-39\%$ | $70-61\%$ | $\mathbf{3\text{d}10}$ | $16.5$ | **3** |
| **IV** | $40-49\%$ | $60-51\%$ | $\mathbf{4\text{d}10}$ | $22.0$ | **4** |
| **V** | $\mathbf{50\%}$ | **50% (Pinnacle)** | $\mathbf{5\text{d}10}$ | $\mathbf{27.5}$ | **5** |
***

## 8. Use of Proficiency (Detailed Mechanics) ⚙️

The result of the $\mathbf{D_{prof}}$ roll ($\mathbf{R_{prof}}$) is used for three simultaneous effects:

1.  **Error Mitigation:** Subtract $\mathbf{R_{prof}}$ from the $\mathbf{d100}$ roll.
2.  **Attrition Reduction:** $\mathbf{Cost} = \text{Weight} - \lfloor R_{prof}/2 \rfloor$.
3.  **Special Attacks (Optional):** Sacrifice dice from the $\mathbf{D_{prof}}$ *pool* to perform enhanced actions.
***

## 9. Optional Rule: Splintering Steel (Weapon Integrity) ⚔️

Tools in Nárëquenta are not eternal; they erode like the souls that wield them.

### 1. Integrity ($\Omega$)
Every weapon has an **Integrity Rating**.
* **Standard:** 3
* **Fine:** 5
* **Relic:** 10

### 2. Fracture Events
A weapon loses **1 Point of Integrity** when:
* **Critical Failure (96-100):** You strike a hard surface at a catastrophic angle.
* **Sacrificial Parry:** The wielder chooses to absorb a **Critical Hit** (Attacker 1-5) entirely on the weapon to negate the Critical effect.

### 3. The Shattering
When Integrity reaches **0**:
* The weapon is **Broken**.
* **Attack Bonus** becomes 0.
* **Parry Bonus** becomes 0.
* **Damage** is limited to the raw $R_{prof}$ floor only.
***

## 10. Appendix: System Reference (Sigla) 📚

### Component Breakdowns

1. Full Potential Margin ($\mathbf{A_{FP}}$)

$$\mathbf{A_{FP}} = \mathbf{100 - (d100-R_{prof})}$$

> ==**This calculates the Attacker's raw power relative to a perfect 100 base. A lower modified roll yields a higher $\mathbf{A_{FP}}$.==**

2. Defender Margin ($\mathbf{D_{Margin}}$)

$$\mathbf{D_{Margin}} = \mathbf{d100_D-D_{Ecur}}$$

> ==**This measures the Defender's vulnerability. A positive $\mathbf{D_{Margin}}$ means the Defender failed their defense, increasing damage.==**

***
© 2025 Serelith Varn — Nárëquenta. Licensed under Nárëquenta Limited Open License (v0.1). See [[LICENSE.md]].
