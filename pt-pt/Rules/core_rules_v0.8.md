# 📜 Nárëquenta Regras Base v0.8 (Suplemento de Vantagem de Tier)

## 1. O Que É Este Jogo 🧭

Nárëquenta é um TTRPG em que os heróis começam perto do auge e terminam gastos.  
As personagens começam definidas pela sua **Erosão** inicial.  
Não sobem de nível.  
São lembradas pela forma como se queimaram, de forma bela.

Não estás a tentar sobreviver para sempre.  
Estás a decidir que partes de ti valem a pena ser gastas antes de partires.

---

## 2. Facetas do Eu (Essências) ✨

Cada personagem é definida por cinco Essências. Cada Essência começa em **$100\%$**, sujeita à Erosão Inicial.

- **VITALIS** — corpo, resistência, força, presença
- **MOTUS** — movimento, finesse, agilidade, graça
- **SENSUS** — perceção, instinto, foco, atenção
- **VERBUM** — intelecto, lógica, estrutura, discurso
- **ANIMA** — convicção, vontade, fé, sacrifício

### Valores de Essência

Cada Faceta tem:

- Um **Valor Atual ($\mathbf{E_{cur}}$)**  
  Quanto dessa parte de ti ainda é utilizável neste momento.

- Um **Valor Máximo ($\mathbf{E_{max}}$)**  
  O teto até ao qual pode ser restaurada.

- **Limite:** $\mathbf{E_{max}}$ nunca pode descer abaixo de **$50\%$**.

### Erosão Inicial

Na criação de personagem, aplica-se a **Erosão Inicial**:

- Para cada uma das cinco Essências, escolhes sobre quais queres rolar, sujeitando-as à perda inicial.
- Rola $\mathbf{1d10}$ para cada Essência escolhida.
- Esse valor é subtraído de **$100\%$**.
- O resultado define tanto o **Valor Atual ($\mathbf{E_{cur}}$)** como o **Valor Máximo ($\mathbf{E_{max}}$)** iniciais dessa Essência.

---

## 3. Agir no Mundo (Resolução de Ações: Letalidade de Precisão) 🎯

As ações são resolvidas como **Jogadas Contestadas**.  
Só o Atacante utiliza $\mathbf{D_{prof}}$ para gerar impacto ofensivo.

### Fluxo de Resolução de Ações

- O limiar de sucesso é definido como:

  $$
  \mathbf{d100 \le \mathbf{E_{cur}}} \text{}
  $$

  O lançamento do dado de cem faces tem de ser menor ou igual ao Valor Atual da Essência.

- **Lançamento do Atacante:**  
  A (Atacante) rola $\mathbf{d100}$ e os seus **Dados de Proficiência ($\mathbf{D_{prof}}$)**.  
  A soma dos Dados de Proficiência é $\mathbf{R_{prof}}$.

- **Mitigação do Atacante:**  
  A **subtrai $\mathbf{R_{prof}}$ ao resultado do $\mathbf{d100}$** (Mitigação de Erro).  
  Se o resultado final for $\le \mathbf{E_{cur}}$ do Atacante, o ataque acerta.

- **Lançamento do Defensor:**  
  D (Defensor) rola $\mathbf{d100 \le \mathbf{E_{cur}}}$ para determinar a **Margem do Defensor ($\mathbf{D_{Margin}}$)** (Sec. 6).

### Custo de Atrito

O custo é aplicado à **Essência Motora ($\mathbf{E_{P}}$)** e à **Essência de Qualidade ($\mathbf{E_{S}}$)**.

- Perda de $\mathbf{E_{P}}$ (Motor):

  $$
  \mathbf{D_{Loss} = \max \left(0, (7-R_{prof}) \right)} \text{}
  $$

  A perda é o valor máximo entre zero e o resultado de sete menos a Jogada de Proficiência do Atacante ($\mathbf{R_{prof}}$).

  - Esta perda paga o custo mitigado.

| Cenário                         | Exemplo de $\mathbf{R_{prof}}$ | Cálculo                                      | Perda resultante de $\mathbf{E_{P}}$ |
| :----------------------------- | :----------------------------- | :------------------------------------------- | :----------------------------------: |
| **Perda Elevada** (Baixa Perícia) | **3** (ex., lançamento de Tier I)  | $\max(0, (7 - 3)) = 4$                       |             **$4\%$**               |
| **Perda Mitigada** (Muita Perícia) | **18** (ex., lançamento de Tier IV) | $\max(0, (7 - 18)) = 0$<br>$\max(0, -11) = 0$ |             **$0\%$**               |

