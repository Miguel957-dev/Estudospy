from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia = 0, frete = 0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calcula_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia, frete = 0):
        super().__init__(distancia, frete)
        self.distancia = distancia
        self.frete = frete

    def calcula_frete(self):
        fator = 0.50
        self.frete = self.distancia * fator
        print(f"O valor do frete de moto de {self.distancia} vai ser de {self.frete}")



class Caminhao(Transporte):
    def __init__(self, distancia, frete = 0):
        super().__init__(distancia, frete)
        self.distancia = distancia
        self.frete = frete 

    def calcula_frete(self):
        fator = 1.20
        if self.distancia < 50:
            print("Não é possivel fazer frete em distância menores de 50KM ")
        else:
            self.frete = self.distancia * fator
            print(f"O valor do frete de caminhão de {self.distancia} vai ser de {self.frete}")

class Drone(Transporte):
    def __init__(self, distancia, frete):
            super().__init__(distancia, frete = 0)
            self.distancia = distancia
            self.frete = frete

    def calcula_frete(self):
        fator = 9.50
        if self.distancia > 10:
            print("Não é possivel realixar frete de drone em distancia acima de 10 KM.")
        else:
            self.frete = self.distancia * fator
            print(f"O valor do frete de Drone de {self.distancia} vai ser de {self.frete}")
        
    