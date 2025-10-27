## 📄 Nárëquenta Core Rules v0.5 (EN-US)

### 1. What This Game Is

Nárëquenta is a TTRPG where heroes begin perfect and end spent.
Characters start at full strength in every aspect of themselves.
They do not gain levels.
They are remembered for how beautifully they burn out.
You are not trying to survive forever.
You are deciding what parts of you are worth spending before you’re gone.

---

### 2. Facets of the Self (Essences)

Each character is defined by five Essences. Each Essence starts at 100%.

- **VITALIS** — body, endurance, force, presence
- **MOTUS** — movement, finesse, agility, grace
- **SENSUS** — awareness, instinct, focus, perception
- **VERBUM** — intellect, logic, structure, speech
- **ANIMA** — conviction, will, faith, sacrifice

Each Facet has:

- A **Current Value ($\mathbf{E_{cur}}$)** (how much of that part of you is still usable right now).
- A **Maximum Value ($\mathbf{E_{max}}$)** (the ceiling it can be restored to).
- An **Attrition Rate ($\mathbf{A_{rate}}$)** (how costly it is for you to act through that Facet).

At character creation:

- Current ($\mathbf{E_{cur}}$) = 100%
- Max ($\mathbf{E_{max}}$) = 100%
- Attrition Rate (Base Cost) = $30\%$/$40\%$

---

### 3. Acting in the World (Action Resolution: Contested Rolls)

Actions are now resolved as **Contested Rolls** where both the Attacker (A) and Defender (D) roll to influence the outcome. The goal is always to roll $\mathbf{d100 \le \mathbf{E_{cur}}}$ of the relevant Essence ($\mathbf{E_{P}}$).

#### Action Resolution Flow
1. **Attacker Rolls:** A rolls $\mathbf{d100 \le \mathbf{E_{cur}}}$ (Attacker Motor $\mathbf{E_{P}}$) to hit.
2. **Attacker Mitigates:** A rolls their **Proficiency Dice ($\mathbf{D_{prof}}$)** and **subtracts the result from the $\mathbf{d100}$ roll**.
3. **Defender Rolls:** If the attack lands, the D rolls $\mathbf{d100 \le \mathbf{E_{cur}}}$ (Defender Motor $\mathbf{E_{P}}$) to mitigate damage.

#### Critical Outcomes (Attack & Defense)
The Critical Hit range is defined as **$<$10 on the d100 roll**. The Critical Fail range is **$>$90 on the d100 roll**.

* **Double Critical:** If A rolls a Critical Hit and D rolls a Critical Fail, the attack triggers a Double Crit. The attacker deals **10d10 Damage**.
* **Reversal on Failure:** If A rolls a Critical Fail and D rolls a Critical Hit, the attacker receives the full critical damage from the defender (**10d10**).

#### Attrition Cost
1. **Success Costs:** Success still costs the most. The cost is calculated as the **Attrition Rate ($\mathbf{A_{rate}}$)** of the Motor ($\mathbf{E_{P}}$) plus the fixed cost ($1\%-2\%$) of the Quality ($\mathbf{E_{S}}$).
2. **Proficiency Reduction:** The average result of the $\mathbf{D_{prof}}$ used is **subtracted from the total $\mathbf{E_{cur}}$ loss**. This makes refined actions more efficient.

#### Actions Outside of Combat (Attrition Scope Refinement)
Most actions outside of combat (investigation, social interactions) **do not incur Attrition costs**, using $\mathbf{E_{cur}}$ only as the success limit. Only in situations of extreme physical or mental stress should the GM apply a **Fixed Cost of $\mathbf{2\%}$** (or more, by consensus) to simulate sustained effort.

When $\mathbf{E_{cur}}$ hits 0% in an Essence:
- You cannot act through that Essence anymore. That part of you is exhausted.

When **ALL** Essences hit 0%:
- Your story is done. Dead, ascended, or faded, depending on the fiction.

---

### 4. Refinement Cycle (The Waning Roll)

**This mechanic replaces the previous Scarring/Reallocation system.** Refinement and Decay occur at the conclusion of every major milestone, mission, or chapter.

#### 4.1. The Proficiency Choice
Before rolling for Decay, the player must choose **one (1)** Essence for Focus (the Refinement Essence).

|**Risk**|**Reward (Proficiency)**|
|---|---|
|Decay Roll of $\mathbf{4\text{d}6}$|Gain $\mathbf{2\text{d}10}$ **Proficiency Dice ($\mathbf{D_{prof}}$)** on contested rolls using this Essence.|

#### 4.2. The Waning Roll (Decay Phase)
Apply Decay to all Essences:

|**Essence**|**Decay Roll**|**Effect on Emax​**|
|---|---|---|
|**Non-Chosen Essences**|$\mathbf{2\text{d}6}$|The total is permanently subtracted from the **Maximum Value ($\mathbf{E_{max}}$)**.|
|**Chosen Essence (Focus)**|$\mathbf{4\text{d}6}$|The total is permanently subtracted from the **Maximum Value ($\mathbf{E_{max}}$)** (burns faster).|

#### 4.3. Using Proficiency (New Tier System)
The $\mathbf{2\text{d}10}$ Proficiency Dice gained from the Waning Roll are converted into a pool of $\mathbf{D_{prof}}$ based on the new Proficiency Tier table (see `rules_contested_rolls_v0.5.md`). The $\mathbf{D_{prof}}$ are used primarily for **Error Mitigation** (subtracting from the d100 roll) and **Attrition Reduction**.

---

### 5. Rest and Renewal (Recovery)

After a mission ends, there is a Recovery Phase.

Recovery does:

- Restore the **E_cur** (Focus) up to the current **E_max** value.
- **DOES NOT** restore $\mathbf{E_{max}}$ that was permanently lost during the **Waning Roll** (Section 4).

You are always coming back a little less than you were.

---

### 6. Damage & Health
* All characters have a base of **100 HP**, regardless of their **$\mathbf{E_{max}}$**.
* **Bonus Damage:** If the attacker rolls significantly below their own $\mathbf{E_{cur}}$ (e.g., a roll of 12 vs. stat 60), **+5 HP for each 10% below the attacker’s stat** is applied.
* **Energy Depletion Cap:** The maximum $\mathbf{E_{cur}}$ depletion from damage is capped by the **maximum possible result of the character's highest Proficiency Die** (e.g., max 6 for 1d6, max 10 for 1d10).

### 7. Endgame

You don't retire rich. You retire hollowed and legendary.

By late play:

- Your Maximums ($\mathbf{E_{max}}$) are low (60%, 55%, 43%...).
- Your Efficiencies ($\mathbf{A_{rate}}$) are inhuman (3%, 4%...).
- Every move costs almost nothing, but you have very few moves left.

The campaign is the record of **how you chose to fade.**

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
