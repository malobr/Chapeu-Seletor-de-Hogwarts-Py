class Casa:

    def __init__(self, nome, fundador, cor, slogan, senha, bandeira):

        self.nome = nome
        self.fundador = fundador
        self.cor = cor
        self.slogan = slogan
        self.bandeira = bandeira
        self.senha = senha
        self.qtdAlunos = []

    def obterQuantidadeAlunos(self):
        return len (self.qtdAlunos)

    def exibirArte(self):
        return self.bandeira