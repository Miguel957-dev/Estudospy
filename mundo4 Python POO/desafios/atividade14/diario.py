from rich import print

class Diario():
    def __init__(self, diario=None):
        if diario is None:
            self.__diario = []
        else:
            self.__diario = diario

    def escrever(self, txt = ''):
        self.__diario.append(txt)

    def ler(self, senha = ""):
        if senha == "123":
            print('[green]DIÁRIO LIBERADO![/green]')
            for p in self.__diario:
                print(f'- {p}')

        else:
            raise PermissionError("Senha é inválida, Você não pode ler o diário")
    @property
    def senha(self):
        raise PermissionError("Senha é inválida, Você não pode ler o diário")
    