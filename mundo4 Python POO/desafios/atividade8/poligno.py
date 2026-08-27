from abc import ABC, abstractmethod

class Poligno(ABC):
    def __init__(self, qtd_lado = 0):
        self.qtd_lado = qtd_lado


    @abstractmethod
    def perimetro(self):
        pass


    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligno):
    def __init__(self,qtd_lado):
        super().__init__(qtd_lado)
        self.qtd_lado = qtd_lado

    def perimetro(self):
        valor_perimetro = self.qtd_lado * 4
        print(f"O perímetro do quadrado é {valor_perimetro}") 

    def area(self):
        valor_area = self.qtd_lado ** 2
        print(f"A area do quadrado é {valor_area}")

class Circulo(Poligno):
    def __init__(self, qtd_lado):
        super().__init__(qtd_lado)
        self.raio = self.qtd_lado

    def perimetro(self):
        valor_perimetro = self.raio * 3.14 * 2
        print(f"O valor do perímetro é {valor_perimetro}.")

    def area(self):
        valor_area = (self.raio ** 2 )* 3.14
        print(f"O valor da area é {valor_area}")