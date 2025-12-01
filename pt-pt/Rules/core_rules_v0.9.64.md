# 📜 Nárëquenta Regras Base v0.9.64 

## 1. O Que É Este Jogo 🧭

Nárëquenta é um TTRPG onde os heróis começam perto do seu auge e terminam gastos. A progressão é a **definição da personagem através da perda**. O poder é um recurso finito. **A Proficiência Compensa o Declínio**.

***

## 2. Facetas do Eu (Essências) ✨

Cada personagem é definida por cinco Essências. Cada Essência começa a **$100\%$**, sujeita à Erosão Inicial.

- **VITALIS** — corpo, resistência, força, presença
- **MOTUS** — movimento, finesse, agilidade, graça
- **SENSUS** — perceção, instinto, foco, atenção
- **VERBUM** — intelecto, lógica, estrutura, discurso
- **ANIMA** — convicção, vontade, fé, sacrifício

### Valores de Essência

- **Pico da Alma ($\mathbf{E_{max}}$):** Limite permanente. Nunca pode descer abaixo de **$50\%$** (Piso Rígido).
- **Vigor Ativo ($\mathbf{E_{cur}}$):** Energia utilizável. Determina a tua **Zona de Tensão**.

***

## 3. Resolução de Ações: A Rolagem Efetiva 🎯

O sucesso é determinado comparando a **Rolagem Efetiva** com a Capacidade Permanente ($\mathbf{E_{max}}$), ajustada pela fadiga.

### A. Condição de Bloqueio (O Vazio Absoluto)

Antes de qualquer rolagem, verifica-se o Vigor Ativo ($\mathbf{E_{cur}}$).

$$\text{Se } \mathbf{E_{cur}} < 1 \rightarrow \text{Falha Automática / Ação Impossível}$$

> ==**Se o Vigor Ativo for menor que 1, a ação resulta em falha automática.**==

**Recuperação de Emergência (Fôlego Rápido):** Se estiveres a $0 \ \mathbf{E_{cur}}$, podes gastar o teu turno inteiro para tomar um Fôlego Rápido (Descanso Curto).

### B. A Fórmula da Rolagem Efetiva

$$\mathbf{R_{Eff}} = \mathbf{d100} - \mathbf{R_{prof}}$$

> ==**A Rolagem Efetiva é igual ao Dado de Caos ($\mathbf{d100}$) menos o Resultado de Perícia ($\mathbf{R_{prof}}$).==**

### C. O Teste de Sucesso

$$\mathbf{R_{Eff}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalty}})$$

> ==**A ação é bem-sucedida se a Rolagem Efetiva for menor ou igual ao teu $\mathbf{E_{max}}$ menos a Penalidade de Zona atual.**
==
### D. Zonas de Tensão ($\mathbf{E_{cur}}$)

À medida que $\mathbf{E_{cur}}$ desce, a dificuldade artificial aumenta.

| **Intervalo $\mathbf{E_{cur}}$** | **Nome da Zona** | **Penalidade ($\mathbf{Z_{Penalty}}$)** |
| :--- | :--- | :--- |
| **100% – 76%** | **Pico** | **-0** |
| **75% – 51%** | **Minguante** | **-10** |
| **50% – 26%** | **Desvanecente** | **-20** |
| **25% – 0%** | **Vazio** | **-30** |

***

## 4. Atrição: O Custo da Ação 🩸

Cada ação queima Essência. O custo deriva do **Peso do Item** e é mitigado pela **Perícia**.

### Fórmula de Atrição

$$\mathbf{Custo} = \max \left( 0, \mathbf{Peso} - \left\lfloor \frac{\mathbf{R_{prof}}}{2} \right\rfloor \right)$$

> ==**O Custo de Energia é igual ao Peso da Arma menos metade do Resultado de Proficiência (arredondado para baixo).**==

| **Classe de Peso** | **Custo Base** | **Exemplos** |
| :--- | :--- | :--- |
| **Leve** | **10%** | Adagas, Arcos Curtos |
| **Médio** | **15%** | Espadas, Dardos |
| **Pesado** | **20%** | Maças, Bestas Pesadas |

