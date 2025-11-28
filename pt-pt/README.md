
![Repository Header Image](header_image.png)
# Nárëquenta — Contos do Declínio (Foundry VTT)

**Versão: v0.9.6 (Letalidade de Precisão & Zonas de Tensão)**
**Autor:** Serelith Varn (cortonemo)
**Licença:** Nárëquenta Limited Open License (v0.1)
**Compatibilidade:** Foundry VTT v11+

-----

## 💡 Filosofia Central: A Atrição é o Significado

Nárëquenta é um TTRPG sobre **Decadência Elegante**. Os heróis começam no seu auge e desvanecem-se gradualmente à medida que agem e gastam a sua Essência. A progressão é a **definição do caráter através da perda**.

**Axioma Central (v0.9.6):** O sucesso torna-se mais difícil à medida que te cansas (Zonas), mas a Perícia ($\mathbf{R_{prof}}$) garante um impacto mínimo ($\mathbf{D_{Piso}}$).

## ⚙️ Sumário do Sistema (v0.9.6)

O jogo é construído em torno da gestão de Essência, **Zonas de Tensão** e **Letalidade de Precisão**.

* **Limiar de Sucesso:** As ações são bem-sucedidas se a **Rolagem Efetiva** for menor ou igual ao **Potencial menos Fadiga**:
    $$\mathbf{d100} - \mathbf{R_{prof}} \le (\mathbf{E_{max}} - \mathbf{Z_{Penalidade}})$$

* **Zonas de Tensão:** À medida que $\mathbf{E_{cur}}$ cai, as penalidades aumentam:
    * **Pico (100-76%):** -0
    * **Minguante (75-51%):** -10
    * **Desvanecente (50-26%):** -20
    * **Vazio (25-0%):** -30

* **Atrição:** O custo da ação deriva do **Peso do Item** e é mitigado pela Perícia:
    $$Custo = \max(0, Peso - \lfloor R_{prof}/2 \rfloor)$$

* **Dano:** Calculado usando a **Fórmula de Dano Aditiva** com um piso rígido de perícia:
    $$\mathbf{D_{Final}} = \max(R_{prof}, (A_{FP} - \bar{M}_{Def} + D_{Margin} + R_{prof})) \times M_{DTA}$$

## 🗂 Conteúdos do Repositório

| Diretório | Conteúdo | Status |
| :--- | :--- | :--- |
| **`/Rules/`** | O Mecanismo Central, Metafísica e Rituais. | **v0.9.6 ATUALIZADO** |
| **`/Playtest/`** | Fichas, cenários e referências rápidas para a Alpha. | **v0.9.6 ATUALIZADO** |
| **`/Tools/`** | Scripts de cálculo e utilidades (e.g., Nárëquenta Calculator em Python). | **v0.9.6 ATUALIZADO** |

-----

### 📦 Instalação

1.  Abra o Foundry VTT.
2.  Vá a **Game Systems** -> **Install System**.
3.  Cole o URL do Manifesto:
    `https://github.com/cortonemo/narequenta-vtt/releases/latest/download/system.json`
4.  Clique em **Install**.

-----

### 📜 Licença & Autoria

**© 2025 Serelith Varn**
Este projeto é lançado sob a **Nárëquenta Limited Open License (v0.1)**.
Você é livre para jogar, transmitir e criar conteúdo de fã para este sistema — desde que forneça o crédito adequado e não o utilize comercialmente.
Este software baseia-se no **Simple Worldbuilding System** de Atropos, utilizado sob a Licença MIT.

📜 [Leia a licença completa →](LICENSE.md)
-----

