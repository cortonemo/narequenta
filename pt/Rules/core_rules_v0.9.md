# 📜 Nárëquenta Regras Base v0.9 (Mitigação da Decadência)

## 1. O Que Este Jogo É 🧭

Nárëquenta é um TTRPG onde as heroínas começam perto do auge e terminam gastas. A progressão é a **definição da personagem através da perda**. O poder é um recurso finito. **A Proficiência Compensa o Declínio**.

---

## 2. Facetas do Eu (Essências) ✨

Cada personagem é definida por cinco Essências. Cada Essência começa a **$100\%$**, sujeita à Erosão Inicial.

- **VITALIS** — corpo, resistência, força, presença
- **MOTUS** — movimento, finesse, agilidade, graça
- **SENSUS** — perceção, instinto, foco, atenção
- **VERBUM** — intelecto, lógica, estrutura, discurso
- **ANIMA** — convicção, vontade, fé, sacrifício

### Valores de Essência

Cada Faceta tem:

- Um **Valor Atual ($\mathbf{E_{cur}}$)** (energia utilizável).
- Um **Valor Máximo ($\mathbf{E_{max}}$)** (limite permanente).
- **Limite:** $\mathbf{E_{max}}$ nunca pode descer abaixo de **$50\%$** (Piso Rígido).

### Erosão Inicial (Atualização v0.9)

Na criação de personagem, aplica-se a **Erosão Inicial**:

- Para cada uma das cinco Essências, lança $\mathbf{1d10}$. Este valor é subtraído de **$100\%$**, definindo o $\mathbf{E_{cur}}$ e o $\mathbf{E_{max}}$ iniciais.
- **Garantia de Tier I:** A jogadora pode designar uma Essência para ter o seu $\mathbf{E_{max}}$ definido exatamente em **$90\%$** após o lançamento, garantindo imediatamente o **Tier I** e $\mathbf{1d10}$ de $\mathbf{D_{prof}}$.

---

## 3. Agir no Mundo (Resolução de Ações: Letalidade de Precisão) 🎯

As ações são resolvidas como **Testes Opostos**.

### Fluxo de Resolução de Ações

- O limiar de sucesso é definido como: $\mathbf{d100 \le \mathbf{E_{cur}}}$.
- **O Atacante Mitiga:** o Atacante subtrai o seu Resultado de Proficiência ($\mathbf{R_{prof}}$) ao lançamento de $\mathbf{d100}$ (Mitigação de Erro).

### Custo de Atrição

O custo é aplicado à **Essência Motora ($\mathbf{E_{P}}$)** e à **Essência de Qualidade ($\mathbf{E_{S}}$)**.

- **Perda de $\mathbf{E_{P}}$ (Motor):** $\mathbf{D_{Loss} = \max \left(0, (7-R_{prof}) \right)}$.
- **Perda de $\mathbf{E_{S}}$ (Qualidade):** $1\%$ (Custo Fixo).

---

## 4. Ciclo de Refinamento (O Waning Roll) 🌘 (v0.9 Mitigação da Decadência)

Refinamento e Decadência ocorrem na conclusão de cada marco importante. O Tier de Proficiência é determinado pela perda total de $\mathbf{E_{max}}$.

### 4.1. A Escolha de Proficiência e o Waning Roll

- **Decadência Universal (Essências Não Escolhidas):**  
    $$\mathbf{1d6} \text{}$$  
    Lança um dado de seis faces e o resultado é subtraído de forma permanente a $\mathbf{E_{max}}$ (até ao Piso Rígido de $50\%$).
- **Foco de Refinamento (Essência Escolhida):**  
    $$\mathbf{2d6} \text{}$$  
    Lança dois dados de seis faces e o resultado é subtraído de forma permanente a $\mathbf{E_{max}}$, concedendo um aumento na Reserva de $\mathbf{D_{prof}}$ (Avanço de Tier).

### 4.2. Usar a Proficiência (Sistema de Tier Uniforme)

