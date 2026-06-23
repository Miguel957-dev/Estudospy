# Primeiro exercicios 
'''valores = []
maior = menor = []
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
    for v in valores:
        if cont == 0:
            menor = v
            maior = v 
        else:
            if menor > v:
                menor = v
            if maior < v:
                maior = v
print(f'Os valores digitados são {valores}')
print(f'O maior valor digitado é {maior} na posição', end=(''))
for i, valor in enumerate(valores):
    if valor == maior:
        print(f' {i + 1}...', end=(''))
print('')
print(f'E o menor valor digitado foi {menor} e a sua posição é ', end=(''))
for n, valor in enumerate(valores):
    if valor == menor:
        print(f' {n + 1}...', end=(''))
print('')
'''

#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Segundo execicio
'''
valores = []
while True:
    n = (input('Digite um valor:'))
    r = str(input('Você quer continuar [S/N] ?')).upper() .strip()
    if n not in valores:
        valores.append(n)
        print('Valor adicionado...')
    elif n in valores:
        print('Valor já existente não vou adicionar...')
    while True:
        if r in ('N','S'):
            break 
        else:
            print('Resposta invalida digite novamente!')
            r = str(input('Você quer continuar [S/N] ?')).upper() .strip()
    if r == 'N':
        break
valores.sort()
print(f'Os valores digitados em ordem crescente foram {valores}')

'''

#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Terceiro execicio

'''
valores = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista.') 
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos}.')
                break 
            pos +=1
print('-='*30)

print(f'Os números digitados em ordem foram {valores}.')
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Quarto execicio
'''
el = 0
valores = []
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ?')). upper(). strip()
    while True:
        if r in ('N','S'):
            break 
        else:
            print('Resposta invalida digite novamente!')
            r = str(input('Você quer continuar [S/N] ?')).upper() .strip()
    valores.append(n)
    el += 1
    if r == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {el} elementos.')
print(f'Os valores digitados na ordem decrescente foram {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
'''

#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Quinto execicio

'''
impar = []
pares = []
valores = []
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ?')). upper(). strip()
    while True:
        if r in ('N','S'):
            break 
        else:
            print('Resposta invalida digite novamente!')
            r = str(input('Você quer continuar [S/N] ?')).upper() .strip()
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)
    if r == 'N':
        break
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares foi {pares}')
print(f'Os valores impares digitados foram {impar}')
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Quinto execicio

'''exp = str(input('Digite uma expressão: '))
pilha = []

for sim in exp:
    if sim == '(':
        pilha.append(sim)
    elif sim == ')':
        pilha.append(sim)
quan = len(pilha)
if quan % 2 == 0: 
    print('Sua expressão é valída.')
else:
    print('Sua expressão é invalída')
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Primeiro execicio da Parte 2

'''mai = men = 0
cont = 0
dado = []
grupo = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    grupo.append(dado[:])
    cont += 1
    for p in grupo:
        if cont == 1:
            mai = men = p[1]
        else:
            if p[1] > mai:
                mai = p[1]
            if p[1] < men:
                men = p[1]
    dado.clear()
    r = str(input('Quer continua [S/N]? ')).upper(). strip()
    while True:
        if r in ('S', 'N'):
            break
        else:
            print('Resposta inavlida tente novamente.')
            r = str(input('Quer continua [S/N]? ')).upper(). strip()
    if r == 'N':
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi {mai}. O peso de', end=(''))
for p in grupo:
    if mai in p[:]:
        print(f' {p[0] } ',end=(''))
print()
print(f'O menor peso foi {men}. O peso de',end=(''))
for p in grupo:
    if men in p[:]:
        print(f' {p[0] } ',end=(''))
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Segundo execicio da Parte 2

'''
pares = []
impa = []
numeros = []
numeros.insert(0, pares)
numeros.insert(1, impa)

for c in range(1, 8):
    n = int(input('Digite o {}º valor: '. format(c)))
    if n % 2 == 0:
        pares.append(n)
    else:
        impa.append(n)
pares.sort()
impa.sort()
print(numeros)
print(f'Os valores pares digitados foram {numeros[0]}. ')
print(f'Os valores impar digitados foram {numeros[1]}. ')
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Terceiro execicio da Parte 2

'''matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]'))
for linha in matriz:
    print(linha)'''

#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Terceiro execicio da Parte 2

'''terceira = 0
pares =  maior = menor = cont = 0
matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('=-'*30)
for linha in matriz:
    print(linha)
    for n in linha:
        if n % 2 == 0:
            pares += n
    if linha[2]:
        terceira += (linha[2])
    if matriz[1]:
        for n in matriz[1]:
            cont += 1 
            if cont == 1:
                maior = menor = n 
            else:
                if n > maior:
                    maior = n
                if n < menor:
                    menor = n
print('=-'*30)
print(f'A soma dos valores pares da matriz é {pares}.')
print(f'A soma dos valores da terceira coluna é de {terceira}.')
print(f'O maior valor da segunda linha é {maior} e o menor valor é de {menor}.')



terceira = pares = 0 
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c]= int(input(f'Digite um número de uma matriz na posição [{l}, {c}]: '))
print('=-'*30)
for linha in matriz:
    print(str(linha).center(10))
    for n in linha:
        if n % 2 == 0: 
            pares += n 
    # if linha[2]:  NÃO PRECISA DISSO, POIS SE O VALOR FOR 0 DA ERRO DE LÓGICA, ENTÃO FAÇA COMO NA PROXIMA LINHA 
        terceira += linha[2]
maior = max(matriz[1])
print(f'A soma dos valores pares da matriz é {pares}')
print(f'A soma dos números da terceira coluna é {terceira}')
print(f'O maior número da segunda linha é {maior}')
'''

#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Quarto execicio da Parte 2

'''import random 
import time
print('='*60)

print('JOGA NA MEGA SENA')

print('='*60)

qnts_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
numeros = list(range(1, 61))
for c in range(1, qnts_jogos + 1):
    sorteio = random.sample(numeros, k=6)
    sorteio.sort()
    set(sorteio)
    print(f'O Jogo{c}: {sorteio}')
    time.sleep(1)
print('-='*10, end='')
print('<BOA SORTE>', end='')
print('=-'*10, end='')
'''
#-=-=-=-==--=-=--==-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Quinto execicio

nome = str()
n1 = 0
n2 = 0 
media = 0
ficha = list()
while True:
    nome = str(input('Qual é o nome? '))
    n1 = float(input('Qual foi sua primeira nota ? '))
    n2 = float(input('Qual foi sua segunda nota ?'))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Você quer continuar ? [S/N]')).upper() .strip()
    if resp == 'N':
        break
print('-='* 30)
print(f'{'NO':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8}')
while True:
    print('-'*60)
    opc = int(input('Mostrar nota de qual aluno (999 interrompe) '))
    if opc == 999:
        print('Programa finalizado')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas do aluno {ficha[opc][0]} é {ficha[opc][1]}')
        