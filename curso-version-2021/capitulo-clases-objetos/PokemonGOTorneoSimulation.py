class Pikachu:

    cantidadVida = 100

    def impactTrueno(self, oponente):
        oponente.cantidadVida = oponente.cantidadVida - 40

class Mewtwo:

    cantidadVida = 100

    def psicocorte(self, oponente):
        oponente.cantidadVida = oponente.cantidadVida - 70

    def recover(self):
        self.cantidadVida = 100

print("Combate entre Mewtwo & Pikachu")
print("========================")
pika = Pikachu()
mewtwo = Mewtwo()
pika.impactTrueno(mewtwo)
print("Mewtwo golpeado, ahora tiene", mewtwo.cantidadVida, "de vida" )
print("Mewtwo se enojo, mewtwo quiere usar psicocorte")
mewtwo.psicocorte(pika)
print("Pikachu ha sufrido un impacto fuerte")
