# GM Reference v0.9.6 (Precision Lethality)

## I. SESSION FLOW
1. **Briefing:** Establish what they risk losing.
2. **Action Resolution:**
   - **Check:** $\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalty}})$.
   - **Attrition:** Action burns $\mathbf{E_{cur}}$ based on Item Weight (Light 10%, Med 15%, Hvy 20%) minus $\lfloor R_{prof}/2 \rfloor$.
3. **Zones of Strain:** Ensure players track their current Zone penalty.
   - **Peak (100-76%):** -0
   - **Waning (75-51%):** -10
   - **Fading (50-26%):** -20
   - **Hollow (25-0%):** -30 .

## II. COMBAT FORMULAS
**The Damage Floor:** Damage never drops below $\mathbf{R_{prof}}$ (before Tier Multiplier).

$$\mathbf{D_{Final}} = \max(\mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Def}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}})) \times \mathbf{M_{DTA}}$$

| Component | Formula / Value |
| :--- | :--- |
| **$\mathbf{A_{FP}}$** | $100 - (d100 - R_{prof})$ |
| **$\mathbf{D_{Margin}}$** | $Defense_{Roll} - Defender_{Ecur}$ |
| **$\mathbf{\bar{M}_{Def}}$** | $Defender_{Tier} \times 5.5$ |

## III. TIER ADVANTAGE MULTIPLIER ($\mathbf{M_{DTA}}$)
Based on $\Delta T = T_{Defender} - T_{Attacker}$.

| Attacker vs Defender | Multiplier |
| :--- | :--- |
| **Equal Tier** | **x 1.00** |
| **Defender +1 Tier** | **x 0.75** |
| **Defender +2 Tier** | **x 0.50** |
| **Attacker +1 Tier** | **x 1.25** |
| **Attacker +2 Tier** | **x 1.50** |

## IV. RECOVERY (RENEWAL)
- **Long Rest:** Restores $\mathbf{E_{cur}}$ to 100% (or current $\mathbf{E_{max}}$). It **does not** recover lost $\mathbf{E_{max}}$.
- **Waning Roll:** Happens at milestones. $\mathbf{1d6}$ (Universal) or $\mathbf{2d6}$ (Focus).

---

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). [Read the full license →](LICENSE.md)


© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
