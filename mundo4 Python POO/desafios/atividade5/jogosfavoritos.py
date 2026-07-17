from rich import print
from rich.panel import Panel

class Gamer:
    
    def __init__(self, nome = '', nick = ''):

        self.nome = nome
        self.nick = nick
        self.jogo_favorito = list()


    def add_jogos_favorito(self, jogo = ''):
        self.jogo_favorito.append(jogo)
        self.jogo_favorito.sort()
        
    def ficha(self):
        conteudo = f'Nome real {self.nome}'
        conteudo += '\n Jogos Favoritos'
        for num, game in enumerate(self.jogo_favorito):
            conteudo += f"\n:video_game:[blue] {game}[/blue] "
        painel = Panel(conteudo, title=f'Jogador {self.nick}')
        print(painel)
j1 = Gamer('Miguel', 'Ninja123')
j1.add_jogos_favorito('God of war')
j1.ficha()