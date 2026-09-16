from rich import print

class Diario():
    def __init__(self, diario=None, senhamestra = 'linda'):
        if diario is None:
            self.__diario = []
            self.__senha = senhamestra.strip()
        else:
            self.__diario = diario
            self.__senha = senhamestra.strip()

    def escrever(self, txt):
        txt.strip()
        if isinstance(txt, str) and len(txt) > 0:
            self.__diario.append(txt)

    def ler(self, senha = ""):
        senha.strip()
        if senha != self.__senha:
            raise PermissionError("!Senha é inválida, Você não pode ler o diário!")

        else:
            print('[green]DIÁRIO LIBERADO![/green]')
            for p in self.__diario:
                print(f'- {p}')
    @property
    def senha(self):
        raise PermissionError("Senha é inválida, Você não pode ler o diário")

    @senha.setter
    def senha(self, novasenha):
        pass