import moedas

v = float(input('Digite um valor: '))
print(f'O dobro de {moedas.moeda(v)} é de {moedas.moeda(moedas.dobro(v))}')
print(f'A metade de {moedas.moeda(v)} é de {moedas.moeda(moedas.metade(v))}')
print(f'Aumentando {moedas.moeda(v)} em 10% fica {moedas.moeda(moedas.aumentar(v))}')
print(f'Diminuindo 13% de {moedas.moeda(v)} fica {moedas.moeda(moedas.diminuir(v))}')
