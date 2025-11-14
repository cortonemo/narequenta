## 📄 Nárëquenta Core Rules v0.7 (EN-US)

### 1. What This Game Is

Nárëquenta is a TTRPG where heroes begin near their peak and end spent.

Characters start defined by their initial **Erosion**.

They do not gain levels.

They are remembered for how beautifully they burn out.

You are not trying to survive forever.

You are deciding what parts of you are worth spending before you’re gone.

---

### 2. Facets of the Self (Essences)

Each character is defined by five Essences. Each Essence starts at **100%**, subject to Initial Erosion.

- **VITALIS** — body, endurance, force, presence
- **MOTUS** — movement, finesse, agility, grace
- **SENSUS** — awareness, instinct, focus, perception
- **VERBUM** — intellect, logic, structure, speech
- **ANIMA** — conviction, will, faith, sacrifice

Each Facet has:

- A **Current Value ($\mathbf{E_{cur}}$)** (how much of that part of you is still usable right now).
- A **Maximum Value ($\mathbf{E_{max}}$)** (the ceiling it can be restored to).
    - **Limit:** $\mathbf{E_{max}}$ can never drop below **$50\%$**.

At character creation:

- **Initial Erosion:** Roll **$1d10$** for each Essence. This value is subtracted from **$100\%$**, setting the initial $\mathbf{E_{cur}}$ and $\mathbf{E_{max}}$ values.

---

### 3. Acting in the World (Action Resolution: Precision Lethality)

Actions are resolved as **Contested Rolls** ($\mathbf{d100 \le \mathbf{E_{cur}}}$). Only the **Attacker** utilizes $\mathbf{D_{prof}}$ for offensive output.

#### Action Resolution Flow
1. **Attacker Rolls:** A rolls $\mathbf{d100}$ and their **Proficiency Dice ($\mathbf{D_{prof}}$)**. The result is $\mathbf{R_{prof}}$.
2. **Attacker Mitigates:** A **subtracts the $\mathbf{R_{prof}}$ from the $\mathbf{d100}$ roll** (Error Mitigation). If the resulting roll is $\le$ the Attacker's $\mathbf{E_{cur}}$, the attack hits.
3. **Defender Rolls:** D rolls $\mathbf{d100 \le \mathbf{E_{cur}}}$ to determine the **Defender's Margin ($\mathbf{D_{Margin}}$)** (Sec. 6).

#### Critical Outcomes (Retained from v0.5)
The Critical Hit range is defined as **$<$10 on the d100 roll**. The Critical Fail range is **$>$90 on the d100 roll**.
* **Double Critical:** If A rolls a Critical Hit and D rolls a Critical Fail, the attack triggers a Double Crit. The attacker deals **10d10 Damage**.
* **Reversal on Failure:** If A rolls a Critical Fail and D rolls a Critical Hit, the attacker receives the full critical damage from the defender (**10d10**).

#### Attrition Cost
1. **Pillars:** Cost is applied to the **Motor Essence ($\mathbf{E_{P}}$)** and **Quality Essence ($\mathbf{E_{S}}$)**.
2. **Cost Formula:**
    - **$E_{P}$ Loss (Motor):** $\mathbf{D_{Loss} = \max \left( 0, (7 - R_{prof}) \right)}$ (Pays the mitigated cost).
    - **$E_{S}$ Loss (Quality):** **$1\%$** (Pays a minor fixed cost).

#### Actions Outside of Combat (Attrition Scope)
Most actions outside of combat **do not incur Attrition costs**, using $\mathbf{E_{cur}}$ only as the success limit.

When $\mathbf{E_{cur}}$ hits 0% in an Essence:
- You cannot act through that Essence anymore. That part of you is exhausted.

---

### 4. Refinement Cycle (The Waning Roll)

Refinement and Decay occur at the conclusion of every major milestone. The **Proficiency Tier** is determined by the total $\mathbf{E_{max}}$ loss.

#### 4.1. The Proficiency Choice & Waning Roll
1. **Focus:** Player chooses **one (1)** Essence for Focus.
2. **Decay:** Apply Decay, subject to the **50% $\mathbf{E_{max}}$ limit**:
    - **Non-Chosen Essences:** $\mathbf{2\text{d}6}$ permanently subtracted from $\mathbf{E_{max}}$.
    - **Chosen Essence (Focus):** $\mathbf{4\text{d}6}$ permanently subtracted from $\mathbf{E_{max}}$, granting an increase in the **$\mathbf{D_{prof}}$ Pool**.

#### 4.2. Using Proficiency (Uniform Tier System)
The $\mathbf{D_{prof}}$ gained is converted into a pool of **$1d10$ per Tier** (max $5d10$ at Tier V). $\mathbf{D_{prof}}$ is the primary engine for offensive power and efficiency.

---

### 5. Rest and Renewal (Recovery)

After a mission ends, there is a Recovery Phase.

Recovery does:

- Restore the **E_cur** up to the current **E_max** value.
- **DOES NOT** restore $\mathbf{E_{max}}$ that was permanently lost.
- **RESTORES** the **Action Surge (AS)** pool (Sec. 7).

---

### 6. Damage & Health (Tier-Neutral Lethality)
* All characters have a base of **100 HP**.

### Damage Formula
Damage is calculated using the Attacker's Full Potential Margin ($\mathbf{A_{FP}}$) and modified by the Defender's Tier Advantage ($\mathbf{M_{DTA}}$).

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$$

* $\mathbf{A_{FP}}$ (Full Potential Margin) $\equiv 100 - (d100 - R_{prof})$.
* $\mathbf{\bar{M}_{Defense}}$ (Defense Mitigation) $\equiv$ Defender's Average $R_{prof}$ (Tier-based mitigation).
* $\mathbf{M_{DTA}}$ (Defensive Tier Advantage Multiplier) $\equiv$ Reduces damage taken if Defender Tier $>$ Attacker Tier.

---

### 7. Endgame and Action Surge Progression

You retire hollowed and legendary.

* **Action Surge Progression:** The AS pool (granting extra attacks per Recovery cycle) scales with Tier, compensating for the low $\mathbf{E_{max}}$ ceiling. (Tier V grants 4 AS).
* **Survival:** By late play, your Efficiencies and $\mathbf{D_{prof}}$ make you incredibly lethal, despite having a low $\mathbf{E_{cur}}$ ceiling.

The campaign is the record of **how you chose to fade.**

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).