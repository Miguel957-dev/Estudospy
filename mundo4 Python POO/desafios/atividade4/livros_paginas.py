from time import sleep
from rich import print

class Livro:

    def __init__(self, titulo = '', paginas_do_livro = 0):

        self.titulo = titulo
        self.paginas_do_livro = paginas_do_livro
        self.contador = 1
        

    def avançar_paginas(self, paginas):
        destino = self.contador + paginas
        
        if destino <= self.paginas_do_livro:
            for p in range(self.contador + 1 , destino + 1):

                print(p)
            self.contador += paginas
        
        if destino > self.paginas_do_livro:
            self.paginas_do_livro += 1
            for p in range(self.contador + 1 , self.paginas_do_livro):
                print(p)
            self.contador += paginas
            print('[red]Você ultrapassou o número de paginas exitente no livro. [/red]')




l1 = Livro('Principe',  20)
l1.avançar_paginas(5)
l1.avançar_paginas(20)