A reserva de $\mathbf{D_{prof}}$ é definida como:
$$\mathbf{1d10} \text{ por Tier}$$

---

## 5. Dano e Saúde (Letalidade Neutra em Relação ao Tier) 💥

Todas as personagens têm uma base de $100$ HP.

### Fórmula de Dano

$$\mathbf{D_{Final}} = \max \left(0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}$$

| **Componente** | **Fórmula** |
| :--- | :--- |
| **$\mathbf{A_{FP}}$ (Margem de Potencial Total)** | $\mathbf{100 - (d100-R_{prof})}$ |
| **$\mathbf{D_{Margin}}$ (Margem do Defensor)** | $\mathbf{d100_D-D_{Ecur}}$ |

---

## 6. Tiers de Proficiência e Multiplicadores $\mathbf{M_{DTA}}$ 🛡️

### Tiers de Proficiência (Correção de AS v0.9)

O Tier de Proficiência é determinado pelo $\mathbf{E_{max}}$ da Essência.

| Perda de $\mathbf{E_{max}}$ | $\mathbf{E_{max}}$ Restante (%) |       Tier       | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Mitigação Defensiva) | **Action Surges (AS)** |
| :-------------------------: | :-----------------------------: | :--------------: | :-----------------: | :--------------------------------------: | :--------------------: |
|          $0-9\%$            |           $100-91\%$            |      **0**       |        Nenhum       |                  $0.0$                  |         **0**          |
|         $10-19\%$           |            $90-81\%$            |      **I**       |   $\mathbf{1d10}$   |                  $5.5$                  |         **1**          |
|         $20-29\%$           |            $80-71\%$            |      **II**      |   $\mathbf{2d10}$   |                 $11.0$                  |         **2**          |
|         $30-39\%$           |            $70-61\%$            |     **III**      |   $\mathbf{3d10}$   |                 $16.5$                  |         **3**          |
|         $40-49\%$           |            $60-51\%$            |      **IV**      |   $\mathbf{4d10}$   |                 $22.0$                  |         **4**          |
|      $\mathbf{50\%}$        |         $\mathbf{50\%}$         | **V (Pinnacle)** |   $\mathbf{5d10}$   |             $\mathbf{27.5}$             |        5 (Máx)         |

### Multiplicador de Vantagem de Tier ($\mathbf{M_{DTA}}$)

| Tier do Atacante $\downarrow$ vs. Tier do Defensor $\rightarrow$ | **I** | **II** | **III** | **IV** | **V** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **I**   | $\mathbf{1.00}$ (Neutro)    | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ | $\mathbf{0.25}$ |
| **II**  | $\mathbf{1.25}$             | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ | $\mathbf{0.50}$ | $\mathbf{0.25}$ |
| **III** | $\mathbf{1.50}$             | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ | $\mathbf{0.50}$ |
| **IV**  | $\mathbf{1.75}$             | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutro) | $\mathbf{0.75}$ |
| **V**   | $\mathbf{2.00}$ (Bónus Máximo) | $\mathbf{1.75}$ | $\mathbf{1.50}$ | $\mathbf{1.25}$ | $\mathbf{1.00}$ (Neutro) |

---

## 7. Recuperação e Fim de Jogo ⏳

- **Fase de Recuperação:** repõe $\mathbf{E_{cur}}$ até ao valor atual de $\mathbf{E_{max}}$.
- **Progressão de Action Surge:** a reserva de AS escala com o Tier, até 5 AS.
- **Fim de Jogo:** a campanha é o registo de **como escolheste desvanecer**.

---

## 8. Fim do Jogo

No fim, retiras-te esvaziado e lendário.

A campanha é o registo de **como escolheste desvanecer**.

---

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.  
Licenciado para jogo não comercial e conteúdo de fãs ao abrigo da Nárëquenta Limited Open License (v0.1). Ver [LICENSE.md](license.md).

---

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See ICENSE.md](license.md).


© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.
