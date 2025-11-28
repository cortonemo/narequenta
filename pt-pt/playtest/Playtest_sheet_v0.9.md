# Nárëquenta: Ficha de Teste Alpha (v0.9.6)

**Nome:** [_____________________]
**Conceito:** [_____________________]
**PV Atuais:** [100] / 100
**RESERVA DE ATAQUE SÚBITO (AS):** [ ] / [ Máx: ___ ]

## ESSÊNCIAS (E_max vs E_cur)
**Instruções:** $\mathbf{E_{max}}$ é o potencial permanente (Piso 50%). $\mathbf{E_{cur}}$ define a sua **Zona de Tensão**.

| Essência | $E_{MAX}$ (Potencial) | NÍVEL | $E_{CUR}$ (Atual) | ZONA (0/-10/-20/-30) |
| :--- | :--- | :--- | :--- | :--- |
| **VITALIS** | [100%] | [____] | [100%] | [____] |
| **MOTUS** | [100%] | [____] | [100%] | [____] |
| **SENSUS** | [100%] | [____] | [100%] | [____] |
| **VERBUM** | [100%] | [____] | [100%] | [____] |
| **ANIMA** | [100%] | [____] | [100%] | [____] |

## REFERÊNCIA RÁPIDA: ZONAS DE TENSÃO
| $E_{cur}$ % | Zona | Penalidade |
| :--- | :--- | :--- |
| 100-76% | Pico | **-0** |
| 75-51% | Minguante | **-10** |
| 50-26% | Desvanecente | **-20** |
| 25-0% | Vazio | **-30** |

## REFERÊNCIA DE ATRIÇÃO E DANO (v0.9.6)

**Sucesso:** $(d100 - R_{prof}) \le (E_{max} - Zona)$

| Atrição (Custo) | Peso Leve (10) | Peso Médio (15) | Peso Pesado (20) |
| :--- | :--- | :--- | :--- |
| **Fórmula** | $\max(0, 10 - \lfloor R_{prof}/2 \rfloor)$ | $\max(0, 15 - \lfloor R_{prof}/2 \rfloor)$ | $\max(0, 20 - \lfloor R_{prof}/2 \rfloor)$ |

**Dano Final:** $\max(R_{prof}, (A_{FP} - \bar{M}_{Def} + D_{Margin} + R_{prof})) \times M_{DTA}$

---
© 2025 Serelith Varn.
