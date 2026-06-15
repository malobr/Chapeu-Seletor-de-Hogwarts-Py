1. Arquivos de Inicialização e Fluxo (As Telas)
Estes arquivos controlam o que o usuário vê na tela preta do terminal. Eles usam muito print(), input() e loops while.

📂 src/main.py (O Botão de Ligar)
O que faz: É o arquivo mais curto do projeto. Ele serve apenas como o ponto de entrada da aplicação.

O que tem dentro: * Um import chamando a função principal do sistema.py.

O bloco padrão do Python if __name__ == '__main__': que inicia a execução.

Nenhuma lógica, nenhuma pergunta e nenhum menu ficam aqui.

📂 src/sistema.py (O Menu Principal e Público)
O que faz: Controla a primeira tela que qualquer usuário vê ao abrir o programa.

O que tem dentro:

Um loop while True mostrando as opções: [1] Ser Selecionado (Cadastrar Aluno), [2] Área do Professor e [0] Sair.

A lógica para capturar os dados iniciais do Aluno (nome, idade, status_sangue, sexo).

A chamada para o arquivo do questionário. Após o questionário dar o resultado da casa, ele cria o objeto Aluno e chama o gerenciador para salvar no arquivo .txt.

A tela de login para a Área do Professor (pede nome e senha e valida).

📂 src/menu_professor.py (O Menu Restrito)
O que faz: É o painel de controle que só abre se o professor digitar a senha correta no sistema.py.

O que tem dentro:

Um loop while True próprio, com o menu da diretoria: [1] Cadastrar Novo Professor, [2] Gerenciar Alunos (Listar/Editar/Excluir), [3] Gerenciar Turmas e [4] Voltar.

Ele importa e direciona as ações para os gerenciadores específicos (g_aluno.py, g_professor.py, g_turma.py).

2. O Módulo de Lógica Pura (O Algoritmo)
📂 src/questionario.py (O Chapéu Seletor)
O que faz: Contém o algoritmo do questionário que pontua e define a casa do aluno.

O que tem dentro:

Uma função chamada fazer_questionario().

As 5 perguntas objetivas com seus respectivos print() e input().

Um dicionário de pontos: pontos = {"Grifinória": 0, "Sonserina": 0, ...}.

Estruturas condicionais (if/elif) para somar pontos nas casas baseadas nas respostas.

A lógica final (usando a função max()) para retornar apenas o texto com o nome da casa vencedora.

3. A Camada de Modelos (Os Moldes/Classes)
Esses arquivos definem como as informações serão estruturadas na memória do computador. Eles não têm print nem input.

📂 src/modelos/aluno.py (A Classe Aluno)
O que tem dentro: * A definição da classe Aluno com o método construtor (def __init__).

Atributos: nome, idade, status_sangue, sexo e casa.

📂 src/modelos/professor.py (A Classe Professor)
O que tem dentro: * A definição da classe Professor.

Atributos: nome, casa, status_sangue, materia e senha.

📂 src/modelos/turma.py (A Classe Turma)
O que tem dentro: * A definição da classe Turma.

Atributos: nome_turma, materia, professor (que vai receber um objeto da classe Professor) e lista_alunos (que nasce como uma lista vazia [] e vai guardando os objetos da classe Aluno).

4. A Camada de Gerenciadores (O CRUD e Arquivos .txt)
Estes arquivos fazem o trabalho pesado de salvar e ler o "banco de dados" em texto plano (.txt). Eles usam comandos como with open().

📂 src/gerenciadores/g_aluno.py (CRUD do Aluno)
O que faz: Manipula o arquivo dados/alunos.txt.

O que tem dentro:

Função salvar(aluno): Transforma o objeto Aluno em uma linha de texto (ex: Harry;11;Mestiço;Masculino;Grifinória) e escreve no fim do arquivo .txt.

Função listar(): Lê o arquivo .txt, quebra as linhas e exibe os alunos bonitinho na tela.

Função excluir(nome): Lê o arquivo inteiro, remove a linha do aluno escolhido e reescreve o arquivo.

Função editar(nome): Localiza o aluno e permite reescrever seus dados (idade, status de sangue, sexo).

📂 src/gerenciadores/g_professor.py (CRUD do Professor e Autenticação)
O que faz: Manipula o arquivo dados/professores.txt.

O que tem dentro:

Funções de cadastrar, listar, editar e excluir professores (igual ao do aluno).

Função autenticar(nome, senha): Uma função crucial que o sistema.py vai chamar. Ela abre o arquivo de professores, procura pelo nome digitado e verifica se a senha bate. Retorna True se estiver correto ou False se estiver errado.

📂 src/gerenciadores/g_turma.py (CRUD da Turma)
O que faz: Manipula o arquivo dados/turmas.txt ou gerencia as turmas ativas na memória.

O que tem dentro:

Função para criar uma turma vinculando um Professor a ela.

Função adicionar_aluno_na_turma(nome_aluno, nome_turma): Procura o aluno no sistema e o joga para dentro da lista daquela turma.

Função para exibir o relatório da turma (mostra o nome da turma, a matéria, o nome do professor e faz um loop listando todos os alunos daquela turma).

5. Arquivos de Configuração
📂 requirements.txt
O que faz: Lista de bibliotecas externas. Como seu projeto usa lógica pura e manipulação de arquivos nativa, este arquivo pode ficar vazio por enquanto.

📂 .gitignore
O que faz: Diz para o Git ignorar a pasta .venv/ e os arquivos .txt com dados de teste na hora que você der git push para o GitHub.

Resumo da ópera:
Se você clicar em src/modelos/aluno.py, você só verá a estrutura do aluno. Se clicar em src/questionario.py, só verá as perguntas. Essa separação cirúrgica é o que chamamos no mercado de Código Limpo (Clean Code).