- **Sucesso Crítico (1-5):** Reduz para metade o Custo final.
- **Falha Crítica (96-100):** Duplica o Custo final.

***

## 5. Combate: Letalidade de Precisão ($\mathbf{D_{Final}}$) 💥

O cálculo de dano privilegia a Perícia ($\mathbf{R_{prof}}$). **O Dano é Neutro em Nível**, calculado pelas Margens e modificado pela Vantagem de Nível.

### Fórmula de Dano Final

$$\mathbf{D_{Final}} = \max \left( \mathbf{R_{prof}}, (\mathbf{A_{FP}} - \mathbf{\bar{M}_{Def}} + \mathbf{D_{Margin}} + \mathbf{R_{prof}}) \right) \times \mathbf{M_{DTA}}$$

> ==**O Dano Final é o maior entre o Piso de Proficiência ou a Margem Calculada, multiplicado pela Vantagem de Nível.**==

| **Componente** | **Definição** |
| :--- | :--- |
| **$\mathbf{R_{prof}}$ (Piso Rígido)** | **Dano Base Aditivo.** O dano mínimo absoluto é o teu resultado de Proficiência. |
| **$\mathbf{A_{FP}}$ (Potencial Total)** | $\mathbf{100 - (d100 - R_{prof})}$. **Neutro em Nível.** Baseado em 100%, não no $E_{cur}$ do Atacante. |
| **$\mathbf{\bar{M}_{Def}}$ (Mitigação)** | A armadura passiva do Defensor (Média do seu *pool* de $D_{prof}$). |
| **$\mathbf{D_{Margin}}$ (Vulnerabilidade)** | Rolagem de Defesa do Defensor menos $\mathbf{E_{cur}}$. Valores positivos aumentam o dano. |
| **$\mathbf{M_{DTA}}$ (Vantagem de Nível)** | Multiplicador que escala de $\times 0.75$ (Desvantagem) a $\times 2.00$ (Dominância). |

***

## 6. Rituais e Renovação (Recuperação) 🕯️

Os Rituais fecham o ciclo do jogo (Gastar → Desvanecer → **Renovar**), permitindo ao PC gerir a fadiga diária e aceitar a perda permanente.

### A. Renovação de Foco (Descanso Longo) 🌙

Este ritual permite ao PC recuperar o seu foco mental e físico, regressando ao seu potencial diário.

- **Gatilho:** Descanso Longo (ex: uma noite de sono segura, mínimo 6 horas).
- **Processo:**
    1. **Restauração de Vigor:** O **Valor Atual ($\mathbf{E_{cur}}$)** de todas as Essências reinicia a **100%**.
       > *Regra Crítica:* A recuperação **NÃO** é limitada pelo $\mathbf{E_{max}}$. Mesmo se o teu Pico da Alma estiver degradado a 50%, o teu Vigor Ativo regressa a 100%. Começas o dia totalmente energizado, na **Zona de Pico**.
    2. **Restauração de Surto:** O **Pool de Impulso de Ação (AS)** é **totalmente restaurado** ao total determinado pelo Nível de Proficiência.
- **Custo Narrativo:** Tempo e segurança.

### B. O Descanso Curto (Pausa) 🍵

Uma breve pausa para tratar feridas, recuperar o fôlego e centrar a mente (15 minutos).

$$\mathbf{Recuperação} = \text{Soma de } \mathbf{D_{prof}}$$

> ==**A Recuperação é igual à soma dos resultados da tua Reserva de Dados de Proficiência.**==

(Fallback: Se Nível 0, rola 1d10).

### C. Recuperação de Emergência (O Fôlego Rápido) 💨

Uma tentativa desesperada de se centrar no calor da batalha, geralmente acionada ao atingir o Vazio ($0 \ \mathbf{E_{cur}}$).

