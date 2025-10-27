# Nárëquenta — Tales of the Waning

Change Log

All notable changes to this project will be documented in this file.
The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

## [v0.1] — 2025-10-25

**Status:** Private Development (Proof of Origin)
**Highlights**
- **Established** the core mechanic of self-attrition: Actions consume Facet percentages.
- **Defined** the optional “Scarring” system which lowers maximum value in exchange for efficiency.
- **Defined** five Facets of the Self: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
- **Added** Recovery Phase and Endgame rule.

**Structure**
/rules/core_rules_v0.1.md
/playtest/character_sheet_v0.1.md
/playtest/gm_reference_v0.1.md

---

## [v0.2] — 2025-10-26 (Design Framework)

**Status:** Alpha Test Readiness
**Highlights**
- **Changed** Facet naming to **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
- **Added** the critical separation between **Maximum Essence ($\mathbf{E_{max}}$)** and **Current Essence ($\mathbf{E_{cur}}$)**.
- **Added** the **Waning Scale**, where low $\mathbf{E_{max}}$ grants **Efficiency ($\mathbf{A_{rate}}$)** bonuses.
- **Added** Hybrid Roll resolution (E_P + E_S) and $\mathbf{E_{max}}$-mitigated Damage system.
- **Added** Multilingual support (PT-PT / EN-US) and sheet automation logic.

---

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)

**Status:** Alpha Test Readiness
**Highlights**
- **Removed** Attrition cost ($\mathbf{E_{cur}}$) for most actions outside of combat (e.g., Social, Investigation).
- **Added** Fixed Cost rule of **$\mathbf{2\%}$** for extreme stress situations outside of combat.
- **Added** **Symmetric Penalty ($\mathbf{10}$)** for NPCs, rewarding the player's narrative/tactical bonus in contested rolls.

---

## [v0.4] — 2025-10-26 (Final Progress Loop)

**Status:** Alpha Test Ready
**Highlights**
- **Removed** the **Decay Milestone Scarring** and 10% Reallocation rules (obsolete).
- **Added** the new progression and decay mechanic: **The Waning Roll**.
    - **Universal Decay:** $\mathbf{2\text{d}6}$ subtracted from $\mathbf{E_{max}}$ at the end of each chapter.
    - **Proficiency Choice:** PC rolls $\mathbf{4\text{d}6}$ (higher decay risk) in exchange for permanent **$\mathbf{2\text{d}10}$ Proficiency Dice ($\mathbf{D_{prof}}$)**, increasing reliability.
- **Fixed** game title to **Nárëquenta — Tales of the Waning**.

---

## [v0.5] — 2025-10-27 (Attack Rolls & Contested Combat)

**Status:** Alpha Test Ready - Core Combat Loop Defined
**Highlights**
- **Changed** The entire Action Resolution system now defaults to **Contested Rolls**.
- **Added** **Proficiency Tiers and Dice Mapping** that tie $\mathbf{E_{max}}$ decay to Proficiency Dice ($\mathbf{D_{prof}}$) acquisition (1d6 up to 3d10/4d10).
- **Changed** **Waning Roll** is now the primary mechanism for converting $\mathbf{E_{max}}$ loss into $\mathbf{D_{prof}}$.
- **Added** **Critical Outcomes** system: **Double Critical** (Attacker Crit Hit vs. Defender Crit Fail) deals **10d10 Damage**. Critical Failure Reversal added.
- **Added** **Proficiency Mitigation:** $\mathbf{D_{prof}}$ are now rolled to **subtract from the d100 roll result** (error mitigation).
- **Added** **Energy Depletion Cap:** Energy loss from damage is capped by the maximum result of the highest $\mathbf{D_{prof}}$ die.
- **Added** **Narrative Influence:** Introduced the DM's **Narrative Modifier Die** (1d6) to reward rich action descriptions.
- **Added** **Special Attacks** by trading $\mathbf{D_{prof}}$.

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