- **Perda de $\mathbf{E_{S}}$ (Qualidade):** $1\%$  
  Paga um custo fixo pequeno.

---

## 4. Ciclo de Refinamento (The Waning Roll) 🌘

Refinamento e Decadência ocorrem no final de cada marco maior.  
O **Tier de Proficiência** é determinado pela perda total de $\mathbf{E_{max}}$.

### 4.1. A Escolha de Proficiência e o Waning Roll

- Essências Não Escolhidas:

  $$
  \mathbf{2d6} \text{}
  $$

  Rola dois dados de seis faces, e o resultado é permanentemente subtraído de $\mathbf{E_{max}}$.

- Essência Escolhida (Foco):

  $$
  \mathbf{4d6} \text{}
  $$

  Rola quatro dados de seis faces, e o resultado é permanentemente subtraído de $\mathbf{E_{max}}$, concedendo um aumento na Pool de $\mathbf{D_{prof}}$.

### 4.2. Uso da Proficiência (Sistema Uniforme de Tiers)

A $\mathbf{D_{prof}}$ obtida é convertida numa pool de:

$$
\mathbf{1d10} \text{ por Tier}
$$

Um dado de dez faces por Tier de Proficiência (máx. $\mathbf{5d10}$ no Tier V).

---

## 5. Dano e Saúde (Letalidade Neutra em Relação ao Tier) 💥

Todas as personagens têm uma base de $100$ HP.

### Fórmula de Dano

O dano é calculado usando a Margem de Potencial Total do Atacante ($\mathbf{A_{FP}}$) e modificado pela Vantagem de Tier do Defensor ($\mathbf{M_{DTA}}$).

$$
\mathbf{D_{Final}} = \max \left(0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}
$$

O Dano Final é o valor máximo entre zero e a soma da Margem de Potencial Total, menos a Mitigação Média do Defensor, mais a Margem do Defensor, mais a Jogada de Proficiência do Atacante, tudo multiplicado pelo Multiplicador de Vantagem de Tier Defensiva.

| **Componente** | **Fórmula** | **Transcrição** |
| :--- | :--- | :--- |
| **$\mathbf{A_{FP}}$ (Full Potential Margin)** | $\mathbf{100 - (d100-R_{prof})}$ | Cem menos o resultado do lançamento de $\mathbf{d100}$ menos a Jogada de Proficiência ($\mathbf{R_{prof}}$). |
| **$\mathbf{D_{Margin}}$ (Defender Margin)** | $\mathbf{d100_D-D_{Ecur}}$ | O lançamento de $\mathbf{d100}$ do Defensor menos a Essência Atual do Defensor ($\mathbf{E_{cur}}$). |

---

### Exemplos Numéricos para os Componentes de Dano

Para calcular $\mathbf{D_{Final}}$, usamos os seguintes valores fixos de cenário:

* **$\mathbf{R_{prof}}$ do Atacante (Dano Aditivo):** **15** (resultado de $3\text{d}10$).
* **Lançamento de $\mathbf{d100}$ do Atacante:** **50**.
* **Tier do Defensor:** III.
* **$\mathbf{\bar{M}_{Defense}}$ do Defensor (Mitigação Média):** **16.5**.
* **$\mathbf{E_{cur}}$ do Defensor:** **70%**.
* **Lançamento de $\mathbf{d100_D}$ do Defensor:** **80**.
* **$\mathbf{M_{DTA}}$:** **1.0** (Assumindo Atacante TIII vs. Defensor TIII, sem Vantagem de Tier).

#### A. Margem de Potencial Total do Atacante ($\mathbf{A_{FP}}$)

Este valor representa o poder inerente do Atacante com base em quão bem mitigou o seu próprio lançamento de $\mathbf{d100}$.

$$
\mathbf{A_{FP}} = \mathbf{100 - (50 - 15)}
$$
$$
\mathbf{A_{FP}} = 100 - 35 = \mathbf{65}
$$

* **Interpretação:** O Atacante acerta com uma Margem de Potencial Total de **65**.

#### B. Margem do Defensor ($\mathbf{D_{Margin}}$)

