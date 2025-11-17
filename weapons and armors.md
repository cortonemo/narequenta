This proposal to add variable damage types, weapon bonuses, and armor-specific mitigation directly impacts the core mechanics of Nárëquenta, specifically the Tier-Neutral Lethality rule  and the unified damage formula.

The system's current structure relies on **Proficiency compensating for Decline**  where damage is primarily driven by $\mathbf{R_{prof}}$ (the Proficiency Roll Result) and the Tier-based $\mathbf{M_{DTA}}$ (Tier Advantage Multiplier).

Introducing flat bonuses from gear breaks the core **Attrition is Meaning** philosophy  by introducing non-decaying, external power sources. However, to incorporate the spirit of this request while preserving the core axioms, I propose an alternative design focusing on **Utility and Attrition Modification** rather than flat bonuses.

## ⚙️ Proposal: Gear as Attrition & Margin Modifiers

Instead of flat attack/defense bonuses, gear provides utility, mitigation, or shifts the nature of the Attrition Cost.

### I. Weapon and Attack Types (Utility Focus)

Weapons do not add flat damage; instead, they alter the action's **Motor/Quality Essence Pair**  and offer a unique utility or **Margin Modifier** on a successful hit, allowing a character to leverage their Proficiency more effectively.

| Weapon Type | Combat Role | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) Pair | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- | :--- |
| **Slashing** (Swords/Axes) | Force & Will | VITALIS / ANIMA  | Add $\mathbf{1d4}$ to the resulting $\mathbf{A_{FP}}$ (Full Potential Margin). |
| **Piercing** (Spears/Daggers) | Precision & Focus | MOTUS / SENSUS  | Ignore the $\mathbf{1\%}$ fixed $\mathbf{E_{S}}$ loss  on successful hit (Precision Attrition). |
| **Bludgeoning** (Hammers/Maces) | Endurance & Power | VITALIS / MOTUS  | On a critical hit, Defender subtracts their Tier's $\mathbf{\bar{M}}$ (Average Mitigation)  from their next defense roll. |
| **Ranged** (Bows/Thrown) | Finesse & Focus | MOTUS / SENSUS  | May target a non-Motor Essence; if hit, impose a $\mathbf{1d4\%}$ temporary $\mathbf{E_{cur}}$ penalty on the target Essence. |

### II. Armor and Defense Types (Attrition/Damage Reduction Focus)

Armor provides additional mitigation or reduces damage specifically against certain types, using historical context to inform the mechanic. Defense is still primarily handled by the Defender's $\mathbf{\bar{M}_{Defense}}$ (Average Mitigation).

| Armor Type | Historical Context | Defense Enhancement | Mitigation Rule ($\mathbf{D_{Final}}$ Modification) |
| :--- | :--- | :--- | :--- |
| **Light Armor** (Leather/Padded) | Focus on mobility and deflection. | **+5** to the Defender's **Current Essence ($\mathbf{E_{cur}}$)** against **Slashing** attacks (making success harder for Attacker). | No $\mathbf{D_{Final}}$ change. |
| **Medium Armor** (Mail/Brigandine) | Good all-around protection. | **+5** to the Defender's $\mathbf{\bar{M}_{Defense}}$  against **Bludgeoning** attacks only. | Apply the damage reduction *before* multiplying by $\mathbf{M_{DTA}}$. |
| **Heavy Armor** (Plate/Harness) | Near-total protection against piercing/slashing. | **-2** to the Attacker's $\mathbf{R_{prof}}$ (Proficiency Roll Result)  against **Piercing** attacks only (reducing the guaranteed damage base). | The reduction to $\mathbf{R_{prof}}$ is applied *before* the damage calculation. |

### 🛠️ Example Impact on Formulas

To implement the **Heavy Armor** rule, the $\mathbf{D_{Final}}$ formula would be modified for Piercing attacks:

$$
\mathbf{D_{Final}} = \max \left( 0, (A_{FP}^{*} - \bar{M}_{Defense} + D_{Margin} + (\mathbf{R_{prof}} - 2) ) \right) \times M_{DTA}
$$

