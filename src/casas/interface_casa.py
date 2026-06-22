class Casa:

    def __init__(self, nome, fundador, cor, slogan, senha, bandeira):

        self.nome = nome
        self.fundador = fundador
        self.cor = cor
        self.slogan = slogan
        self.bandeira = bandeira
        self.senha = senha
        self.alunos = []

    def obterQuantidadeAlunos(self):
        return len(self.alunos)

    def exibirArte(self):
        return self.bandeira
    
    def informarSenha(self):
        return self.senha

    def __str__(self):
        return f"Nome: {self.nome}\nFundador: {self.fundador}\nCor: {self.cor}\nSlogan: {self.slogan}\nSenha: {self.senha}\nBandeira: {self.exibirArte()}\nAlunos: {self.obterQuantidadeAlunos()}"