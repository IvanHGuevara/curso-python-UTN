class Raton:

    anios = 0
    kmsEscapados = 0

    def cumplirAnios(self):
        self.anios = self.anios + 1

    def escapar(self, kms):
        self.kmsEscapados = self.kmsEscapados + kms

mickey = Raton()
print("Tengo", mickey.anios, "anios")
mickey.escapar(10)
print("Me escape y estoy a", mickey.kmsEscapados, "kms")