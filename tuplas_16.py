
'''

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis' , 'sete', 'oito', 'nove' , 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num > 20:
        print('Tente novamente. ', end=(''))
    else:
        break
print(f'Você digitou o número {números[num]}.')


colocação = ('Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Mirassol', 'Palmeiras', 'Remo', 'Santos', 'São Paulo', 'Vasco', 'Vitória')
print('-='*20)
print(f'Lista dos times do Brasileirão é {colocação}')
print('-='*20)
print(f'Os 5 primeiros são {colocação[0:5]}')
print('-='*20)
print(f'Os 4 ultimos são {colocação[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabetica é {sorted(colocação)}')
print('-='*20)
print(f'O {colocação[7]} está na oitava colocação!')



from random import randint

numeros = (
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100)
)

print('Números gerados:')
for n in numeros:
    print(n, end=' ')

print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')


numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')),)

print(f'O 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'A posição que o 3 apareceu pela primeira vez foi {numeros.index(3)+ 1}ª posição.') 
else:
    print('O valor 3 não foi digitado')
print('Os números pares digitados foram ', end=(''))
for n in numeros:
    if n % 2 == 0:
        print(f'{n}, ', end=(''))


print('-'*40)
print('          LISTAGEM DE PREÇOS')
print('-'*40)

listagem =('LAPÍS', 1.75,
      'BORRACHA', 2.00,
      'CADERNO', 15.90, 
      'ESTOJO', 25.00,
      'TRANFERIDOR', 4.20,
      'COMPASSO', 9.99,
      'MOCHILA', 120.32,
      'CANETAS', 22.30,
      'LIVRO', 34.90)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=(''))
    else:
        print(f'R${listagem[pos]:>5.2f}')

print('-'*40)
'''

palavras = (
    "Algoritmo", "Montanha", "Enigma", "Cafe", "Satelite", 
    "Horizonte", "Código", "Neblina", "Piquenique", "Galáxia",
    "Sussurro", "Oceano")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos  ', end=(''))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()} ', end=(''))
