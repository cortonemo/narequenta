## ⚔️ Systematic Output: PC Sheet (v0.8 Update)

---
# GM Reference v0.9 (Decay Mitigation)
Finalized Draft — 2025-11-17

## SESSION FLOW
1. **Briefing / Setup:** Why this mission matters (and what they risk losing).
2. **Play Scenes:** Any meaningful action costs Essence ($\mathbf{E_{cur}}$) and is resolved with a **Contested Roll**.
- Player chooses the Motor ($\mathbf{E_{P}}$) and Quality ($\mathbf{E_{S}}$) Essences (see Core Rules for Pairs).
- Player uses $\mathbf{D_{prof}}$ for **Error Mitigation** ($\mathbf{R_{prof}}$ subtracts from the $\mathbf{d100}$ roll) and **Damage Base**.
- **Attrition Cost:** $\mathbf{E_{cur}}$ loss is calculated using the **$R_{prof}$ roll result** (Cost: $\max(0, 7 - R_{prof})$).

## RITUAL AND RECOVERY PHASE (v0.9)
- **Renewal (E_cur & AS):** Restores **$\mathbf{E_{cur}}$** to its current $\mathbf{E_{max}}$ value.
Also restores the **Action Surge (AS)** pool to the Tier-determined maximum (Tier V = **4 AS**).
- **Decay and Refinement (E_max):** This process happens **ONLY at the end of the Chapter** (Waning Roll).
- Prompt players to choose their Proficiency Focus (the **$\mathbf{2d6}$** risk).
- Roll Universal Decay ($\mathbf{1d6}$) and apply all losses, ensuring $\mathbf{E_{max}}$ never drops below **$50\%$**.

## PACING / TONE
- **Attrition is a Choice:** Never say, "You cannot do that". Say: "The cost is $\mathbf{X\%}$ loss from both [Motor] and [Quality]. Are you willing to burn that much?".
- **Tier Advantage (DTA):** Remember that the **Defensive Tier Advantage ($\mathbf{M_{DTA}}$)** automatically manages low-Tier vs. high-Tier encounters. The highly proficient PC (low $\mathbf{E_{max}}$) is defensively strong against weaker foes.
- **Lethality:** When Tiers are equal, combat is highly lethal ($\approx 46 \text{ HP}$ per hit). Be ready for quick, decisive outcomes based on critical margins.
- **Narrative Reward:** Reward creative and vivid descriptions by allowing the Attacker to gain advantage on the **$\mathbf{D_{prof}}$ roll** itself (e.g., re-roll one die), rather than modifying the final formula.
- **Treat the Ending as Sacred.** When all Facets hit $\mathbf{E_{cur}} = 0$, ask: how are they remembered?.

---

## VII. Proficiency Tiers and Mitigation Reference (v0.9)
The Tier is calculated from $\mathbf{E_{max}}$ loss.

| $\mathbf{E_{max}}$ Loss | Remaining $\mathbf{E_{max}}$ (%) |       Tier       | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Defense Mitigation) | **Action Surges (AS)** |
| :---------------------: | :------------------------------: | :--------------: | :-----------------: | :-------------------------------------: | :--------------------: |
|         $0-9\%$         |            $100-91\%$            |      **0**       |        None         |                  $0.0$                  |         **0**          |
|        $10-19\%$        |            $90-81\%$             |      **I**       |   $\mathbf{1d10}$   |                  $5.5$                  |         **1**          |
|        $20-29\%$        |            $80-71\%$             |      **II**      |   $\mathbf{2d10}$   |                 $11.0$                  |         **2**          |
|        $30-39\%$        |            $70-61\%$             |     **III**      |   $\mathbf{3d10}$   |                 $16.5$                  |         **3**          |
|        $40-49\%$        |            $60-51\%$             |      **IV**      |   $\mathbf{4d10}$   |                 $22.0$                  |         **4**          |
|     $\mathbf{50\%}$     |         $\mathbf{50\%}$          | **V (Pinnacle)** |   $\mathbf{5d10}$   |             $\mathbf{27.5}$             |      **5** (Max)       |

---

## VIII. Defensive Tier Advantage Multiplier ($\mathbf{M_{DTA}}$) Grid (v0.9)
The $\mathbf{M_{DTA}}$ is determined by the difference in Tiers ($\Delta T = T_{Defender} - T_{Attacker}$).

| Attacker Tier $\downarrow$ vs. Defender Tier $\rightarrow$ |            **I**            |          **II**           |          **III**          |          **IV**           |           **V**           |
| :--------------------------------------------------------: | :-------------------------: | :-----------------------: | :-----------------------: | :-----------------------: | :-----------------------: |
|                           **I**                            |  $\mathbf{1.00}$ (Neutral)  |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |      $\mathbf{0.25}$      | $\mathbf{0.25}$ (Capped)  |
|                           **II**                           |       $\mathbf{1.25}$       | $\mathbf{1.00}$ (Neutral) |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |      $\mathbf{0.25}$      |
|                          **III**                           |       $\mathbf{1.50}$       |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutral) |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |
|                           **IV**                           |       $\mathbf{1.75}$       |      $\mathbf{1.50}$      |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutral) |      $\mathbf{0.75}$      |
|                           **V**                            | $\mathbf{2.00}$ (Max Bonus) |      $\mathbf{1.75}$      |      $\mathbf{1.50}$      |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutral) |

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See [LICENSE.md](license.md).