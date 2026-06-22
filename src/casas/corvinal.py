from interface_casa import Casa

class Corvinal(Casa):
    def __init__(self):
        super().__init__(
            nome = "Corvinal",
            fundador = "Rowena Ravenclaw",
            cor = "Azul e Bronze",
            slogan = "Sabedoria sem limites",
            senha = "Curiosidade",
            bandeira =  "                __\n" +
                        "               /'{>\n" +
                        "           ____) (____\n" +
                        "         //'--;   ;--'\\\\\n" +
                        "        ///////\\_/\\\\\\\\\\\\\n" +
                        "                m m"
        )