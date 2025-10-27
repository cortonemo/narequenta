## 📄 Nárëquenta Regras Base v0.4

Rascunho — 2025-10-26

## 1. O Que É Este Jogo

Nárëquenta é um TTRPG onde os heróis começam perfeitos e acabam esgotados.

As personagens começam com força total em todos os aspetos de si mesmas.

Não ganham níveis.

São lembrados pela forma elegante como se desvanecem.

Não estás a tentar sobreviver para sempre.

Estás a decidir que partes de ti valem a pena gastar antes de partires.

---

## 2. Facetas do Ser (Essências)

Cada personagem é definida por cinco Facetas (Essências). Cada Faceta começa a 100%.

- **VITALIS** — corpo, resistência, força, presença
    
- **MOTUS** — movimento, destreza, agilidade, graça
    
- **SENSUS** — consciência, instinto, foco, perceção
    
- **VERBUM** — intelecto, lógica, estrutura, discurso
    
- **ANIMA** — convicção, vontade, fé, sacrifício
    

Cada Faceta tem:

- Um **Valor Atual ($\mathbf{E_{cur}}$)** (quanto dessa parte de ti está utilizável neste momento).
    
- Um **Valor Máximo ($\mathbf{E_{max}}$)** (o limite até onde pode ser restaurado).
    
- Uma **Eficiência ($\mathbf{A_{rate}}$)** (o quão custoso é para ti agir através dessa Faceta).
    

Na criação de personagem:

- Atual ($\mathbf{E_{cur}}$) = 100%
    
- Máximo ($\mathbf{E_{max}}$) = 100%
    
- Eficiência (Custo) = 1.0 (custo base $30\%$/$40\%$)
    

---

### 3. Agir no Mundo (Resolução de Ação: Rolagens Contestadas)

As Ações são agora resolvidas como **Rolagens Contestadas** onde tanto o Atacante (A) quanto o Defensor (D) rolam para influenciar o resultado. O objetivo é sempre rolar $\mathbf{d100 \le \mathbf{E_{cur}}}$ da Essência relevante ($\mathbf{E_{P}}$).

#### Fluxo de Resolução de Ação
1. **Atacante Rola:** A rola $\mathbf{d100 \le \mathbf{E_{cur}}}$ (Motor do Atacante $\mathbf{E_{P}}$) para acertar.
2. **Atacante Mitiga:** A rola os seus **Dados de Proficiência ($\mathbf{D_{prof}}$)** e **subtrai o resultado da rolagem $\mathbf{d100}$**.
3. **Defensor Rola:** Se o ataque acertar, o D rola $\mathbf{d100 \le \mathbf{E_{cur}}}$ (Motor do Defensor $\mathbf{E_{P}}$) para mitigar o dano.

#### Resultados Críticos (Ataque e Defesa)
O intervalo de Acerto Crítico é definido como **$<$10 na rolagem d100**. O intervalo de Falha Crítica é **$>$90 na rolagem d100**.
* **Crítico Duplo:** Se A rola um Acerto Crítico e D rola uma Falha Crítica, o ataque desencadeia um Crítico Duplo. O atacante causa **10d10 de Dano**.
* **Reversão em Falha:** Se A rola uma Falha Crítica e D rola um Acerto Crítico, o atacante recebe o dano crítico total do defensor (**10d10**).

#### Custo de Atrição
1. **Custos de Sucesso:** O custo é calculado como a **Eficiência ($\mathbf{A_{rate}}$)** do Motor ($\mathbf{E_{P}}$) mais o custo fixo ($1\%$-$2\%$) da Qualidade ($\mathbf{E_{S}}$).
2. **Redução de Proficiência:** O resultado médio dos $\mathbf{D_{prof}}$ utilizados é **subtraído do custo total de $\mathbf{E_{cur}}$**.

#### Ações Fora de Combate (v0.5 Mantido):
A maioria das ações fora de combate (investigação, interações sociais) **não incorre em custos de Atrição**, usando a $\mathbf{E_{cur}}$ apenas como limite de sucesso. Apenas em situações de stress físico ou mental extremo, o MJ pode aplicar um **Custo Fixo de $\mathbf{2\%}$** (ou mais, por consenso) para simular o esforço sustentado.

---

### 4. Ciclo de Refinamento e Decaimento (The Waning Roll)

**Esta mecânica substitui o sistema de Marcos de Decadência.** O Refinamento e o Decaimento ocorrem no final de cada marco importante.

### 4.1. A Escolha de Proficiência (The Proficiency Choice)
Antes de qualquer rolagem, o jogador deve escolher **uma (1)** Essência para Foco (a Essência de Refinamento).

| Custo | Recompensa (Proficiência) |
| :--- | :--- |
| Decaimento de $\mathbf{4\text{d}6}$ | Ganha **$\mathbf{2\text{d}10}$ Dados de Proficiência ($\mathbf{D_{prof}}$)** em rolagens contestadas com essa Essência. |

### 4.2. A Rolagem do Esvanecer (Decay Phase)
Aplica-se o Decaimento a todas as Essências:

| Essência | Rolagem de Decaimento | Efeito no $\mathbf{E_{max}}$ |
| :--- | :--- | :--- |
| **Essências Não Escolhidas** | $\mathbf{2\text{d}6}$ | O total é subtraído permanentemente do **Valor Máximo ($\mathbf{E_{max}}$)**. |
| **Essência Escolhida (Foco)** | $\mathbf{4\text{d}6}$ | O total é subtraído permanentemente do **Valor Máximo ($\mathbf{E_{max}}$)** (queima mais rápido). |
#### 4.3. Uso da Proficiência (Novo Sistema de Tiers)
Os $\mathbf{2\text{d}10}$ Dados de Proficiência ganhos são convertidos num *pool* de $\mathbf{D_{prof}}$ com base na Tabela de Tiers de Proficiência (consulte `rules_contested_rolls_v0.5.md`). Os $\mathbf{D_{prof}}$ são usados principalmente para **Mitigação de Erro** e **Redução de Atrição**.

---
## 5. Descanso e Renovação (Recovery)

Após o fim de uma missão, há uma Fase de Recuperação.

A Recuperação faz:

- Restaura a **E_cur** (Foco) para o valor da **E_max** atual.
    
- **NÃO** restaura o $\mathbf{E_{max}}$ que foi permanentemente perdido durante a **Rolagem do Esvanecer** (Secção 4).
    

Estás sempre a regressar um pouco menos do que eras.

---
### 6. Dano e Saúde
* Todas as personagens têm uma base de **100 HP**.
* **Dano Bónus:** Se o atacante rolar significativamente abaixo da sua própria $\mathbf{E_{cur}}$ (e.g., uma rolagem de 12 vs. estatística 60), **+5 HP por cada 10% abaixo da estatística do atacante** é aplicado.
* **Teto de Desgaste de Energia:** O desgaste máximo de $\mathbf{E_{cur}}$ por dano é limitado pelo **resultado máximo possível do dado de Proficiência mais alto da personagem**.

---
## 7. Fim do Jogo

Não te retiras rico. Retiras-te esgotado e lendário.

No final do jogo:

- Os teus Máximos ($\mathbf{E_{max}}$) estão mais baixos (60%, 55%, 43%...).
    
- As tuas Eficiências ($\mathbf{A_{rate}}$) são desumanas (3%, 4%...).
    
- Cada movimento custa quase nada, mas tens muito poucos movimentos restantes.
    

A campanha é o registo de **como escolheste desvanecer**.

---
© 2025 Serelith Varn — Nárëquenta: Contos do Escurecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte [LICENSE.md](license.md).

© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See  [LICENSE.md](license.md).

---
