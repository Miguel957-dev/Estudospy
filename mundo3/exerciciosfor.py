'''# Contagem regressiva 

from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOMMM!\U0001F4A5')
print('Feliz fogos de artifício!🎆')

#Números pares 

for c in range(0 , 51, 2):
    print(c)
print('50')

#Soma 
s = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        s = s + c
print(s)

#Tabuada 
N = int(input('Digite um numero:  '))
print('A tabuada do {} de 1 até 10 é'. format(N))
for c in range(1, 11):
    print(c * N) 

s = 0
cont = 0
for c in range( 1, 7):
    num = int(input('Digite o {} valor: '. format(c)))
    if c % 2 == 0:
        s += c
        cont += 1
print('Você informou {} números e a soma é de {}'.format(cont, s))

        
#P.A

s = 0
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razão
for c in range(primeiro, decimo, razão):
    print('{}'. format(c), end=',')


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print('O inverso da frase {} é {} '.format(frase, inverso))
if inverso == junto:
    print('A frase é um palíndomo.')
else:
    print('A palavra não é um palídro.')

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Qual o ano que voce nasceu?'))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor +=1
print('A quantidade de pessoas maiores de idades são {} e menores são {}'. format(totmaior, totmenor))
        

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))

maioridadehomem =0
nomevelho =0
mediaidade = 0
somaidade = 0
totmulher20 =0
for p in range(1,5):
    print('----{}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
'''

pares = 0
impares = 0
somadosnumerosvalidos = 0
numerosvalidos = 0
for c in range(1, 11):
    n = int(input('Digite {}ª número: '. format(c)))
    if n == 0: 
        break
    elif n < 0:
        continue 
    elif n > 0:
        somadosnumerosvalidos = somadosnumerosvalidos + 1
    if n % 2 == 0:
        pares = pares + 1
    if n % 2 != 0:
        impares = impares + 1
    if n > 0:
        numerosvalidos = numerosvalidos + n 

print('A quantidade de números válidos é de {}.'. format(somadosnumerosvalidos))
print('A quantidade de números pares é {} e impares {}.'. format(pares, impares))
print('A soma dos números válidos é {}.'. format(numerosvalidos))