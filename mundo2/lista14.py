'''sexo = ''
while sexo not in ('M', 'F'):
    sexo = str(input('Digite seu sexo "M" ou "F"'))
    if sexo not in ('M', 'F'):
        print('Por favor digite novamente resposta invalída!')
    else:
        print('Fim')


from random import randint
quantosloop = 1 
sorteio = randint(0, 10)
print('Eu sou o computador e esrou pensando em um número de 0 a 10.' \
'Será que consegue adivinhar qual foi ?')
numero = int(input('Qual número eu estou pensando?'))
while sorteio != numero:
    if numero > sorteio:
        print('Menos... Tente mais uma vez.')
        numero = int(input('Qual número eu estou pensando?'))
        quantosloop += 1
    elif numero < sorteio:
        print('Mais... Tente mais uma vez.')
        numero = int(input('Qual número eu estou pensando?'))
        quantosloop += 1
print('Parabens você acertou!' \
'Você tentou {} vezes.'.format(quantosloop))
print(sorteio)

#menu de opções 

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao !=5:
    print('    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa')
    opçao = int(input('Qual a sua opção? '))
    if opçao == 1: 
        soma = n1 + n2 
        print('A soma de {} e {} é igual à {}'.format(n1, n2, soma))
    elif opçao == 2:
        vezes = n1 * n2 
        print('A multiplicação de {} vezes {} é {}'. format(n1, n2, vezes))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
            menor = n2 
        elif n2 > n1:
            maior = n2 
            menor = n1 
        else:
            maior = menor = n1
        print('Maior número é {} e o menor é {}'.format(maior, menor))
    elif opçao == 4:
        n1 = int(input('Dgite um número novamente: '))
        n2 = int(input('Dgite um número novamente: '))
    elif opçao == 5:
        print('FIM')


n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))


print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0 
mais = 10
while mais !=0:
    total += mais 
    while cont <= total:
        print('{} - '.format(termo), end=(''))
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais deseja calcular ?'))   
print('FIM')   



print(20*'-')
print('Sequencia de fibonacci')
print(20*'-')
n = int(input('Quantos termos você quer mostrar ?'))
cont = 3
t1 = 0 
t2 = 1 
print('{} -> {} -> '. format(t1, t2), end=(''))
while cont <= n:
    t3 = t1 + t2 
    t1 = t2 
    t2 = t3 
    print('{} -> '. format(t3), end=(''))
    cont += 1 
print('FIM')


soma = 0
n = int(input('Digite um número [999 para parar]'))
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]')) 
cont - 1 

print('A quantidade de números digitados foi {} e a soma deles é {}.'. format(cont, soma))
'''

sn = 'n'
qn = 0
soma = 0
n = 0
soma += n
while sn not in ('N', 'NÃO'):
    n = int(input('Digite um numero: '))
    qn += 1
    sn = str(input('Quer continuar[S/N]?')). upper()
    if sn not in ('S', 'SIM', 'N', 'NÃO',):
        print('Resultado invalido, digite novamente.')
        sn = str(input('Quer continuar[S/N]?')). upper()
    soma += n
    if qn == 1:
        maior = menor = n 
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n 
media = soma / qn 
print('A quantidade de números digitados foi {} a soma deles é {} e a média entre eles é {}'. format(qn, soma, media))
print('O maior foi {} e o menor foi {}'. format(maior, menor))

    
