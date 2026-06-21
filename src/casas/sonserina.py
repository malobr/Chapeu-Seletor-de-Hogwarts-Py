from interface_casa import Casa

class Sonserina(Casa):
    def __init__(self):
        super().__init__(
            nome = "Sonserina",
            fundador = "Salazar Slytherin",
            cor = "Verde e Prata",
            slogan="Astucia e ambição",
            bandeira="▄▄▀█▄───▄───────▄\n" +
                     "▀▀▀██──███─────███\n" +
                     "░▄██▀░█████░░░█████░░\n" +
                     "███▀▄███░███░███░███░▄\n" +
                     "▀█████▀░░░▀███▀░░░▀██▀"
            )
