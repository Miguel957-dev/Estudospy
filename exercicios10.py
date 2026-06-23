'''#adivinhação 
from random import randint
computador = randint(0, 10) #Faz o computador sorteia um número 
número = int(input('Vou pensar em um número entre 0 e 10, adivinhe em qual número eu pensei'))
if número == computador:
    print('Você ganhou adivinhou o número que eu pensei!')
else:
    print('Eu pensei no número {} e não no {}!'. format(computador, número))

#Limie de velocidade( limites lembrei de calculo KKKKKK)
velocidade = int(input('Qual é a velocidade que você ta dirigindo ?'))
if velocidade <= 80:
    print('Tenha um bom dia, dirija com segurança!')
else:
    multa =(velocidade - 80)*7
    print('Você foi multado! No valor de {} pois excedeu o limite de 80 KM/H da rodovia.'. format(multa))

# ímpar ou par
número = int(input('Digite um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')

#Calculando valor da viagem 

distancia = int(input('Informe a distancia da viagem, em KM:'))
if distancia <= 200:
    valor = int(distancia * 0.5) 
else:
    valor = distancia * 0.45
print('O valor da viagem é de {} reais!'. format(valor))
print('Tenha uma boa viagem! ;)')

# Ano bissexto 
from datetime import date 
ano = int(input('Que ano você que analizar? Coloque 0 para nalisar o ano atal  ' ))
if ano == 0: 
    ano = date.today().year  
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'. format(ano))
else:
    print('O ano {} não é bissexto!'. format(ano))

# Qual numero é maior ?
a = int(input('Digite um valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a 
if b<c and b<a:
    menor = b 
if c<b and c<a:
    menor = c 
print('O menor valor digitado foi {}.'. format(menor))
maior = a 
if b>c and b>a:
    maior = b 
if c>b and c>a:
    maior = c
print('O maior valor digitado foi {}.'. format(maior))

salario = float(input('Qual é o seu salário? '))
if salario <= 1250.00:
    aumento = salario * 0.15
else:
    aumento = salario * 0.1
novo = aumento + salario 
print('O novo valor do seu salário com aumento é de {} reais'. format(novo))

#analisando triângulo 
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos podem formar um triângulo ;) ')
else:
    print('Os segmentos não podem formar um triangulo.')'''

print(19//2) 