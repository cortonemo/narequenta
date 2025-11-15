## 📜 Nárëquenta — Tales of the Waning

**Change Log**

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog, and adheres to Semantic Versioning when applicable.

---

## [v0.1] — 2025-10-25 (Private Development)

**Status:** Proof of Origin

- **Added:** Established the core mechanic of self-attrition: Actions consume Facet percentages1.
    
- **Added:** Defined the optional “Scarring” system which lowers maximum value in exchange for efficiency2.
    
- **Added:** Defined five Facets of the Self: VIGOR · GRACE · MIND · SPIRIT · SHADOW3.
    
- **Added:** Added Recovery Phase and Endgame rule4.
    

---

## [v0.2] — 2025-10-26 (Design Framework)

**Status:** Alpha Test Readiness

- **Changed:** Facet naming to **VITALIS · MOTUS · SENSUS · VERBUM · ANIMA**5.
    
- **Added:** Added the critical separation between **Maximum Essence ($\mathbf{E_{max}}$)** and **Current Essence ($\mathbf{E_{cur}}$)**6.
    
- **Added:** Added the **Waning Scale**, where low $\mathbf{E_{max}}$ grants **Efficiency ($\mathbf{A_{rate}}$)** bonuses7.
    
- **Added:** Added Hybrid Roll resolution ($\mathbf{E_P + E_S}$) and $\mathbf{E_{max}}$-mitigated Damage system8.
    
- **Added:** Added Multilingual support (PT-PT / EN-US) and sheet automation logic9.
    

---

## [v0.3] — 2025-10-26 (Attrition Scope Refinement)

**Status:** Alpha Test Readiness

- **Removed:** Removed Attrition cost ($\mathbf{E_{cur}}$) for most actions outside of combat (e.g., Social, Investigation)10.
    
- **Added:** Added Fixed Cost rule of **$\mathbf{2\%}$** for extreme stress situations outside of combat11.
    
- **Added:** Added **Symmetric Penalty ($\mathbf{10}$)** for NPCs, rewarding the player's narrative/tactical bonus in contested rolls12.
    

---

## [v0.4] — 2025-10-26 (Final Progress Loop)

**Status:** Alpha Test Ready

- **Removed:** Removed the **Decay Milestone Scarring** and 10% Reallocation rules (obsolete)13.
    
- **Changed:** Altered the rule for progression and decay to **The Waning Roll**14.
    
- **Changed:** Proficiency Choice rolls $\mathbf{4\text{d}6}$ (higher decay risk) in exchange for permanent **$\mathbf{2\text{d}10}$ Proficiency Dice ($\mathbf{D_{prof}}$)**15.
    
- **Fixed:** Fixed game title to **Nárëquenta — Tales of the Waning**16.
    

---

## [v0.5] — 2025-10-27 (Attack Rolls & Contested Combat)

**Status:** Alpha Test Ready - Core Combat Loop Defined

- **Changed:** The entire Action Resolution system now defaults to **Contested Rolls**17.
    
- **Added:** **Proficiency Tiers and Dice Mapping** that tie $\mathbf{E_{max}}$ decay to $\mathbf{D_{prof}}$ acquisition18.
    
- **Changed:** **Waning Roll** is now the primary mechanism for converting $\mathbf{E_{max}}$ loss into $\mathbf{D_{prof}}$19.
    
- **Added:** Added **Critical Outcomes** system (Double Critical, Reversal) and **Proficiency Mitigation** ($\mathbf{D_{prof}}$ subtracts from $\mathbf{d100}$)20.
    
- **Added:** Added **Special Attacks** by trading $\mathbf{D_{prof}}$21.
    

---

## [v0.7] — 2025-11-14 (Precision Lethality & Tier-Neutral Balance)

**Status:** Alpha Test Ready - Core Ruleset Finalized

- **Changed:** Version increased from v0.5 to v0.7 due to the **complete restructuring of progression and combat**22.
    
- **Added:** **Initial Erosion ($\mathbf{1\text{d}10}$)** added for all Essences at character creation23.
    
- **Added:** **Maximum Limit ($\mathbf{50\%}$)** added for $\mathbf{E_{max}}$, defining the permanent success ceiling24.
    
- **Changed:** The **Proficiency Tier Table** was altered to **Uniform Progression ($\mathbf{1\text{d}10}$ per Tier)**, simplifying the scale and increasing power25.
    
- **Changed:** The role of $\mathbf{D_{prof}}$ was **Unified** for: 1) Error Mitigation, 2) Attrition Reduction, and 3) **Additive Base Damage ($\mathbf{R_{prof}}$)**26.
    
- **Added:** Added the **Additive Damage Formula** (Precision Lethality): $\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right)$27.
    
- **Added:** Added the **Defensive Tier Advantage Multiplier ($\mathbf{M_{DTA}}$)** to reduce damage from lower-Tier enemies ($\Delta T \ge 1$)28.
    
- **Added:** Added **Action Surge (AS) Progression**, linking the number of available Action Surges to the Proficiency Tier (up to 4 AS at Tier V)29.
    
- **Changed:** The **Attrition Cost** was mitigated and simplified to: $\mathbf{E_{cur} \text{ Loss}} = \max \left( 0, (7 - R_{prof}) \right)$30.
    
- **Added:** Added the rule of **Motor/Quality Essence Pairs** to determine which $\mathbf{E_{cur}}$ pools are spent in combat31.
    

---

## **[v0.8] — 2025-11-15 (SPA Migration & Launcher Stabilization)**

**Status:** Alpha Test Ready - Architecture Stabilized

- **Added:** Implementation of the **Single Page Application (SPA)** architecture in `index.html`, unifying the three sheets (`PC`, `NPC`, `GM_REF`) into a single page.
    
- **Added:** Full integration of the **Damage Calculator** into the GM Reference section (`index.html`).
    
- **Added:** All GM Reference headers and descriptions now support **Multilingual Localization** (`data-lang`).
    
- **Removed:** Obsolete HTML files (`pc_sheet.html`, `npc_sheet.html`, `gm_reference.html`).
    
- **Changed:** Sheet navigation was migrated from page _reload_ to **internal JavaScript view transitions** (`showSheet()`), eliminating threading _glitches_ and increasing application stability.
    
- **Fixed:** Corrected the calculation of the **root path** (_root_dir_) in the Python _launcher_ (`sheet_gui.py`) to resolve the fatal path duplication error when loading JSON localization files.
    
- **Fixed:** Corrected the path mapping logic and error handling of the `pywebview` API for the language selector, ensuring robust language initialization.
    

---

🧾 Version Key

|**Type**|**Meaning**|
|---|---|
|**Added**|New feature or mechanic 32|
|**Changed**|Adjusted or rebalanced rule 33|
|**Removed**|Mechanic or file removed 34|
|**Fixed**|Correction or typo 35|

🪶 Credits

Design & Writing — Serelith Varn

System Development & Documentation — GPT-5 (Liora Vex Framework)

“We are remembered for how beautifully we burn out.” 36

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.

Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md37.

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