*Where $\mathbf{A_{FP}^{*}}$ uses the adjusted $\mathbf{R_{prof}}$ for its calculation as well.*

---

Would you prefer to use the flat bonus system (breaking the attrition model) or proceed with this **Attrition/Margin Modification** system?

The Nárëquenta system integrates historical weapon types by defining their utility and effect on the Attrition and Damage Margins, rather than granting flat numerical bonuses. This preserves the core mechanical focus on Proficiency and Essence loss.

Here are examples for each damage category and their corresponding effects, based on the proposed **Attrition/Margin Modification** system.

## ⚔️ Weapon Attrition & Margin Modifiers (v0.9)

### 1. Slashing (VITALIS + ANIMA Pair)

Weapons of this type rely on **Force (VITALIS)** and **Will (ANIMA)** to cut through defenses, adding impact to the $\mathbf{A_{FP}}$ (Full Potential Margin).

| Weapon Name | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- |
| **Longsword / Katana** | VITALIS / ANIMA (Mêlée) | Add $\mathbf{1d4}$ to the resulting $\mathbf{A_{FP}}$. |
| **Battle Axe / War Scythe** | VITALIS / ANIMA (Mêlée) | Add $\mathbf{1d4}$ to the resulting $\mathbf{A_{FP}}$. |

### 2. Piercing (MOTUS + SENSUS Pair)

These weapons emphasize **Precision (MOTUS)** and **Focus (SENSUS)** to find openings, reducing the strain on the wielder's $\mathbf{E_{cur}}$.

| Weapon Name | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- |
| **Dagger / Rapier** | MOTUS / SENSUS (Finesse) | Ignore the $\mathbf{1\%}$ fixed $\mathbf{E_{S}}$ loss on successful hit. |
| **Lance / Spear** | MOTUS / SENSUS (Finesse) | Ignore the $\mathbf{1\%}$ fixed $\mathbf{E_{S}}$ loss on successful hit. |

### 3. Bludgeoning (VITALIS + MOTUS Pair)

These weapons use brute force and momentum (**VITALIS**) for impactful attacks. Their damage focuses on weakening the Defender's ability to resist future attacks.

| Weapon Name | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- |
| **Warhammer / Mace** | VITALIS / MOTUS (Force) | On a critical hit (GM-defined), Defender subtracts their Tier's $\mathbf{\bar{M}_{Defense}}$ from their next defense roll. |
| **Club / Quarterstaff** | VITALIS / MOTUS (Force) | On a critical hit (GM-defined), Defender subtracts their Tier's $\mathbf{\bar{M}_{Defense}}$ from their next defense roll. |

### 4. Ranged (MOTUS + SENSUS Pair)

Ranged attacks leverage **Motor (MOTUS)** coordination and **Focus (SENSUS)** to inflict specific penalties by targeting vulnerable points.

| Weapon Name | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- |
| **Hunting Bow / Longbow** | MOTUS / SENSUS (Range) | May target a non-Motor Essence; if hit, impose a $\mathbf{1d4\%}$ temporary $\mathbf{E_{cur}}$ penalty on the target Essence. |
| **Crossbow / Thrown Knife** | MOTUS / SENSUS (Range) | May target a non-Motor Essence; if hit, impose a $\mathbf{1d4\%}$ temporary $\mathbf{E_{cur}}$ penalty on the target Essence. |

### 5. Unarmed (VITALIS + MOTUS Pair)

Unarmed strikes are considered basic expressions of **Vigor (VITALIS)** and **Movement (MOTUS)**, using the standard $\mathbf{A_{FP}}$ calculation without a modifier.

| Weapon Name | Motor ($\mathbf{E_{P}}$) / Quality ($\mathbf{E_{S}}$) | Secondary Effect / Margin Modifier |
| :--- | :--- | :--- |
| **Fist / Kick** | VITALIS / MOTUS (Unarmed) | Standard damage calculation. |

---

Would you like to review the proposed Armor rules and see how they apply their specific damage reductions?

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
