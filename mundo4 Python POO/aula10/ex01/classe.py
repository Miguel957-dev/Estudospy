from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possivel analisar o {valor}')

    @analisar.register
    def _analisar(self, valor:int):
        print(f"{valor} é um número Inteiro")

    @analisar.register
    def _analisar(self, valor:float):
        print(f'{valor} é uma número com casas decimais.')

    @analisar.register
    def _analisar(self, valor:str):
        print(f'{valor} é uma cadeia de caracteres.')
        