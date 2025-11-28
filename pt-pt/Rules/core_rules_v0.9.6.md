# 📜 Nárëquenta Regras Base v0.9.6 (Letalidade de Precisão)

## 1. O Que É Este Jogo 🧭
Nárëquenta é um TTRPG onde os heróis começam perto do seu auge e terminam gastos. A progressão é a **definição da personagem através da perda**. O poder é um recurso finito. **A Proficiência Compensa o Declínio**.

---

## 2. Facetas do Eu (Essências) ✨
Cada personagem é definida por cinco Essências. [cite_start]Cada Essência começa a **$100\%$**, sujeita à Erosão Inicial[cite: 2488].

- **VITALIS** — corpo, resistência, força, presença
- **MOTUS** — movimento, finesse, agilidade, graça
- **SENSUS** — perceção, instinto, foco, atenção
- **VERBUM** — intelecto, lógica, estrutura, discurso
- **ANIMA** — convicção, vontade, fé, sacrifício

### Valores de Essência
- **Pico da Alma ($\mathbf{E_{max}}$):** Limite permanente. [cite_start]Nunca pode descer abaixo de **$50\%$** (Piso Rígido)[cite: 2489].
- **Vigor Ativo ($\mathbf{E_{cur}}$):** Energia utilizável. Determina a tua **Zona de Tensão**.

---

## 3. Resolução de Ações: A Rolagem Efetiva 🎯

[cite_start]O sucesso é determinado comparando a **Rolagem Efetiva** contra o Potencial Permanente ($\mathbf{E_{max}}$), ajustado pela fadiga[cite: 2497].

### A. A Fórmula da Rolagem Efetiva
$$\mathbf{R_{Eff}} = \mathbf{d100} - \mathbf{R_{prof}}$$
A Rolagem Efetiva é igual ao Dado de Caos ($\mathbf{d100}$) menos o Resultado de Perícia ($\mathbf{R_{prof}}$).

### B. O Teste de Sucesso
$$\mathbf{R_{Eff}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalidade}})$$
[cite_start]A ação é bem-sucedida se a Rolagem Efetiva for menor ou igual ao teu $\mathbf{E_{max}}$ menos a **Penalidade de Zona** atual[cite: 2502].

### C. Zonas de Tensão ($\mathbf{E_{cur}}$)
[cite_start]À medida que $\mathbf{E_{cur}}$ se esgota, cais em Zonas mais baixas, aumentando a dificuldade das ações[cite: 2504].

| Intervalo $\mathbf{E_{cur}}$ | Nome da Zona | Penalidade ($\mathbf{Z_{Penalidade}}$) |
| :--- | :--- | :--- |
| **100% – 76%** | **Pico** | **-0** |
| **75% – 51%** | **Minguante** | **-10** |
| **50% – 26%** | **Desvanecente** | **-20** |
| **25% – 0%** | **Vazio** | **-30** |

---

## 4. Atrição: O Custo da Ação 🩸
Cada ação queima Essência. [cite_start]O custo deriva do **Peso do Item** e é mitigado pela **Perícia**[cite: 2526].

### Fórmula de Atrição
$$\mathbf{Custo} = \max \left( 0, \mathbf{Peso} - \left\lfloor \frac{\mathbf{R_{prof}}}{2} \right\rfloor \right)$$
[cite_start]O Custo de Energia (perda de $\mathbf{E_{cur}}$) é igual ao Peso da Arma menos metade da Rolagem de Proficiência (arredondado para baixo)[cite: 2528].

| Classe de Peso | Custo Base | Exemplos |
| :--- | :--- | :--- |
| **Leve** | **10%** | [cite_start]Adagas, Arcos Curtos [cite: 2531] |
| **Médio** | **15%** | [cite_start]Espadas, Dardos [cite: 2532] |
| **Pesado** | **20%** | [cite_start]Maças, Bestas Pesadas [cite: 2533] |

* [cite_start]**Sucesso Crítico (1-5):** Reduz para metade o Custo final[cite: 2534].
* [cite_start]**Falha Crítica (96-100):** Duplica o Custo final[cite: 2535].

---

## 5. Combate: Letalidade de Precisão ($\mathbf{D_{Final}}$) 💥
O cálculo de dano privilegia a Perícia ($\mathbf{R_{prof}}$). Mesmo se bloqueado, a força da perícia atravessa (O Piso Rígido).

### Fórmula de Dano Final
$$\mathbf{D_{Final}} = \max \left( \mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Def}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}}) \right) \times \mathbf{M_{DTA}}$$

| Componente | Definição |
| :--- | :--- |
| **$\mathbf{R_{prof}}$ (Piso Rígido)** | [cite_start]O dano mínimo absoluto é o teu resultado de Proficiência[cite: 2518]. |
| **$\mathbf{A_{FP}}$ (Potencial Total)** | $\mathbf{100 - (d100 - R_{prof})}$. [cite_start]O quão próximo o ataque esteve da perfeição[cite: 2513]. |
| **$\mathbf{\bar{M}_{Def}}$ (Mitigação)** | [cite_start]A armadura passiva do Defensor (Nível $\times$ 5.5)[cite: 2523]. |
| **$\mathbf{D_{Margin}}$ (Vulnerabilidade)** | Rolagem de Defesa do Defensor menos $\mathbf{E_{cur}}$. [cite_start]Valores positivos aumentam o dano[cite: 2524]. |

---

## 6. Progressão: A Rolagem do Esvanecer 🌘
A progressão ocorre em marcos narrativos ao reduzir permanentemente $\mathbf{E_{max}}$ para avançar Níveis de Proficiência.

- **Decadência Universal (Não-Escolhida):** Rola **1d6**. Subtrai a $\mathbf{E_{max}}$.
- **Foco de Refinamento (Escolhida):** Rola **2d6**. Subtrai a $\mathbf{E_{max}}$ para ganhar $\mathbf{D_{prof}}$.

### Níveis de Proficiência
| $\mathbf{E_{max}}$ Restante | Nível | Reserva $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Mitigação) |
| :--- | :--- | :--- | :--- |
| 90% – 81% | I | **1d10** | 5.5 |
| 80% – 71% | II | **2d10** | 11.0 |
| 70% – 61% | III | **3d10** | 16.5 |
| 60% – 51% | IV | **4d10** | 22.0 |
| **50%** | **V** | **5d10** | 27.5 |

---
© 2025 Serelith Varn — Nárëquenta. Licenciado sob Nárëquenta Limited Open License (v0.1).


© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
