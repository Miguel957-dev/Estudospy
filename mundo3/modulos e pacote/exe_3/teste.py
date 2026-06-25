import moedas

v = float(input('Digite um valor: '))
print(f'O dobro de {moedas.moeda(v)} é de {moedas.dobro(v, True)}')
print(f'A metade de {moedas.moeda(v)} é de {moedas.metade(v, True)}')
print(f'Aumentando {moedas.moeda(v)} em 10% fica {moedas.aumentar(v, 10, True)}')
print(f'Diminuindo 13% de {moedas.moeda(v)} fica {moedas.diminuir(v, 13, True)}')
