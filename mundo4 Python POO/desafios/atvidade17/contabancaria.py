from hashlib import sha256


class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos agora melhorada com senha usando o sha-256
    """
    
    def __init__(self, id:int, nome:str=None, saldo:float = 0, chave:str = None):
        self._id = id #protegido
        self._titular = nome #protegido
        self.__saldo = saldo #privado
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self) -> str:
        from pwinput import pwinput
        while True:
            senha = str(pwinput('Senha: ')).strip()
            if len(senha) >=6:
                break
        return senha 

    def __str__(self):
        return f"O estado atual da conta {self.__dict__}"

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso na conta {self._id}")

