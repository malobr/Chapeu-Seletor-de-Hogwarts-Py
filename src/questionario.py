numeroMatricula = 0
alunosCadastrados = []#Criando uma lista de alunos para a sala comunal...

def sistema():
    
    def chapeuSeletor():
        print("")
        print("--──────--▄▀▀▄")
        print("---──────▄▀▄░▀▄")
        print("--──────▄▀▄░░░░▀▄")
        print("--──────▄▀▄░░░░░░▀▄")
        print("--─────▄█░░░░░░░░░█▄")
        print("--─▄▄──█░░░░░░░░░░░█──▄▄")
        print("--█▄▄██░░▀░░░░░░░░▀░░██▄▄█")
        print("--Chapeu Seletor de Hogwarts--")

    def exibirMenu():
        chapeuSeletor()
        print("1 - Cadastrar Novo Aluno")#Cadastro e quiz
        print("2 - Sala Comunal")#Lista de alunos por casa, Ver infos, editar e Duelar
        print("3 - Cadastrar Professor")#Cadastro de professor
        print("4 - Area do Professor")#Painel do professor, Sala de aula, Alunos por turma...
        print("0 - Sair")#Sair
        opcao = input("Digite uma opção: ")
        return opcao
    
    def verificarOpcao(opcao):
        if opcao == "1":
            cadastrarAluno()
        elif opcao == "2":
            salaComunal()
        elif opcao == "3":
            cadastrarProfessor()
        elif opcao == "4":
            areaDoProfessor()
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida!")
    
    def cadastrarAluno():
        global numeroMatricula
        # Iniciando os contadores das casas em 0
        grifinoria = 0
        sonserina = 0
        corvinal = 0
        lufalufa = 0

        print("\nHmmm, interessante... Me diga mais sobre voce.\nBem-vindo ao Chapéu Seletor de Hogwarts!")
        
        nome = input("\nInforme seu nome:\n")
        
        try:# definindo que apenas numeros sao permitidos...
            idade = int(input("\nInforme sua idade:\n"))
        except ValueError:
            print("\nErro: Idade deve ser um número inteiro.")
            return
            
        sexo = input("\nInforme seu sexo:\n")
        statusSangue = input("\nInforme seu Status de Sangue (Puro ou Trouxa):\n")
        
        numeroMatricula = len(alunosCadastrados) + 1 # Adicionando +1 para o proximo aluno, com base na lista atual de alunos...


        print("\nResponda às seguintes perguntas para descobrir sua casa.")

        def computarPonto(resposta):#Criando funcao para calcular pontos para cada resposta...
            nonlocal grifinoria, sonserina, corvinal, lufalufa
            if resposta == 1:
                grifinoria += 1
            elif resposta == 2:
                sonserina += 1
            elif resposta == 3:
                corvinal += 1
            elif resposta == 4:
                lufalufa += 1
            else:
                print("Resposta inválida!")

        #Pergunta 1
        print("\nPergunta 1: Qual dessas qualidades você mais valoriza?")
        print("1. Coragem\n2. Ambição\n3. Inteligência\n4. Lealdade")
        computarPonto(int(input("\nDigite o número da sua resposta:\n")))

        #Pergunta 2
        print("\nPergunta 2: Qual dessas criaturas mágicas você prefere?")
        print("1. Fênix\n2. Serpente\n3. Coruja\n4. Texugo")
        computarPonto(int(input("\nDigite o número da sua resposta:\n")))
        #Pergunta 3
        print("\nPergunta 3: Qual dessas matérias você mais gosta?")
        print("1. Defesa Contra as Artes das Trevas\n2. Poções\n3. Feitiços\n4. Herbologia")
        computarPonto(int(input("\nDigite o número da sua resposta:\n")))

        #Pergunta 4
        print("\nPergunta 4: Qual desses lugares você preferiria explorar?")
        print("1. A Floresta Proibida\n2. As Masmorras\n3. A Torre da Corvinal\n4. A cozinha dos elfos domésticos")
        computarPonto(int(input("\nDigite o número da sua resposta:\n")))

        #Pergunta 5
        print("\nPergunta 5: Qual dessas palavras melhor descreve você?")
        print("1. Destemido\n2. Astuto\n3. Sábio\n4. Trabalhador")
        computarPonto(int(input("\nDigite o número da sua resposta:\n")))

        pontuacoes ={
            "Grifinoria": grifinoria,
            "Sonserina": sonserina,
            "Corvinal": corvinal,
            "Lufalufa": lufalufa
        }
        nomeCasa = max(pontuacoes, key=pontuacoes.get)

        print(f"\nO Chapéu Seletor grita: {nomeCasa.upper()}!")

        if nomeCasa == "Sonserina":
            casaEscolhida = Sonserina()
        elif nomeCasa == "Grifinoria":
            casaEscolhida = Grifinoria() 
        elif nomeCasa == "Corvinal":
            casaEscolhida = Corvinal()   
        else:
            casaEscolhida = LufaLufa()


        novoAluno = {#Criando um dicionário para armazenar as informações do novo aluno...
        "matricula": numeroMatricula,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "statusSangue": statusSangue,
        "casa": casaEscolhida 
        }

        alunosCadastrados.append(novoAluno)#Adicionando o novo aluno a lista de alunos... 

        print(f"\nAluno {nome} cadastrado com sucesso! Sua matrícula é: {numeroMatricula:06}")
        print("-" * 40)
        print(casaEscolhida.exibirArte())
        print(f"\nBem-vindo à {casaEscolhida.nome}!")
        print(f"A senha da sua Sala Comunal é: ** {casaEscolhida.informarSenha()} **")
        print("-" * 40)        
        
    def salaComunal():

        print(f"\n-----Entrada da Sala Comunal-----\n")

        try:
            matriculaDigitada = int(input("Informe a sua matrícula:\n"))
        except ValueError:
            print("Matrícula inválida! Digite apenas números.")
            return
        
        alunoEncontrado = None
        for aluno in alunosCadastrados:
            if aluno ["matricula"] == matriculaDigitada:
                alunoEncontrado = aluno
                break
        
        if alunoEncontrado != None:
            casaDoAluno = alunoEncontrado["casa"]
        
            print(f"\nVoce esta diante da porta da Sala Comunal de {casaDoAluno.nome}!")
            print(casaDoAluno.exibirArte())
            senhaDigitada = input("\nInforme a senha da Sala Comunal:\n")

            if senhaDigitada == casaDoAluno.informarSenha():
                    print("\n" + "="*40)
                    print("A passagem se abre...")
                    print("="*40)
                    print(casaDoAluno.exibirArte())
                    print(f"\nBem-vindo(a) de volta à {casaDoAluno.nome}, {alunoEncontrado['nome']}!")
                    
                    # --- AQUI COMEÇA O MENU INTERNO DA SALA COMUNAL ---
                    print("\n1 - Ver minhas informações")
                    print("2 - Duelar (Em breve)")
                    print("0 - Voltar aos corredores de Hogwarts")
                    
                    opcaoSala = input("O que deseja fazer? ")
                    
                    if opcaoSala == 1:
                        print(f"\nNome: {alunoEncontrado['nome']}")
                        print(f"Idade: {alunoEncontrado['idade']}")
                        print(f"Sangue: {alunoEncontrado['statusSangue']}")
                        print(f"Casa: {casaDoAluno.nome}")
                        print(f"Fundador: {casaDoAluno.fundador}")
                    elif opcaoSala == 0:
                        print("Saindo da Sala Comunal...")
                    else:
                        print("Opção inválida ou em desenvolvimento.")
                    
            else:
                print("\nSenha incorreta! A entrada permanece fechada.")
        else:
            print("\nMatrícula não encontrada. O Chapéu Seletor não lembra de você!")
        
    
