# Emprestimo de banco
'''valor = int(input('Digite o valor imóvel que deseja financiar: '))
salario = int(input('Digite o valor do seu salario: '))
tempo = int(input('Em quanto tempo você que pagar o imóvel(em meses): '))
valormensal = valor / tempo
if valormensal > salario * (30/100):
    print('O valor das parcelas excedeu 30% do seu salário, e por isso não podemos aprovar o financiamento.')
elif valormensal <= salario * (30/100):
    print('Parabens seu financiamento pode ser aprovado!')
print('Uma boa tarde!')

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1>n2: 
    maior = n1 
    menor = n2
elif n2>n1:
    maior = n2
    menor = n1
    print('O maior número é {} e o menor número é {}'. format(maior, menor))
elif n1 == n2:
    igual = n1
    print('Os dois números são o mesmo, que é {}.'.format(igual))

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você reprovou pois sua meia foi {} que é menor que 5'. format(media))
elif 5 <= media <= 6.9:
    print('Devido sua média ser {} você esta de recuperação!'.format(media))
elif media >=7:
    print('Sua média é {} e você foi aprovado!'.format(media))


l1 = float(input('Medida do lado do triângulo: '))
l2 = float(input('Medida do outro lado do triâgulo:'))
l3 = float(input('Medida do terceiro lado do triângulo:'))
if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('Pode ser um trianlo')
elif l1 + l2 < l3 and l1 + l3 < l2 and l3 + l2 < l1:
    print('Não pode ser um triangulo.')
elif l1 == l2 == l3:
    print('As medidas do lado que você informou, formam um triângulo equilátero!')
elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
    print('As medidas do triângulo que você informou, formam um triângulo isósceles.')
elif l1 != l2 != l3:
    print('As medidas do triâgulo que você digitou formam um triângulo Escaleno.')'''


'''# Alistamento militar 
from datetime import date 
atual = date.today().year
nasc = int(input('Ano de naccimento: '))
idade = atual - nasc
print('Quem nasceu em {} já tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18 
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))

from datetime import date
atual = date.today().year  
nasc = int(input('Qual ano você nasceu? '))
idade = atual - nasc
print('O atleta tem {} anos.'. format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif 9 < idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif 14 < idade <= 19:
    print('CLSSIFICAÇÃO: JUNIOR')
elif 19 < idade <= 25:
    print('CLASSIFICAÇÃO:SÊNIOR')
elif 25 < idade:
    print('CLASSIFICAÇÃO: MASTER')


peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso / (altura ** 2.0) 
print('Seu IMC é igual a {:.1f}'. format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= IMC <= 24.9:
    print('Você ta com o peso ideal.')
elif 25 <= IMC <=29.9:
    print('Você está com sobrepeso.')
elif 30 <= IMC <= 34.9:
    print('Você tem obesidade grau 1')
elif 35 <= IMC <= 39.9:
    print('Você está com obesidae grau 2')
else: 
    print('Você está com obesidade mórbida')


compra = float(input('Digite o valor da compra: '))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    valor = compra * 0.9
elif opçao == 2:
    valor = compra * 0.95
elif opçao == 3:
    valormensal = compra / 2
    print('Sua compra será parcelada em 2x de R${} SEM JUROS.'. format(valormensal))
    valor = valormensal * 2
elif opçao == 4:
    t = int(input('Quantas parcelas?'))
    total = compra + (compra * 20 /100)
    valormensal = total / t
    print('Sua compra será parcelada em {}x de R${} COM JUROS.'. format(t, valormensal))
    valor = total
print('Sua compra de R${} vai custar R${} no final.'. format(compra, valor))'''

from random import randint
from time import sleep
intens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O computador jogou {}.'.format(intens[computador]))
print('Jogador jogou {}.'. format(intens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('JOGADOR PERDE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('JOGADOR PERDE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
    
