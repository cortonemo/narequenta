![Repository Header Image](header_image.png)
# Nárëquenta — Tales of the Waning

**Version: v0.8-FINAL (Precision Lethality and SPA Stabilization)**
**Author:** Serelith Varn (cortonemo)
**License:** Nárëquenta Limited Open License (v0.1)

-----

## 💡 Core Philosophy: Attrition is Meaning

Nárëquenta is a TTRPG about **Beautiful Erosion**. Heroes start at their peak and gradually fade as they act and spend their Essence. Progression is the **defining of character through loss**.

**Core Axiom (v0.8):** Power is a finite resource. The real threat is the **Extinction of Essence**. **Proficiency Compensates for Decline**, allowing maximum impact with minimal capacity.

## ⚙️ System Summary (v0.8)

The game is built around Essence management, **Level-Neutral Damage**, and **Level-Based Mitigation**.

  * **E\_max (Maximum):** Has a **Hard Floor of 50%**. The reduction determines your **Proficiency Tier**.
  * **E\_cur (Current):** The usable energy. Defines the success threshold ($\mathbf{d100 \le E_{cur}}$).
  * **Damage:** Calculated using the **Additive Damage Formula** that privileges proficiency.
    $$\\mathbf{D\_{Final}} = \\max \\left( 0, (A\_{FP} - \\bar{M}*{Defense} + D*{Margin} + R\_{prof}) \\right) \\times M\_{DTA} \\text{}$$

  * **$\mathbf{M_{DTA}}$ Multiplier:** The **Complete $\mathbf{M_{DTA}}$ Grid** was added and restructured in v0.8 to explicitly manage damage advantage/reduction based on the Tier difference.
  * **Architecture:** The sheet application was migrated to a **Single Page Application (SPA)**, unifying the PC, NPC, and GM references into a single `index.html` file.

## 🗂 Repository Contents

| Directory | Content | Status |
| :--- | :--- | :--- |
| **`/Rules/`** | The Core Mechanism, Metaphysics, and Rituals. | **v0.8 UPDATED** |
| **`/Playtest/`** | Sheets, scenarios, and quick references for the Alpha. | **v0.8 UPDATED** |
| **`/Tools/`** | Calculation scripts and utilities (e.g., Nárëquenta Calculator in Python). | **v0.8 UPDATED** |

-----

### 📜 License & Authorship

**© 2025 Serelith Varn**
This project is released under the **Nárëquenta Limited Open License (v0.1)**.
You are free to play, stream, and create fan content for this system—provided you give proper credit and do not use it commercially.

📜 [Read the full license →](LICENSE.md)