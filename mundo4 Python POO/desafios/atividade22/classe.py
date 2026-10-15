from rich import print
from rich.panel import Panel
from abc import ABC

class Mensagem(ABC):
    def __init__(self, msg:str = '', tipo:str = '', aviso:str = ':speech_balloon:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = aviso

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo} {self._icone}", style="#ffffff on #000000",width=50)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg = ''):
        super().__init__(msg, tipo = 'alerta', aviso = ':warning:')

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo} {self._icone}", style="#000000 on #fffc1b",width=50)
        print(msg)

class Erro(Mensagem):
    def __init__(self, msg = ''):
        super().__init__(msg, tipo = 'erro', aviso = ':prohibited:')

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo} {self._icone}", style="#ffff00 on #880000",width=50)
        print(msg)