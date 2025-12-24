# 📜 Nárëquenta — Tales of the Waning

**Change Log**

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

***
## [v0.9.7] — 2025-12-02 (Steel & Splinters)
**Status:** Beta Feature Expansion - Equipment Logic
- **Changed:** **Combat Formula** updated to use $\mathbf{\bar{M}_{Total}}$ instead of just Tier Mitigation.
- **Added:** Defined **Three Layers of Mitigation**: Reflex (Tier×5.5), Static (Armor/Shields), and Active Parry (Weapons).
- **Added:** **Weapon Data Table** defining Attack ($\mathbf{A_{FP}}$) and Parry ($\mathbf{\bar{M}}$) bonuses for standard archetypes (Sword, Axe, Spear, Bow, Unarmed).
- **Added:** **Parry Restriction Rule:** Active Parry only applies against attacks within melee range (≤5ft).
- **Added:** **Optional Rule: Splintering Steel.** Weapons now have an Integrity rating (3/5/10) and degrade on Critical Failures or Sacrificial Parries.

***

## [v0.9.64] — 2025-12-01 (Unified Recovery)
**Status:** Beta Refinement - Game Cycle Adjustment
- **Changed:** **Focus Renewal (Long Rest)** rule altered. $\mathbf{E_{cur}}$ restoration now goes to **100%** (Peak Zone), no longer limited by the current $\mathbf{E_{max}}$ value. The $\mathbf{E_{max}}$ limit applies only to difficulty tests.
- **Added:** Defined **Short Rest** formula as the **Sum of $\mathbf{D_{prof}}$ results** (or 1d10 for Tier 0).
- **Added:** **Emergency Recovery (The Quick Breath)** mechanic added, allowing a full action to be spent to perform a Short Rest when Vigor hits zero.
- **Fixed:** Consolidated Core Rules and Rituals files into a single logical flow for easier reference.

---

## [v0.9.6] — 2025-11-28 (Precision Lethality & Zones of Strain)
**Status:** Beta Refinement - Core Math Update
- **Changed:** **Success Threshold** altered. Success is now $\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalty}})$. Current Essence ($\mathbf{E_{cur}}$) only determines the Zone.
- **Added:** **Zones of Strain** defined: **Peak** (-0), **Waning** (-10), **Fading** (-20), and **Hollow** (-30).
- **Changed:** **Attrition Formula** updated to reflect Item Weight.
    - Old: $\max(0, 7 - R_{prof})$.
    - New: $\max(0, \mathbf{Weight} - \lfloor R_{prof}/2 \rfloor)$.
- **Added:** **Weight Classes** defined as Light (**10%**), Medium (**15%**), and Heavy (**20%**).
- **Changed:** **Damage Formula** updated to include a **Hard Floor**. Damage can no longer be reduced below the raw $\mathbf{R_{prof}}$ result by mitigation (before Tier Multipliers).
- **Fixed:** Localization files (`en.json`) updated to reflect the new Attrition and Success formulas.

---

## [v0.9] — 2025-11-17 (Progressive Mastery & Attrition Control)
**Status:** Progression Logic Finalized
- **Changed:** Progression via $\mathbf{E_{max}}$ loss is now strictly sequential (one Tier at a time).
- **Added:** Tier Synchronization Rule for Waning Rolls.
- **Added:** **Refocus (Short Rest)** mechanic to restore $\mathbf{E_{cur}}$.
- **Added:** **Final Spark** emergency action ($\mathbf{E_{cur}=0\%}$).

---

## [v0.8] — 2025-11-15 (SPA Migration & Stabilization)
**Status:** Architecture Stabilized
- **Added:** Implementation of **Single Page Application (SPA)** architecture.
- **Added:** Full integration of the **Damage Calculator** into the GM Reference section.
- **Fixed:** Critical fixes to Python launcher and localization logic.

---

## [v0.7] — 2025-11-14 (Precision Lethality)
**Status:** Core Rules Finalized
- **Changed:** Complete restructuring of progression and combat.
- **Added:** **Initial Erosion ($\mathbf{1\text{d}10}$)** at character creation.
- **Added:** **Maximum Limit ($\mathbf{50\%}$)** for $\mathbf{E_{max}}$.
- **Changed:** Proficiency Tier Table altered to **Uniform Progression ($\mathbf{1\text{d}10}$ per Tier)**.
- **Added:** Additive Damage Formula and Tier Advantage Multiplier ($\mathbf{M_{DTA}}$).
- **Added:** Motor/Quality Essence Pairs rule.

---

## [v0.5] — 2025-10-27 (Attack Rolls & Combat)
**Status:** Alpha Test Ready
- **Changed:** Action Resolution system defaults to **Contested Rolls**.
- **Added:** Proficiency Tiers and Dice Mapping.
- **Added:** Critical Outcomes and Proficiency Mitigation system.

---

## [v0.4] — 2025-10-26 (Final Progress Loop)
**Status:** Alpha Test Ready
- **Removed:** Obsolete Scarring rules removed.
- **Changed:** Progression rule altered to **The Waning Roll**.
- **Changed:** Proficiency Choice rolls $\mathbf{4\text{d}6}$ in exchange for permanent **$\mathbf{2\text{d}10}$ Proficiency Dice ($\mathbf{D_{prof}}$)**.
- **Fixed:** Game title fixed to **Nárëquenta — Tales of the Waning**.

---

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)
**Status:** Alpha Test Readiness
- **Removed:** Removed Attrition cost ($\mathbf{E_{cur}}$) for most non-combat actions.
- **Added:** Added Fixed Cost rule of **$\mathbf{2\%}$** for extreme stress situations outside combat.
- **Added:** Added **Symmetric Penalty ($\mathbf{10}$)** for NPCs.

---

## [v0.2] — 2025-10-26 (Design Framework)
**Status:** Alpha Test Readiness
- **Changed:** Facet naming changed to **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**.
- **Added:** Added critical separation between **Maximum Essence ($\mathbf{E_{max}}$)** and **Current Essence ($\mathbf{E_{cur}}$)**.
- **Added:** Added **Waning Scale**, where low $\mathbf{E_{max}}$ grants Efficiency bonuses.
- **Added:** Added Hybrid Roll resolution and $\mathbf{E_{max}}$-mitigated Damage system.
- **Added:** Added Multilingual support (PT-PT / EN-US) and sheet automation logic.

---

## [v0.1] — 2025-10-25 (Private Development)
**Status:** Proof of Origin
- **Added:** Established core mechanic of self-attrition: Actions consume Facet percentages.
- **Added:** Defined optional "Scarring" system reducing max value for efficiency.
- **Added:** Defined five Facets of the Self: VIGOR · GRACE · MIND · SPIRIT · SHADOW.
- **Added:** Added Recovery Phase and Endgame rule.

***

🧾 Version Key

|**Type**|**Meaning**|
|---|---|
|**Added**|New feature or mechanic|
|**Changed**|Adjusted or rebalanced rule|
|**Removed**|Mechanic or file removed|
|**Fixed**|Correction or typo|

---
🪶 Credits

Design & Writing — Serelith Varn
System Development & Documentation — GPT-5 (Liora Vex Framework)

“We are remembered for how beautifully we burn out.”

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](LICENSE.md).

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
