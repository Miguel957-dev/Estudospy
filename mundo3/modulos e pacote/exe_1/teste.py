import moedas

v = float(input('Digite um valor: '))
print(f'O dobro de {v} é de {moedas.dobro(v)}')
print(f'A metade de {v} é de {moedas.metade(v)}')
print(f'Aumentando {v} em 10% fica {moedas.aumentar(v)}')
print(f'Diminuindo 13% de {v} fica {moedas.diminuir(v)}')
