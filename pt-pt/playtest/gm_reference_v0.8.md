# ⚔️ GM Reference v0.8

Rascunho Finalizado — 2025-11-15 (Arquitetura Estabilizada)

## FLUXO DA SESSÃO

1. **Briefing / Preparação:** Por que esta missão é importante (e o que arriscam perder).
    
2. **Cenas de Jogo:** Qualquer ação significativa custa Essência ($\mathbf{E_{cur}}$) e é resolvida com uma **Rolagem Contestada**.
    
    - O jogador escolhe as Essências Motor ($\mathbf{E_{P}}$) e Qualidade ($\mathbf{E_{S}}$).
        
    - O jogador usa $\mathbf{D_{prof}}$ para **Mitigação de Erro** ($\mathbf{R_{prof}}$ subtrai do $\mathbf{d100}$) e **Dano Base**.
        
    - **Custo de Atrição:** A perda de $\mathbf{E_{cur}}$ é calculada usando o **resultado $\mathbf{R_{prof}}$ da rolagem** (Custo: $\max(0, 7 - R_{prof})$).
        

## RITUAL E FASE DE RECUPERAÇÃO

- **Renovação ($\mathbf{E_{cur}}$ e AS):** Restaura **$\mathbf{E_{cur}}$** para o seu valor $\mathbf{E_{max}}$ atual. Também restaura o pool de **Impulsos de Ação (AS)** até ao máximo determinado pelo Tier (Tier V = 4 AS).
    
- **Decaimento e Refinamento ($\mathbf{E_{max}}$):** Este processo acontece **SOMENTE no final do Capítulo** (Rolagem do Esvanecer).
    
    - O jogador foca a perda na **Essência Escolhida (Foco)** com um risco de $\mathbf{4d6}$.
        
    - O Decaimento Universal aplica $\mathbf{2d6}$ a Essências Não Escolhidas.
        
    - **Limite:** $\mathbf{E_{max}}$ nunca pode descer abaixo de **$50\%$**.
        

## 🛡️ Tabela Completa do Multiplicador de Vantagem de Tier ($\mathbf{M_{DTA}}$)

Use esta grelha para aplicar o multiplicador na **Fórmula de Dano Aditiva**.

$$\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defense} + D_{Margin} + R_{prof}) \right) \times M_{DTA} \text{}$$

## RITMO / TOM

- **A Atrição é uma Escolha:** O custo de $\mathbf{E_{cur}}$ é inevitável; a questão é se o jogador está disposto a queimar.
    
- **Vantagem de Nível (DTA):** A grelha acima gere automaticamente o dano. Lembre-se que o PC altamente proficiente (Tier alto, $\mathbf{E_{max}}$ baixo) é **defensivamente forte** contra inimigos mais fracos (Tier baixo).
    
- **Letalidade:** Quando os Tiers são iguais, o combate é rápido e decisivo.
    
- **Ferramentas Integradas (SPA v0.8):** A **Calculadora de Dano** está agora integrada na nova arquitetura Single Page Application (`index.html`) na secção de Referência do GM. Utilize-a para validação rápida de dano.
    
- **Trate o Fim Como Sagrado.** Quando todas as Facetas atingem $\mathbf{E_{cur}} = 0$, pergunte: como são lembrados?.
    

---
© 2025 Serelith Varn — Nárëquenta: Contos do Escurecer.
Licenciado para jogo não comercial e conteúdo de fã sob a Nárëquenta Limited Open License (v0.1). Consulte [LICENSE.md](license.md).

---
© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.
Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See  [LICENSE.md](license.md).