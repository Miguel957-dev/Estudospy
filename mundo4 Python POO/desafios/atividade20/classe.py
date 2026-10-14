from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self,nome:str, tamanho:int, extensao:str = ''):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f'{self.nome}.{self._extensao}'

class DOC(Arquivo):
    def __init__(self, nome, tamanho, extensao = 'docx'):
        super().__init__(nome, tamanho, extensao)


class PDF(Arquivo):
    def __init__(self, nome, tamanho, extensao = 'pdf'):
        super().__init__(nome, tamanho, extensao)
        

def abrir_arquivo(arquivo_recebido):
    print(f"Abrindo o arquivo '{arquivo_recebido.nome_completo}'({arquivo_recebido.tamanho/1000000}MB)  no Adobe Reader") 