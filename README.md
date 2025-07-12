# Automate Flow

## 📖 Sobre o Projeto

O **Automate Flow** é uma aplicação de desktop desenvolvida para criar e executar automações de tarefas de forma visual e intuitiva. A ferramenta permite que os usuários construam "fluxos" compostos por uma sequência de ações que são acionadas por diferentes "gatilhos".

A ideia central é oferecer uma alternativa acessível para usuários que desejam automatizar processos repetitivos em seus computadores sem a necessidade de escrever scripts complexos.

## ✨ Funcionalidades

* **Criação de Fluxos de Automação:** Crie múltiplos fluxos, cada um com uma sequência de passos personalizada.
* **Gatilhos (Triggers) Variados:**
    * **Tempo:** Inicie uma ação após um determinado período.
    * **Reconhecimento de Imagem:** Execute uma ação quando uma imagem específica for encontrada na tela.
    * **Clique do Mouse:** Dispare um evento a partir de um clique do mouse.
    * **Tecla de Atalho:** Inicie o fluxo ao pressionar uma tecla (ex: `Ctrl`).
* **Ações (Actions) Abrangentes:**
    * **Clique do Mouse:** Simule cliques em coordenadas específicas ou em imagens.
    * **Escrita:** Preencha campos de texto ou formulários.
    * **Comandos de Teclado:** Execute atalhos como `Ctrl+C`, `Ctrl+V`, `Alt+Tab`, entre outros.
    * **Operações do Sistema (OS):** Copie, mova, crie ou delete arquivos e pastas.
* **Interface Gráfica Intuitiva:** Gerencie seus fluxos, adicione, edite, teste e execute ações diretamente pela interface.
* **Configuração Flexível:** Salve as configurações do projeto localmente, no diretório do usuário ou em uma pasta personalizada.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

* **Python:** Linguagem principal do projeto.
* **PySide6 (Qt for Python):** Para a construção de toda a interface gráfica.
* **PyAutoGUI:** Para a automação de cliques, teclado e reconhecimento de imagem.
* **Pynput:** Para monitorar eventos de mouse e teclado.
* **OpenCV e Pillow (PIL):** Para processamento e manipulação de imagens.

## 🚀 Como Usar

### Pré-requisitos

Antes de começar, certifique-se de ter o Python 3.9 (ou superior) instalado.

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/GNSiqueira/automate_flow.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd automate_flow
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Para iniciar a aplicação, execute o arquivo `main.py`:

```bash
python main.py
```

Ao iniciar pela primeira vez, a aplicação perguntará onde você deseja salvar os arquivos de configuração.

## 🖼️ Telas da Aplicação

*(Em breve: Adicione aqui screenshots da sua aplicação para demonstrar a interface.)*

## 👨‍💻 Contato

**Gabriel Neto** - [gabriel272173siqueira@gmail.com](gabriel272173siqueira@gmail.com)

Link do Projeto: [https://github.com/GNSiqueira/automate_flow.git](https://github.com/GNSiqueira/automate_flow.git)
