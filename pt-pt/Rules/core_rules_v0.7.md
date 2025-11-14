## 📄 Nárëquenta Regras Base v0.7

Rascunho Finalizado — 2025-11-14

## 1. O Que É Este Jogo

Nárëquenta é um TTRPG onde os heróis começam perto do seu auge e acabam esgotados.

As personagens começam com força total em todos os aspetos de si mesmas.

Não ganham níveis.

São lembrados pela forma elegante como se desvanecem.

Não estás a tentar sobreviver para sempre.

Estás a decidir que partes de ti valem a pena gastar antes de partires.

---

## 2. Facetas do Ser (Essências)

Cada personagem é definida por cinco Facetas (Essências). Cada Faceta começa a **100%**, sujeita à Erosão Inicial.

- **VITALIS** — corpo, resistência, força, presença
    
- **MOTUS** — movimento, destreza, agilidade, graça
    
- **SENSUS** — consciência, instinto, foco, perceção
    
- **VERBUM** — intelecto, lógica, estrutura, discurso
    
- **ANIMA** — convicção, vontade, fé, sacrifício
    

Cada Faceta tem:

- Um **Valor Atual ($\mathbf{E_{cur}}$)** (quanto dessa parte de ti está utilizável neste momento).
    
- Um **Valor Máximo ($\mathbf{E_{max}}$)** (o limite até onde pode ser restaurado).
    - **Limite:** $\mathbf{E_{max}}$ nunca pode ser inferior a **$50\%$**.
    

Na criação de personagem:

- **Erosão Inicial:** Rola-se **$1d10$** para cada Essência. Este valor é subtraído de **$100\%$**, definindo os valores iniciais de $\mathbf{E_{cur}}$ e $\mathbf{E_{max}}$.
    

---

### 3. Agir no Mundo (Resolução de Ação: Letalidade de Precisão)

As Ações são resolvidas como **Rolagens Contestadas** onde a $\mathbf{E_{cur}}$ do Atacante e Defensor define o limiar de sucesso ($\mathbf{d100 \le \mathbf{E_{cur}}}$).

#### Fluxo de Resolução de Ação
1. **Atacante Rola:** A rola $\mathbf{d100}$ e os seus **Dados de Proficiência ($\mathbf{D_{prof}}$)**. O resultado da proficiência é $\mathbf{R_{prof}}$.
2. **Atacante Mitiga:** A rola os seus $\mathbf{D_{prof}}$ e **subtrai o $\mathbf{R_{prof}}$ da rolagem $\mathbf{d100}$**. Se o resultado for $\le$ à $\mathbf{E_{cur}}$ do Atacante, o ataque acerta.
3. **Defensor Rola:** D rola $\mathbf{d100 \le \mathbf{E_{cur}}}$ para determinar a **Margem do Defensor ($\mathbf{D_{Margin}}$)**.
4. **Cálculo de Dano:** O dano final é calculado pela **Fórmula de Dano Aditiva** (Secção 6).

#### Custo de Atrição
1. **Pares de Essência:** O jogador escolhe uma **Essência Motor ($\mathbf{E_{P}}$)** e uma **Essência Qualidade ($\mathbf{E_{S}}$)**.
2. **Custos:** O custo é aplicado às duas Essências:
    - **$E_{P}$ Loss:** $\mathbf{D_{Loss} = \max \left( 0, (7 - R_{prof}) \right)}$
    - **$E_{S}$ Loss:** **$1\%$**
    - *Nota: A maioria das ações fora de combate não incorre em custos de Atrição.*

---

### 4. Ciclo de Refinamento e Decaimento (The Waning Roll)

Esta mecânica de **Erosão Permanente** ocorre no final de cada marco importante. O Nível de Proficiência é determinado pela perda total de $\mathbf{E_{max}}$ (consulte a Tabela de Tiers na documentação `rules_progression`).

#### A Escolha de Proficiência e Rolagem do Esvanecer
1. **Foco:** O jogador escolhe **uma (1)** Essência para Foco.
2. **Decaimento:** Aplica-se o Decaimento a todas as Essências, sujeito ao limite de $\mathbf{50\%}$:
    - **Essências Não Escolhidas:** $\mathbf{2\text{d}6}$ subtraídos permanentemente da $\mathbf{E_{max}}$.
    - **Essência Escolhida (Foco):** $\mathbf{4\text{d}6}$ subtraídos permanentemente da $\mathbf{E_{max}}$ (queima mais rápido), o que concede um aumento no **Pool de $\mathbf{D_{prof}}$**.

---

## 5. Progressão de Impulso de Ação (Action Surge)

O pool de Impulsos de Ação (AS) aumenta com o Tier de Proficiência, permitindo que o PC compense o limite de $\mathbf{E_{cur}}$ com atividade. (Consulte a Tabela de Progressão de AS na documentação `rules_progression`).

## 6. Dano, Saúde e Vantagem de Nível

* Todas as personagens têm uma base de **100 HP**.

### Dano Final (Fórmula de Dano Aditiva)

O dano é calculado pela Margem de Potencial Total do Atacante ($\mathbf{A_{FP}}$) e modificado pela Defesa, sendo sempre **Neutro por Nível** na Ofensa.

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$$

* $\mathbf{A_{FP}}$ (Margem de Potencial Total) $\equiv 100 - (d100 - R_{prof})$.
* $\mathbf{M_{DTA}}$ (Multiplicador de Vantagem de Nível Defensivo) $\equiv$ Reduz o dano se o Nível do Defensor for superior ao do Atacante (máximo $\times 0.25$ no $\Delta T=3$).

---

## 7. Descanso e Renovação (Recovery)

- Restaura a **E_cur** (Foco) para o valor da **E_max** atual.
- **NÃO** restaura o $\mathbf{E_{max}}$ que foi permanentemente perdido.
- **Restaura** o Pool de Impulsos de Ação (AS).

---

## 8. Fim do Jogo

Retiras-te esgotado e lendário.

A campanha é o registo de **como escolheste desvanecer**.

---
© 2025 Serelith Varn — Nárëquenta: Contos do Esvanecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte [LICENSE.md](license.md).
