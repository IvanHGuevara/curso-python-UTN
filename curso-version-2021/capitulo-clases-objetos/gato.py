class Gato:

    anios = 0
    kmsRecorridos = 0

    def cumplirAnios(self):
        self.anios = self.anios + 1
    
    def correr(self, kms):
        self.kmsRecorridos = self.kmsRecorridos + kms

mora = Gato()
print("Tengo", mora.anios, "anios")
mora.cumplirAnios()
print("Tengo", mora.anios, "anios")
mora.correr(10)
print("Corri", mora.kmsRecorridos, "kms")
