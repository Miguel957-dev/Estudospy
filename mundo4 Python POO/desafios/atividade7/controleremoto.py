from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5


    def __init__(self,  canal = 3, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def ligar_desligar(self):
        self.ligado = not self.ligado

    def mostrar_tv(self):
        
        conteudo = ''
        if not self.ligado:
            conteudo = f"[red]A TV está desligada[/red]"
        else:
            conteudo = f"[green]CANAL = [/green]"
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f" [black on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "



        tv = Panel(conteudo, title = "[TV]")
        print(tv)

c = ControleRemoto()
c.ligar_desligar()
c.mostrar_tv()