![Repository Header Image](header_image.png)
# Nárëquenta — Contos do Esvanecer (Tales of the Waning)

**Versão: v0.8-FINAL (Letalidade de Precisão e Estabilização SPA)**
**Autor:** Serelith Varn (cortonemo)
**Licença:** Nárëquenta Limited Open License (v0.1)

-----

## 💡 Filosofia Central: A Atrição é o Significado

Nárëquenta é um TTRPG sobre **Decadência Elegante** (*beautiful erosion*). Os heróis começam no seu auge e desvanecem-se gradualmente à medida que agem e usam a sua Essência. A progressão é a **definição do caráter através da perda**.

**Axioma Central (v0.8):** O poder é um recurso finito. O risco real não é a morte, mas o **Extinção da Essência**. A **Proficiência Compensa o Declínio**, permitindo um impacto máximo com capacidade mínima.

## ⚙️ Sumário do Sistema (v0.8)

O jogo é construído em torno da gestão de Essência, do **Dano Neutro por Nível** e **Mitigação por Nível**.

  * **E\_max (Máximo):** Tem um **Limite Fixo de 50%**. A redução determina o seu **Tier de Proficiência**.
  * **E\_cur (Atual):** A energia utilizável. Define o limiar de sucesso ($\mathbf{d100 \le E_{cur}}$).
  * **Dano:** Calculado usando a **Fórmula de Dano Aditiva** que privilegia a proficiência.   $$\\mathbf{D\_{Final}} = \\max \\left( 0, (A\_{FP} - \\bar{M}*{Defesa} + D*{Margin} + R\_{prof}) \\right) \\times M\_{DTA} \\text{}$$
* **Multiplicador $\mathbf{M_{DTA}}$:** A **Grelha Completa de $\mathbf{M_{DTA}}$** foi adicionada e reestruturada na v0.8 para gerir explicitamente a vantagem/redução de dano com base na diferença de Tier.
  * **Arquitetura:** A aplicação da ficha foi migrada para uma **Single Page Application (SPA)**, unificando as referências do PC, NPC e GM em `index.html`.

## 🗂 Conteúdos do Repositório

| Diretório | Conteúdo | Status |
| :--- | :--- | :--- |
| **`/Rules/`** | O Mecanismo Central, Metafísica e Rituais. | **v0.8 ATUALIZADO** |
| **`/Playtest/`** | Fichas, cenários e referências rápidas para a Alpha. | **v0.8 ATUALIZADO** |
| **`/Tools/`** | Scripts de cálculo e utilidades (e.g., Nárëquenta Calculator em Python). | **v0.8 ATUALIZADO** |

-----

### 📜 Licença & Autoria

**© 2025 Serelith Varn**
Este projeto é lançado sob a **Nárëquenta Limited Open License (v0.1)**.
Você é livre para jogar, transmitir e criar conteúdo de fã para este sistema — desde que forneça o crédito adequado e não o utilize comercialmente.

📜 [Leia a licença completa →](LICENSE.md)