- **Gatilho:** Pode ser realizado a qualquer momento durante o teu turno, ou forçado quando $\mathbf{E_{cur}} < 1$.
- **Custo:** **Ação de Turno Completo.** Não podes Mover, Defender, Atacar ou Reagir até ao início do teu próximo turno.
- **Efeito:** Resolve imediatamente como um **Descanso Curto** (Rola $\mathbf{D_{prof}}$ ou 1d10 e recupera essa quantidade em $\mathbf{E_{cur}}$).

### D. Nota sobre Perda Permanente 💀

O sistema distingue entre **Fadiga** e **Decadência**.

- **Renovável:** $\mathbf{E_{cur}}$ (**Vigor Ativo**) representa energia. Flutua constantemente e recupera a **100%**.
- **Não Renovável:** $\mathbf{E_{max}}$ (**Pico da Alma**) representa a integridade estrutural da alma. O sistema **NÃO** restaura $\mathbf{E_{max}}$ perdido através da Rolagem do Esvanecer.

***

## 7. Progressão: A Rolagem do Esvanecer 🌘

A progressão ocorre em marcos narrativos ao reduzir permanentemente $\mathbf{E_{max}}$ para avançar Níveis de Proficiência.

- **Decadência Universal (Não-Escolhida):** Rola **1d6**. Subtrai a $\mathbf{E_{max}}$.
- **Foco de Refinamento (Escolhida):** Rola **2d6**. Subtrai a $\mathbf{E_{max}}$ para ganhar $\mathbf{D_{prof}}$.

### Tabela de Proficiência e Mapeamento de Dados

| **Nível** | **Perda Total $\mathbf{E_{max}}$** | **$\mathbf{E_{max}}$ Restante** | **Dados $\mathbf{D_{prof}}$** | **Mitigação ($\mathbf{\bar{M}}$)** | **Surtos de Ação** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | $0-9\%$ | $100-91\%$ | Nenhum | $0.0$ | **0** |
| **I** | $10-19\%$ | $90-81\%$ | $\mathbf{1\text{d}10}$ | $5.5$ | **1** |
| **II** | $20-29\%$ | $80-71\%$ | $\mathbf{2\text{d}10}$ | $11.0$ | **2** |
| **III** | $30-39\%$ | $70-61\%$ | $\mathbf{3\text{d}10}$ | $16.5$ | **3** |
| **IV** | $40-49\%$ | $60-51\%$ | $\mathbf{4\text{d}10}$ | $22.0$ | **4** |
| **V** | $\mathbf{50\%}$ | **50% (Pináculo)** | $\mathbf{5\text{d}10}$ | $\mathbf{27.5}$ | **5** |

***

## 8. Uso da Proficiência (Mecânicas Detalhadas) ⚙️

O resultado da rolagem $\mathbf{D_{prof}}$ ($\mathbf{R_{prof}}$) é usado para três efeitos simultâneos:

1.  **Mitigação de Erro:** Subtrai $\mathbf{R_{prof}}$ da rolagem de $\mathbf{d100}$.
2.  **Redução de Atrição:** $\mathbf{Custo} = \text{Peso} - \lfloor R_{prof}/2 \rfloor$.
3.  **Ataques Especiais (Opcional):** Sacrificar dados do *pool* de $\mathbf{D_{prof}}$ para realizar ações aprimoradas.

***

## 9. Apêndice: Referência do Sistema (Sigla) 📚

### Detalhes dos Componentes

1. Margem de Potencial Total ($\mathbf{A_{FP}}$)

$$\mathbf{A_{FP}} = \mathbf{100 - (d100-R_{prof})}$$

> ==**Isto calcula o poder bruto do Atacante em relação a uma base perfeita de 100. Uma rolagem modificada mais baixa gera um $\mathbf{A_{FP}}$ maior.==**

2. Margem do Defensor ($\mathbf{D_{Margin}}$)

$$\mathbf{D_{Margin}} = \mathbf{d100_D-D_{Ecur}}$$

> ==**Isto mede a vulnerabilidade do Defensor. Um $\mathbf{D_{Margin}}$ positivo significa que o Defensor falhou na defesa, aumentando o dano.**
==
***
© 2025 Serelith Varn — Nárëquenta. Licenciado sob Nárëquenta Limited Open License (v0.1). Ver [[LICENSE.md]].