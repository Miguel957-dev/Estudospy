from abc import ABC, abstractmethod
#POLIMOSFISMO DE INCLUSÃO, QUANDO UM METODO SOBRESCREVE UM METODO DA MÃE

class Animal(ABC):
    def __init__(self, nome:str=""):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som.")

class Pato(Animal):
    pass

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer, AU! AU! AU!")


class Splitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome}, acabou de dizer, AU AU AU")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome}, acabou de dizer, RUF RUF RUF")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer, MIAU!")

class Galinha(Animal):
    pass

