from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def ferver_agua(self):
        print('1. Fervendo a água ate 100 graus Celsius.')


    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
        print('---INICIANDO O PREPARO---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('---BEBIDA PRONTA---')
        print('')

class Cafe(BebidaQuente):

    def misturar(self):
        print("2. Passando a água pressurizado pelo pó de café moido.")

    def servir(self):
        print("3. Servindo em xícara pequena.")

    def preparar(self):
        super().preparar()


class Cha(BebidaQuente):

    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na canelca de porcelana com limão.")

    def preparar(self):
        super().preparar()

class Leite(BebidaQuente):

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")

    def preparar(self):
        super().preparar()