Este valor determina se o Defensor defendeu com sucesso ($\mathbf{D_{Margin}}$ negativo) ou falhou na defesa ($\mathbf{D_{Margin}}$ positivo).

$$
\mathbf{D_{Margin}} = \mathbf{80 - 70}
$$
$$
\mathbf{D_{Margin}} = \mathbf{+10}
$$

* **Interpretação:** O Defensor falhou o lançamento ($80 > 70$), resultando numa Margem positiva de **+10**, que aumenta o dano sofrido.

#### C. Cálculo do Dano Final ($\mathbf{D_{Final}}$)

Colocamos tudo na fórmula principal:

$$
\mathbf{D_{Final}} = \max \left(0, (65 - 16.5 + 10 + 15) \right) \times 1.0
$$
$$
\mathbf{D_{Final}} = \max \left(0, (73.5) \right) \times 1.0
$$
$$
\mathbf{D_{Final}} = \mathbf{73} \text{ HP (Arredondado para Baixo)}
$$

* **Interpretação:** O dano base foi 73 HP.  
  A falha do Defensor ($\mathbf{D_{Margin}} = +10$) aumentou o dano, mas a perícia inata do Defensor ($\mathbf{\bar{M}_{Defense}} = 16.5$) conseguiu reduzi-lo a partir do potencial máximo do Atacante.

---

## 6. Tiers de Proficiência e Multiplicadores $\mathbf{M_{DTA}}$ 🛡️

### Tiers de Proficiência

O Tier de Proficiência é determinado pela $\mathbf{E_{max}}$ atual da Essência.  
$\mathbf{\bar{M}_{Defense}}$ é a Mitigação Média de $\mathbf{R_{prof}}$ do Defensor.

| $\mathbf{E_{max}}$ Perdida | $\mathbf{E_{max}}$ Restante (%) | Tier | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Mitigação Defensiva) | **Action Surges (AS)** |
| :--: | :---: | :--: | :--: | :--: | :--: |
| $0-9\%$   | $100-91\%$ | **0** | Nenhum     | $0.0$  | **0** |
| $10-19\%$ | $90-81\%$  | **I** | $\mathbf{1d10}$ | $5.5$  | **1** |
| $20-29\%$ | $80-71\%$  | **II** | $\mathbf{2d10}$ | $11.0$ | **2** |
| $30-39\%$ | $70-61\%$  | **III** | $\mathbf{3d10}$ | $16.5$ | **3** |
| $40-49\%$ | $60-51\%$  | **IV** | $\mathbf{4d10}$ | $22.0$ | **4** |
| $\mathbf{50\%}$ | $\mathbf{50\%}$ | **V (Pinnacle)** | $\mathbf{5d10}$ | $\mathbf{27.5}$ | **5** |

### Multiplicador de Vantagem de Tier ($\mathbf{M_{DTA}}$) – Suplemento v0.8

O multiplicador $\mathbf{M_{DTA}}$ agora cobre tanto **redução de dano** (Vantagem Defensiva) como **aumento de dano** (Vantagem Ofensiva), com base na diferença de Tier.

#### Vantagem de Tier Defensiva (Referência: Atacante Tier I)

| **Tier do Atacante** | **Tier do Defensor** | **Diferença de Tier (ΔT)** | **$\mathbf{M_{DTA}}$ (Redução)** |
| :---------------: | :---------------: | :----------------------: | :------------------------------: |
| **I** | **I**   | $\mathbf{0}$  | $\mathbf{1.00}$ |
| **I** | **II**  | $\mathbf{+1}$ | $\mathbf{0.75}$ |
| **I** | **III** | $\mathbf{+2}$ | $\mathbf{0.50}$ |
| **I** | **IV**  | $\mathbf{+3}$ | $\mathbf{0.25}$ |
| **I** | **V**   | $\mathbf{+4}$ | $\mathbf{0.25}$ (Capado) |

#### Vantagem de Tier Ofensiva (Referência: Atacante Tier V)

