![Repository Header Image](header_image.png)
# Nárëquenta — Contos do Esvanecer (Tales of the Waning)

**Versão: v0.7-FINAL (Letalidade de Precisão)**
**Autor:** Serelith Varn (cortonemo)
**Licença:** Nárëquenta Limited Open License (v0.1)

---

## 💡 Filosofia Central: A Atrição é o Significado

Nárëquenta é um TTRPG sobre **Decadência Elegante** (beautiful erosion). Os heróis começam no seu auge (100% de potencial) e desvanecem-se gradualmente à medida que agem e usam a sua Essência. A progressão não é o crescimento de números, mas sim a **definição do caráter através da perda**.

**Axioma Central (v0.7):** O poder é um recurso finito. O risco real não é a morte, mas o **Extinção da Essência**. A **Proficiência Compensa o Declínio**, permitindo um impacto máximo com capacidade mínima.

### Core Ideas (Ideias Base)

* Começa-se perto de **100%** em todas as Facetas do ser, após a **Erosão Inicial ($1d10$)**.
* Ao agir, **gasta-se** dessa Faceta ($\mathbf{E_{cur}}$). O gasto é lento e mitigado pela proficiência.
* Pode-se escolher **Refinar** essa Faceta: diminuir permanentemente o seu máximo ($\mathbf{E_{max}}$), mas ganhar **Dados de Proficiência ($\mathbf{D_{prof}}$)** para eficiência e poder ofensivo.
* O descanso restaura o que resta, mas nunca o que já foi queimado.

## ⚙️ Sumário do Sistema (v0.7)

O jogo é construído em torno da gestão de Essência, do **Dano Neutro por Nível** e **Mitigação por Nível**.

- **E_max (Máximo):** Tem um **Limite Fixo de 50%**. A Rolagem do Esvanecer é o único mecanismo de perda permanente. Esta redução determina o seu **Tier de Proficiência**.
- **E_cur (Atual):** A energia utilizável. Define o limiar de sucesso ($\mathbf{d100 \le E_{cur}}$).
- **Rolagens Contestadas:** O Atacante usa a sua $\mathbf{D_{prof}}$ (agora unificada para $1d10$) para Mitigação de Erro.
- **Dano:** Calculado usando a **Fórmula de Dano Aditiva** que privilegia a proficiência: $\mathbf{D_{Final}} = \max \left( 0, (A_{FP} - \bar{M}_{Defesa} + D_{Margin} + R_{prof}) \right) \times M_{DTA}$.
- **Progressão:** O risco de decaimento garante **$D_{prof}$** e **Impulsos de Ação (AS)** adicionais (até 4 no Tier V).

## 🗂 Conteúdos do Repositório

| Diretório | Conteúdo | Status |
| :--- | :--- | :--- |
| **`/Rules/`** | O Mecanismo Central, Metafísica e Rituais. | **v0.7 ATUALIZADO** |
| **`/Playtest/`** | Fichas, cenários e referências rápidas para a Alpha. | **v0.7 ATUALIZADO** |
| **`/Logs/`** | Notas de design e feedback de playtest (datado). | **v0.1 DRAFT** |
| **`/Tools/`** | Scripts de cálculo e utilidades (e.g., Nárëquenta Calculator em Python). | **NOVO** |

---

### 📜 Licença & Autoria

**© 2025 Serelith Varn**
Este projeto é lançado sob a **Nárëquenta Limited Open License (v0.1)**.
Você é livre para jogar, transmitir e criar conteúdo de fã para este sistema — desde que forneça o crédito adequado e não o utilize comercialmente.

📜 [Leia a licença completa →](LICENSE.md)