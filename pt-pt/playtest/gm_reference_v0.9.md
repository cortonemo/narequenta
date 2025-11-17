# ⚔️ GM Reference v0.9 (Mitigação de Degradação)


Rascunho Finalizado — 2025-11-17

***
## FLUXO DA SESSÃO
1.  **Briefing / Configuração:** Por que esta missão é importante (e o que arriscam perder).
2.  **Cenas de Jogo:** Qualquer ação significativa custa Essência ($\mathbf{E_{cur}}$) e é resolvida com uma **Jogada Contestada**.
    * O Jogador escolhe as Essências Motor ($\mathbf{E_{P}}$) e Qualidade ($\mathbf{E_{S}}$) (ver Regras Principais para Pares).
    * O Jogador usa $\mathbf{D_{prof}}$ para **Mitigação de Erro** ($\mathbf{R_{prof}}$ subtrai da jogada de $\mathbf{d100}$) e **Base de Dano**.
    * **Custo de Atrição:** A perda de $\mathbf{E_{cur}}$ é calculada usando o **resultado da jogada $\mathbf{R_{prof}}$** (Custo: $\max(0, 7 - R_{prof})$).

***
## FASE DE RITUAL E RECUPERAÇÃO (v0.9)
* **Renovação ($E_{cur}$ e AS):** Restaura **$\mathbf{E_{cur}}$** ao seu valor atual de $\mathbf{E_{max}}$.
    * Também restaura a reserva de **Ataque Súbito (AS)** ao máximo determinado pelo Nível (Nível V = **4 AS**).
* **Degradação e Refinamento ($E_{max}$):** Este processo ocorre **APENAS no final do Capítulo** (Jogada Minguante).
    * Solicitar aos jogadores que escolham o seu Foco de Proficiência (o risco de **$\mathbf{2d6}$**).
    * Rolar Degradação Universal ($\mathbf{1d6}$) e aplicar todas as perdas, garantindo que $\mathbf{E_{max}}$ nunca caia abaixo de **$\mathbf{50\%}$**.

***
## RITMO / TOM
* **Atrição é uma Escolha:** Nunca diga: "Não pode fazer isso". Diga: "O custo é uma perda de $\mathbf{X\%}$ de [Motor] e [Qualidade]. Está disposto a queimar tanto?".
* **Vantagem de Nível (DTA):** Lembre-se que a **Vantagem de Nível Defensiva ($\mathbf{M_{DTA}}$)** gere automaticamente os encontros de Nível baixo vs. Nível alto. O PC altamente proficiente ($\mathbf{E_{max}}$ baixo) é defensivamente forte contra inimigos mais fracos.
* **Letalidade:** Quando os Níveis são iguais, o combate é altamente letal ($\approx 46 \text{ PV}$ por golpe). Esteja pronto para resultados rápidos e decisivos baseados em margens críticas.
* **Recompensa Narrativa:** Recompense descrições criativas e vívidas, permitindo que o Atacante ganhe vantagem na própria **jogada $\mathbf{D_{prof}}$** (p. ex., rolar novamente um dado), em vez de modificar a fórmula final.
* **Trate o Final como Sagrado.** Quando todas as Facetas atingem $\mathbf{E_{cur}} = 0$, pergunte: como serão lembrados?.

---

## VII. Referência de Níveis de Proficiência e Mitigação (v0.9)
O Nível é calculado a partir da perda de $\mathbf{E_{max}}$.

| Perda $\mathbf{E_{max}}$ | $\mathbf{E_{max}}$ Remanescente (%) |        Nível         | $\mathbf{D_{prof}}$ | $\mathbf{\bar{M}}$ (Mitigação de Defesa) | **Ataques Súbitos (AS)** |
| :----------------------: | :--------------------------------: | :------------------: | :-----------------: | :--------------------------------------: | :----------------------: |
|         $0-9\%$          |             $100-91\%$             |      **0** |        Nenhum         |                  $0.0$                  |          **0** |
|        $10-19\%$         |             $90-81\%$              |      **I** |   $\mathbf{1d10}$   |                  $5.5$                  |          **1** |
|        $20-29\%$         |             $80-71\%$              |      **II** |   $\mathbf{2d10}$   |                 $11.0$                  |          **2** |
|        $30-39\%$         |             $70-61\%$              |     **III** |   $\mathbf{3d10}$   |                 $16.5$                  |          **3** |
|        $40-49\%$         |             $60-51\%$              |      **IV** |   $\mathbf{4d10}$   |                 $22.0$                  |          **4** |
|     $\mathbf{50\%}$      |          $\mathbf{50\%}$           | **V (Pináculo)** |   $\mathbf{5d10}$   |             $\mathbf{27.5}$             |       **5** (Máx)        |

---

## VIII. Grelha do Multiplicador de Vantagem de Nível Defensiva ($\mathbf{M_{DTA}}$) (v0.9)
O $\mathbf{M_{DTA}}$ é determinado pela diferença nos Níveis ($\Delta T = T_{Defensor} - T_{Atacante}$).

| Nível do Atacante $\downarrow$ vs. Nível do Defensor $\rightarrow$ |            **I** |          **II** |          **III** |          **IV** |           **V** |
| :----------------------------------------------------------------: | :-------------------------: | :-----------------------: | :-----------------------: | :-----------------------: | :-----------------------: |
|                           **I** |  $\mathbf{1.00}$ (Neutro)   |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |      $\mathbf{0.25}$      | $\mathbf{0.25}$ (Limitado)  |
|                           **II** |       $\mathbf{1.25}$       | $\mathbf{1.00}$ (Neutro) |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |      $\mathbf{0.25}$      |
|                          **III** |       $\mathbf{1.50}$       |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutro) |      $\mathbf{0.75}$      |      $\mathbf{0.50}$      |
|                           **IV** |       $\mathbf{1.75}$       |      $\mathbf{1.50}$      |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutro) |      $\mathbf{0.75}$      |
|                            **V** | $\mathbf{2.00}$ (Bónus Máx) |      $\mathbf{1.75}$      |      $\mathbf{1.50}$      |      $\mathbf{1.25}$      | $\mathbf{1.00}$ (Neutro) |

---
© 2025 Serelith Varn — Nárëquenta: Contos do Minguante.
Licenciado para jogo não comercial e conteúdo de fãs sob a Licença Aberta Limitada Nárëquenta (v0.1). Ver [LICENSE.md](license.md).

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See  [LICENSE.md](license.md).