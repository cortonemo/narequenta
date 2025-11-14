## Nárëquenta — Tales of the Waning

Change Log

All notable changes to this project will be documented in this file.
The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

## [v0.1] — 2025-10-25 (Private Development)
**Status:** Proof of Origin
* **Added:** Established the core mechanic of self-attrition: Actions consume Facet percentages.
* **Added:** Defined the optional “Scarring” system which lowers maximum value in exchange for efficiency.
* **Added:** Defined five Facets of the Self: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
* **Added:** Added Recovery Phase and Endgame rule.

---

## [v0.2] — 2025-10-26 (Design Framework)
**Status:** Alpha Test Readiness
* **Changed:** Facet naming to **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
* **Added:** Added the critical separation between **Maximum Essence ($\mathbf{E_{max}}$)** and **Current Essence ($\mathbf{E_{cur}}$)**.
* **Added:** Added the **Waning Scale**, where low $\mathbf{E_{max}}$ grants **Efficiency ($\mathbf{A_{rate}}$)** bonuses.
* **Added:** Added Hybrid Roll resolution ($\mathbf{E_P + E_S}$) and $\mathbf{E_{max}}$-mitigated Damage system.
* **Added:** Added Multilingual support (PT-PT / EN-US) and sheet automation logic.

---

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)
**Status:** Alpha Test Readiness
* **Removed:** Removed Attrition cost ($\mathbf{E_{cur}}$) for most actions outside of combat (e.g., Social, Investigation).
* **Added:** Added Fixed Cost rule of **$\mathbf{2\%}$** for extreme stress situations outside of combat.
* **Added:** Added **Symmetric Penalty ($\mathbf{10}$)** for NPCs, rewarding the player's narrative/tactical bonus in contested rolls.

---

## [v0.4] — 2025-10-26 (Final Progress Loop)
**Status:** Alpha Test Ready
* **Removed:** Removed the **Decay Milestone Scarring** and 10% Reallocation rules (obsolete).
* **Changed:** Altered the rule for progression and decay to **The Waning Roll**.
* **Changed:** Proficiency Choice rolls $\mathbf{4\text{d}6}$ (higher decay risk) in exchange for permanent **$\mathbf{2\text{d}10}$ Proficiency Dice ($\mathbf{D_{prof}}$)**.
* **Fixed:** Fixed game title to **Nárëquenta — Tales of the Waning**.

---

## [v0.5] — 2025-10-27 (Attack Rolls & Contested Combat)
**Status:** Alpha Test Ready - Core Combat Loop Defined
* **Changed:** The entire Action Resolution system now defaults to **Contested Rolls**.
* **Added:** **Proficiency Tiers and Dice Mapping** that tie $\mathbf{E_{max}}$ decay to $\mathbf{D_{prof}}$ acquisition.
* **Changed:** **Waning Roll** is now the primary mechanism for converting $\mathbf{E_{max}}$ loss into $\mathbf{D_{prof}}$.
* **Added:** **Critical Outcomes** system (Double Critical, Reversal) and **Proficiency Mitigation** ($\mathbf{D_{prof}}$ subtracts from $\mathbf{d100}$).
* **Added:** **Energy Depletion Cap** on $\mathbf{E_{cur}}$ loss from damage.
* **Added:** **Special Attacks** by trading $\mathbf{D_{prof}}$.

---

## [v0.7] — 2025-11-14 (Precision Lethality & Tier-Neutral Balance)
**Status:** Alpha Test Ready - Core Ruleset Finalized
* **Changed:** Version increased from v0.5 to v0.7 due to the **complete restructuring of progression and combat**.
* **Added:** **Initial Erosion ($\mathbf{1\text{d}10}$)** added for all Essences at character creation.
* **Added:** **Maximum Limit ($\mathbf{50\%}$)** added for $\mathbf{E_{max}}$, defining the permanent success ceiling.
* **Changed:** The **Proficiency Tier Table** was altered to **Uniform Progression ($\mathbf{1\text{d}10}$ per Tier)**, simplifying the scale and increasing power.
* **Changed:** The role of $\mathbf{D_{prof}}$ was **Unified** for: 1) Error Mitigation, 2) Attrition Reduction, and 3) **Additive Base Damage ($\mathbf{R_{prof}}$)**.
* **Added:** **Additive Damage Formula** (Precision Lethality) added: $\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right)$.
* **Added:** **Defensive Tier Advantage Multiplier ($\mathbf{M_{DTA}}$)** added to reduce damage from lower-Tier enemies ($\Delta T \ge 1$).
* **Added:** **Action Surge (AS) Progression** added, linking the number of available Action Surges to the Proficiency Tier (up to 4 AS at Tier V).
* **Changed:** The **Attrition Cost** was mitigated and simplified to: $\mathbf{E_{cur} \text{ Loss}} = \max \left( 0, (7 - R_{prof}) \right)$.
* **Added:** **Motor/Quality Essence Pairs** rule added to determine which $\mathbf{E_{cur}}$ pools are spent in combat.

---

🧾 Version Key

Type | Meaning
:---|:---
**Added**| New feature or mechanic
**Changed**| Adjusted or rebalanced rule
**Removed**| Mechanic or file removed
**Fixed**| Correction or typo

🪶 Credits

Design & Writing — Serelith Varn
System Development & Documentation — GPT-5 (Liora Vex Framework)
“We are remembered for how beautifully we burn out.”

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.