| **Tier do Atacante** | **Tier do Defensor** | **Diferença de Tier (ΔT)** | **$\mathbf{M_{DTA}}$ (Bónus Ofensivo)** |
| :---: | :---: | :---: | :---: |
| **V** | **V**   | $\mathbf{0}$   | $\mathbf{1.00}$ |
| **V** | **IV**  | $\mathbf{-1}$  | $\mathbf{1.25}$ |
| **V** | **III** | $\mathbf{-2}$  | $\mathbf{1.50}$ |
| **V** | **II**  | $\mathbf{-3}$  | $\mathbf{1.75}$ |
| **V** | **I**   | $\mathbf{-4}$  | $\mathbf{2.00}$ |

## ⚔️ Grelha Completa de $\mathbf{M_{DTA}}$ (Atacante vs. Defensor)

O valor de $\mathbf{M_{DTA}}$ é determinado pela diferença de Tiers ($\Delta T = T_{Defensor} - T_{Atacante}$).  
Valores abaixo de $1.00$ são **Reduções Defensivas**, valores acima de $1.00$ são **Bónus Ofensivos**.

| Tier do Atacante $\downarrow$ vs. Tier do Defensor $\rightarrow$ | **I** ($\mathbf{E_{max}} \mathbf{90-81\%}$) | **II** ($\mathbf{E_{max}} \mathbf{80-71\%}$) | **III** ($\mathbf{E_{max}} \mathbf{70-61\%}$) | **IV** ($\mathbf{E_{max}} \mathbf{60-51\%}$) | **V** ($\mathbf{E_{max}} \mathbf{50\%}$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **I**   | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ | $\mathbf{0.25}$ (Capado) |
| **II**  | $\mathbf{1.25}$          | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ |
| **III** | $\mathbf{1.50}$          | $\mathbf{1.25}$          | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ | $\mathbf{0.50}$ |
| **IV**  | $\mathbf{1.75}$          | $\mathbf{1.50}$          | $\mathbf{1.25}$          | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ |
| **V**   | $\mathbf{2.00}$ (Bónus Máx.) | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutro) |

Esta tabela completa de $\mathbf{M_{DTA}}$ fornece o multiplicador para qualquer combinação de Tier de Atacante vs. Defensor, com base na regra progressiva estabelecida.

## ⚔️ Exemplos Numéricos de $\mathbf{M_{DTA}}$

Usamos o componente fixo de dano do exemplo anterior:

* **Soma Base de Dano (Antes de $\mathbf{M_{DTA}}$):**  
  $A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof} = 36 \text{ (assumido para exemplo limpo)}$.

| Caso | Cenário | $\Delta T$ ($T_{Def} - T_{Att}$) | $\mathbf{M_{DTA}}$ (Multiplicador) | Cálculo de $\mathbf{D_{Final}}$ | Resultado de $\mathbf{D_{Final}}$ |
| :----- | :--------------------------------------------------------------- | :------------------------------- | :------------------------------ | :------------------------------- | :------------------------------ |
| **1.** | **Bónus Ofensivo Máximo** (PC de Nível 5 ataca Goblin de Nível 1) | $\mathbf{-4}$ | $\mathbf{2.00}$ | $36 \times 2.00$  | **72 HP** |
| **2.** | **Combate Neutro** (Atacante de Nível 2 ataca Defensor de Nível 2) | $\mathbf{0}$ | $\mathbf{1.00}$ | $36 \times 1.00$  | **36 HP** |
| **3.** | **Mitigação Defensiva Máxima** (Goblin de Nível 1 ataca PC de Nível 4) | $\mathbf{+3}$ | $\mathbf{0.25}$ | $36 \times 0.25$ | **9 HP**  |

---

## 7. Recuperação e Fim de Jogo ⏳

* A **Fase de Recuperação** restaura $\mathbf{E_{cur}}$ até ao valor atual de $\mathbf{E_{max}}$.
* **Progressão de Action Surge:**  
  A pool de AS (que concede ataques/ações extra por ciclo de Recuperação) escala com o Tier, compensando o teto baixo de $\mathbf{E_{max}}$.  
  (O Tier V concede 5 AS).
* **Sobrevivência:**  
  Nas fases tardias, as tuas Eficiências e a tua $\mathbf{D_{prof}}$ tornam-te incrivelmente letal, apesar do teto baixo de $\mathbf{E_{cur}}$.


---

## 8. Fim do Jogo

No fim, retiras-te esgotado e lendário.

A campanha é o registo de **como escolheste desvanecer**.

---
© 2025 Serelith Varn — Nárëquenta: Contos do Esvanecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte [LICENSE.md](license.md).


© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
