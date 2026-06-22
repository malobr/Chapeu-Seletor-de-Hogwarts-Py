from interface_casa import Casa

class Grifinoria(Casa):
    def __init__(self):
        super().__init__(
            nome = "Grifinoria",
            fundador = "Godric Griffindor",
            cor = "Vermelho e Dourado",
            slogan="Onde habitam os bravos de coração",
            senha = "Coragem",
            bandeira =   "──▄▀▀▀▀▀───▄█▀▀▀█▄\n" +
                        "──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n" +
                        "──▐▒▒▒▒▒▒▒▒███▌▀▐███\n" +
                        "───▌▒▓▒▒▒▒▓▒██▌▀▐██\n" +
                        " ───▌▓▐▀▀▀▀▌▓─▀▀"
        )