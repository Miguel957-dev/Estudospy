from time import sleep
from rich import print

class Livro:

    def __init__(self, titulo = '', paginas_do_livro = 0):

        self.titulo = titulo
        self.paginas_do_livro = paginas_do_livro
        self.contador = 1
        

    def avançar_paginas(self, paginas):
        destino = self.contador + paginas
        if self.contador == 1:
            print(f"[blue]Você acabou de abrir o livro '[red]{self.titulo}[/red]' que tem [green]{self.paginas_do_livro}[/green] páginas no total. Você agora está na [yellow]página 1.[/yellow] [/blue]")
        
        if destino <= self.paginas_do_livro:
            for p in range(self.contador + 1 , destino + 1):
                if p == destino:
                    print(f'Pág{p} ▶ [blue]Você avançou {paginas} páginas e agora está na [/blue][yellow] página {destino}[/yellow]')
                    sleep(0.5)
                else:print(f'Pág{p} ▶ ', end= '') 
                sleep(0.5) 
            self.contador += paginas
        
        if destino > self.paginas_do_livro:
            self.paginas_do_livro += 1
            for p in range(self.contador + 1 , self.paginas_do_livro):
                if self.contador == self.paginas_do_livro:
                    print(f'Pág{p} ▶ [blue]Você avançou {paginas} páginas e agora está na [/blue][yellow] página {destino}[/yellow]', end= '')
                    sleep(0.5)
                else: print(f'Pág{p} ▶ ', end= '')
                sleep(0.5)
            self.contador += paginas
            print('[red]Você ultrapassou o número de paginas exitente no livro. [/red]')




l1 = Livro('Principe',  20)
l1.avançar_paginas(5)
l1.avançar_paginas(7)
l1.avançar_paginas(10)