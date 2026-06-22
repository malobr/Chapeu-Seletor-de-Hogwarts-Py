from ..casas.interface_casa import Casa
class Aluno:
    def __init__(self, nome, idade, statusSangue, sexo, matricula, casa=None):
        self.nome = nome
        self.idade = idade
        self.status_sangue = status_sangue
        self.sexo = sexo
        self.matricula = matricula
        self.casa = casa

    def setCasa(self, casa):
        self.casa = casa

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nStatus de Sangue: {self.statusSangue}\nSexo: {self.sexo}\nMatricula: {self.matricula}\nCasa: {self.casa.nome}"