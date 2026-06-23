#Primeiro exercicio

'''def area():
    reta_ar = (a * b)
    print(f'A area do retangulo é {reta_ar} m*2')

a = float(input('Digita a base do retangulo: '))
b = float(input('Digite a altura do retangulo: '))
area()'''

#Outra opção(MELHOR)

'''def area():
    print('-'*30)
    a = float(input('Largura (m)'))
    b = float(input('Altura (m)'))
    retan = a * b
    print(f'A área de um terreno {a} x {b} = {retan}m²')

area()'''

#Terceira opção e a melhor 


'''def area(largura, altura):
    return largura * altura


a = float(input('Largura (m): '))
b = float(input('Altura (m): '))

resultado = area(a, b)

print(f'A área de um terreno {a} x {b} = {resultado} m²')

'''
# Segundo  exercicio

'''def escreva(esc):
    print('~~'*len(esc))
    print(f'   {esc}   ')
    print('~~'*len(esc))

escreva('Gustavo')
escreva('Miguel Lucas lopes de Queiroz')
escreva('Não gosto de sptfy gratis')
'''


# Terceiro exercicio

'''from time import sleep

def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f: 
        cont = i 
        while cont <= f:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont -= p
        print('FIM!') 

#PROGRAMA PRINCIPAL 

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
'''

# Quarto exercicio

'''from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passado... ')
    sleep(2)
    for valor in num:
        print(f'{valor} ', end='', flush= True)
        sleep(0.5)
        cont += 1
    print()
    if num:  # Isso verifica se a lista NÃO está vazia
        mai = max(num)
    else:    # Se estiver vazia (seja lista, string ou tupla)
        mai = 0
        print("A lista está vazia!")
    print(f'A quantidade de números informados foram {cont} e o maior é o {mai}')
    print()

#Programa principal 

maior(2, 9, 4, 3, 5, 7, 10)
maior(1, 8, 0)
maior(1, 0)
maior(6)
maior()
'''


#Quinto exercicio

from random import randint

lista = []
def sortea():
    for c in range(0, 5):
        lista.append(randint(0, 11))
    print('Sorteando 5 valores da lista: ', end='')
    for n in lista:
        print(f'{n} ', end='')
    print(', PRONTO!')


def par_soma():
    par = 0
    for n in lista:
        if n % 2 ==0:
            par += n
    print(f'Somando os valores pares de {lista}, temos {par}')

sortea()
par_soma()
        

#PARTE DOIS DA AULA 



