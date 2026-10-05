class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz pudim com leite codensado e calda')

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no oleo de soja.")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com ninho e nutella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} fritar coxinha na air Fryer")