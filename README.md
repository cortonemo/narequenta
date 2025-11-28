![Repository Header Image](header_image.png)
# Nárëquenta — Tales of the Waning (Foundry VTT)

**Version: v0.9.6 (Precision Lethality & Zones of Strain)**
**Author:** Serelith Varn (cortonemo)
**License:** Nárëquenta Limited Open License (v0.1)
**Compatibility:** Foundry VTT v11+

-----

## 💡 Core Philosophy: Attrition is Meaning

[cite_start]Nárëquenta is a TTRPG about **Beautiful Erosion**[cite: 2497]. Heroes start at their peak and gradually fade as they act and spend their Essence. [cite_start]Progression is the **defining of character through loss**[cite: 7].

[cite_start]**Core Axiom (v0.9.6):** Success becomes harder as you tire (Zones), but Skill ($R_{prof}$) guarantees minimum impact ($D_{Floor}$)[cite: 9].

## ⚙️ System Summary (v0.9.6)

The game is built around Essence management, **Zones of Strain**, and **Precision Lethality**.

* **Success Threshold:** Actions succeed if the **Effective Roll** is less than or equal to **Potential minus Fatigue**:
    [cite_start]$$\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Zone_{Penalty}})$$ [cite: 30, 33]

* **Zones of Strain:** As $\mathbf{E_{cur}}$ drops, penalties increase:
    * **Peak (100-76%):** -0
    * **Waning (75-51%):** -10
    * **Fading (50-26%):** -20
    * [cite_start]**Hollow (25-0%):** -30 [cite: 36-39]

* **Attrition:** The cost of action is derived from **Item Weight** and mitigated by Skill:
    [cite_start]$$Cost = \max(0, Weight - \lfloor R_{prof}/2 \rfloor)$$ [cite: 59]

* **Damage:** Calculated using the **Additive Damage Formula** with a hard skill floor:
    [cite_start]$$\mathbf{D_{Final}} = \max(R_{prof}, (A_{FP} - \bar{M}_{Def} + D_{Margin} + R_{prof})) \times M_{DTA}$$ [cite: 52]

## 🗂 Repository Contents

| Directory | Content | Status |
| :--- | :--- | :--- |
| **`/Rules/`** | The Core Mechanism, Metaphysics, and Rituals. | **v0.9.6 UPDATED** |
| **`/Playtest/`** | Sheets, scenarios, and quick references for the Alpha. | **v0.9.6 UPDATED** |
| **`/Tools/`** | Calculation scripts and utilities (e.g., Nárëquenta Calculator in Python). | **v0.9.6 UPDATED** |

-----

### 📦 Installation

1.  Open Foundry VTT.
2.  Go to **Game Systems** -> **Install System**.
3.  Paste the Manifest URL:
    `https://github.com/cortonemo/narequenta-vtt/releases/latest/download/system.json`
4.  [cite_start]Click **Install** [cite: 2504-2505].

-----

### 📜 License & Authorship

**© 2025 Serelith Varn**
This project is released under the **Nárëquenta Limited Open License (v0.1)**.
You are free to play, stream, and create fan content for this system—provided you give proper credit and do not use it commercially.
[cite_start]This software is based on the **Simple Worldbuilding System** by Atropos, used under the MIT License [cite: 2506-2508].

📜 [Read the full license →](LICENSE.md)
