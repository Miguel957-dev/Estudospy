from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 10


    def __init__(self,  canal = 1, volume = 1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual > ControleRemoto.canal_min:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual < ControleRemoto.volume_max:
                self.volume_atual += 1
                
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                self.volume_atual = self.volume_atual

            else:
                self.volume_atual -= 1


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
                    conteudo += f" [yellow on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan]  [/]"
                else:
                    conteudo += f"[black on white]  [/]"


        tv = Panel(conteudo, title = "[TV]", width = 30)
        print(tv)

c = ControleRemoto(3, 7)
c.ligar_desligar()
c.mostrar_tv()