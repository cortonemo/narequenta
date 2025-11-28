# 📜 Nárëquenta Core Rules v0.9.6 (Precision Lethality)

## 1. What This Game Is 🧭
Nárëquenta is a TTRPG where heroes begin near their peak and end spent. Progression is the **defining of character through loss**. Power is a finite resource. [cite_start]**Proficiency Compensates for Decline**[cite: 2476, 2477].

---

## 2. Facets of the Self (Essences) ✨
Each character is defined by five Essences. [cite_start]Each Essence starts at **$100\%$**, subject to Initial Erosion[cite: 2488].

- **VITALIS** — body, endurance, force, presence
- **MOTUS** — movement, finesse, agility, grace
- **SENSUS** — awareness, instinct, focus, perception
- **VERBUM** — intellect, logic, structure, speech
- **ANIMA** — conviction, will, faith, sacrifice

### Essence Values
- **Maximum Value ($\mathbf{E_{max}}$):** Permanent limit. [cite_start]Can never drop below **$50\%$** (Hard Floor)[cite: 2489].
- **Current Value ($\mathbf{E_{cur}}$):** Usable energy. Determines your **Zone of Strain**.

---

## 3. Action Resolution: The Effective Roll 🎯

[cite_start]Success is determined by comparing the **Effective Roll** against the Permanent Capacity ($\mathbf{E_{max}}$), adjusted by fatigue[cite: 2497].

### A. The Effective Roll Formula
$$\mathbf{R_{Eff}} = \mathbf{d100} - \mathbf{R_{prof}}$$
[cite_start]The Effective Roll equals the Chaos Die ($\mathbf{d100}$) minus the Skill Result ($\mathbf{R_{prof}}$)[cite: 2499].

### B. The Success Check
$$\mathbf{R_{Eff}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalty}})$$
[cite_start]The action succeeds if the Effective Roll is less than or equal to your $\mathbf{E_{max}}$ minus the current **Zone Penalty**[cite: 2502].

### C. Zones of Strain ($\mathbf{E_{cur}}$)
[cite_start]As $\mathbf{E_{cur}}$ depletes, you fall into lower Zones, increasing the difficulty of actions[cite: 2504].

| $\mathbf{E_{cur}}$ Range | Zone Name | Penalty ($\mathbf{Z_{Penalty}}$) |
| :--- | :--- | :--- |
| **100% – 76%** | **Peak** | **-0** |
| **75% – 51%** | **Waning** | **-10** |
| **50% – 26%** | **Fading** | **-20** |
| **25% – 0%** | **Hollow** | **-30** |

---

## 4. Attrition: The Cost of Action 🩸
Every action burns Essence. [cite_start]The cost is derived from the **Item Weight** and mitigated by **Skill**[cite: 2526].

### Attrition Formula
$$\mathbf{Cost} = \max \left( 0, \mathbf{Weight} - \left\lfloor \frac{\mathbf{R_{prof}}}{2} \right\rfloor \right)$$
[cite_start]The Energy Cost ($\mathbf{E_{cur}}$ loss) equals the Weapon Weight minus half of the Proficiency Roll (rounded down)[cite: 2528].

| Weight Class | Base Cost | Examples |
| :--- | :--- | :--- |
| **Light** | **10%** | [cite_start]Daggers, Shortbows [cite: 2531] |
| **Medium** | **15%** | [cite_start]Swords, Javelins [cite: 2532] |
| **Heavy** | **20%** | [cite_start]Mauls, Arbalests [cite: 2533] |

* [cite_start]**Critical Success (1-5):** Halve the final Cost[cite: 2534].
* **Critical Failure (96-100):** Double the final Cost[cite: 2535].

---

## 5. Combat: Precision Lethality ($\mathbf{D_{Final}}$) 💥
Damage calculation privileges Skill ($\mathbf{R_{prof}}$). Even when blocked, the force of skill carries through (The Hard Floor)[cite: 2516].

### Final Damage Formula
$$\mathbf{D_{Final}} = \max \left( \mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Def}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}}) \right) \times \mathbf{M_{DTA}}$$

| Component | Definition |
| :--- | :--- |
| **$\mathbf{R_{prof}}$ (Hard Floor)** | [cite_start]The absolute minimum damage is your Proficiency Roll result[cite: 2518]. |
| **$\mathbf{A_{FP}}$ (Full Force Potential)** | $\mathbf{100 - (d100 - R_{prof})}$. [cite_start]How close the attack was to perfection[cite: 2513]. |
| **$\mathbf{\bar{M}_{Def}}$ (Mitigation)** | [cite_start]The Defender's passive armor (Tier $\times$ 5.5)[cite: 2523]. |
| **$\mathbf{D_{Margin}}$ (Vulnerability)** | Defender's Defense Roll minus Defender's $\mathbf{E_{cur}}$. Positive values add damage[cite: 2524]. |

---

## 6. Progression: The Waning Roll 🌘
Progression occurs at narrative milestones by permanently reducing $\mathbf{E_{max}}$ to advance Proficiency Tiers[cite: 2492].

- **Universal Decay (Non-Chosen):** Roll **1d6**. Subtract from $\mathbf{E_{max}}$.
- **Refinement Focus (Chosen):** Roll **2d6**. Subtract from $\mathbf{E_{max}}$ to gain $\mathbf{D_{prof}}$.

### Proficiency Tiers
| Remaining $\mathbf{E_{max}}$ | Tier | $\mathbf{D_{prof}}$ Pool | $\mathbf{\bar{M}}$ (Mitigation) |
| :--- | :--- | :--- | :--- |
| 90% – 81% | I | **1d10** | 5.5 |
| 80% – 71% | II | **2d10** | 11.0 |
| 70% – 61% | III | **3d10** | 16.5 |
| 60% – 51% | IV | **4d10** | 22.0 |
| **50%** | **V** | **5d10** | 27.5 |

---
© 2025 Serelith Varn — Nárëquenta. Licensed under Nárëquenta Limited Open License (v0.1).
