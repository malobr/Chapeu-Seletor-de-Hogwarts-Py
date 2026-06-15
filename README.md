


# 🧙‍♂️ Chapéu Seletor de Hogwarts (Python CLI Edition)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Este é um sistema console desenvolvido em **Python** que simula o famoso Chapéu Seletor do universo de Harry Potter. O projeto permite gerenciar o cadastro de alunos (com persistência de dados em arquivos locais) e determina de forma automatizada a qual casa de Hogwarts (*Grifinória, Sonserina, Corvinal ou Lufa-Lufa*) o aluno pertence, baseando-se em um questionário comportamental de 5 perguntas objetivas.

> 📊 **Nota de Evolução:** Este projeto foi originalmente concebido em Java (Orientado a Objetos estruturado), passou por experimentos em ecossistema PHP/Laravel e agora foi totalmente refatorado para Python, aplicando as melhores práticas de organização de pacotes, módulos e ambientes isolados.

---

## 🛠️ Funcionalidades

*   **[1] Cadastrar Aluno + Sorting Hat:** Registra o aluno (Nome, Idade, Status de Sangue) e inicia o questionário dinâmico. O sistema calcula as respostas e define a casa ideal.
*   **[2] Remover Aluno:** Exclui um aluno do registro através do seu identificador/nome.
*   **[3] Exibir Aluno:** Busca detalhada exibindo a ficha do aluno e a heráldica (Escudo em ASCII Art) da sua respectiva casa.
*   **[4] Listar todos os Alunos:** Exibe a lista completa de bruxos matriculados e suas respectivas casas.
*   **[5] Atualizar Aluno:** Permite alterar dados cadastrais (como idade ou status de sangue) sem afetar a casa já selecionada.

---

## 📂 Estrutura de Pastas e Arquivos Explicada

O projeto adota o padrão de mercado para aplicações Python, separando as responsabilidades em módulos distintos dentro do diretório `src/` (Source):

```text
chapeu_seletor/
│
├── .venv/                      # Ambiente virtual isolado (dependências do projeto)
│
├── src/                        # Código-fonte principal da aplicação
│   ├── __init__.py             # Inicializador que transforma a pasta em um pacote Python
│   ├── main.py                 # Ponto de entrada (Entry Point). Apenas inicializa o sistema
│   ├── sistema.py              # Orquestrador/Maestro. Gerencia o menu e o fluxo do usuário
│   │
│   ├── gerenciadores/          # Camada de Persistência (I/O de Arquivos)
│   │   ├── __init__.py
│   │   └── gerenciador_aluno.py # Cuida da leitura, escrita e deleção dos dados no arquivo .txt
│   │
│   ├── modelos/                # Entidades e Regras de Negócio
│   │   ├── __init__.py
│   │   ├── aluno.py            # Definição da classe Aluno (atributos e propriedades)
│   │   └── cadastro.py         # Validações de regras de cadastro
│   │
│   └── casas/                  # Módulo de Polimorfismo e Arte
│       ├── __init__.py
│       ├── interface_casa.py   # Classe abstrata (molde) usando o módulo nativo 'abc'
│       ├── grifinoria.py       # Regras específicas e ASCII Art da Grifinória
│       ├── sonserina.py        # Regras específicas e ASCII Art da Sonserina
│       ├── corvinal.py         # Regras específicas e ASCII Art da Corvinal
│       └── lufalufa.py         # Regras específicas e ASCII Art da Lufa-Lufa
│
├── dados/                      # Banco de dados em texto plano
│   └── alunos.txt              # Arquivo onde os registros são salvos de forma persistente
│
├── .gitignore                  # Arquivos ignorados pelo Git (como a pasta .venv/)
├── README.md                   # Documentação do projeto
└── requirements.txt            # Lista de dependências externas do projeto

```

### Detalhamento dos Componentes Principais:

1. **`src/main.py`**: Seguindo boas práticas de arquitetura, este arquivo funciona estritamente como um "interruptor". Ele não processa lógica, apenas importa e executa a função principal contida em `sistema.py`.
2. **`src/sistema.py`**: Atua como o controlador da interface de linha de comando (CLI). Ele roda o loop principal (`while True`), renderiza as opções do menu e faz a ponte entre o usuário e as regras de negócio.
3. **`src/casas/interface_casa.py`**: Como o Python não possui a palavra-chave nativa `interface` (como o Java), utilizamos a biblioteca interna `abc` (*Abstract Base Classes*). Ela força com que todas as casas herdem a mesma estrutura e implementem obrigatoriamente métodos como `exibir_escudo()`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior instalado na máquina.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/seu-usuario/Chapeu-Seletor-De-Hogwarts.git](https://github.com/seu-usuario/Chapeu-Seletor-De-Hogwarts.git)
cd Chapeu-Seletor-De-Hogwarts

```

### 2. Configurar o Ambiente Virtual (`.venv`)

O ambiente virtual garante que as dependências deste projeto não entrem em conflito com outras aplicações do seu computador.

**No Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate

```

**No Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

```

### 3. Instalar Dependências

*(Se houver pacotes externos listados no arquivo)*

```bash
pip install -r requirements.txt

```

### 4. Executar a Aplicação

Para que o interpretador do Python consiga mapear corretamente as importações absolutas (`from src.pasta import ...`), **você deve rodar o comando a partir da raiz do projeto**, utilizando a flag de módulo (`-m`):

```bash
python -m src.main

```

---

## 🛠️ Conceitos de Programação Aplicados

* **POO (Programação Orientada a Objetos):** Utilização de classes para representar entidades do mundo real (Alunos e Casas) com encapsulamento de atributos.
* **Polimorfismo / Classes Abstratas:** Implementação do módulo `abc` para garantir contratos de interface uniformes entre as diferentes casas de Hogwarts.
* **Manipulação de Arquivos (File I/O):** Uso de gerenciadores de contexto (`with open()`) em Python para ler e salvar de forma segura os dados cadastrais em formato `.txt`.
* **Modularização:** Separação estrita de responsabilidades em arquivos independentes, facilitando futuras manutenções e acoplamento de novas interfaces (como Web ou GUI).

