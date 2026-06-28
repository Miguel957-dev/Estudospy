class ContaBancaria:
    """Cria uma conta bancaria para saque e depositos"""

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} crida com sucesso. Saldo atual de R${self.saldo:.2f}')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de valor R${valor:,.2f} autorizado na conta {self.id}')
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICENTE.')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} autorizado na conta {self.id}')


c1 = ContaBancaria(112, 'Miguel', 300)
c1.deposito(500)
c1.sacar(900000)
print(c1)