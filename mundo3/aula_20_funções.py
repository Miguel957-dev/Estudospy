'''def mostraLinha():
    print('-'*50)
    #def quer dizer a definição de uma função util para voce mas que não tem no python 

mostraLinha()'''
'''
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')

# uma forma de agilizar melhor ainda 

def soma(a, b):
    s = a + b
    print(s)
    print('-'*30)


#Codigo principal 
soma(4, 5)
soma(3, 5)
soma(5, 1)


#EMPACOTAR PARAMETROS 

def contador(*núm):
    print(núm)

#Codigo principal
contador(9, 5, 5)
contador(2, 3, 7)
contador(1, 2 , 8, 6 , 7, 3)
'''
#Segunda parte da aula 

#help() # Manual de cada função Digite 'quit' para sair 

#print(input.__doc__) #paramento do comando 

# Isso é para mostrar o manual de umd função de outra pessoa

def contador(i, f, p):
    """Tudo aqui dentro é uma docs strings para detalhar a função que você criou, assim podendo ver como funciona detalhadamente"""
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')

help(contador)# nao da muita indformação util
contador(0, 100, 10)


#Agora veremos sobre parametros opcionais 

def somar(a=0, b=0, c=0):
    s = a + b + c 
    print(f'A soma vale {s}')


somar(2, 2, 5)
somar(5, 1)# daria erro, por isso igualamos as variaveis dentro do paranteses da função para que se ela não receber nenhuma infomação ela receba 0


# Escopo de variaveis


def teste():
    x = 8 #VARIAVEL LOCAL 
    print(f'O valor de n é {n}')
    print(f'O valor de x vale {x}')


#programa principal 

n = 2 # VARIAVEL GLOBAL 
print(f'O valor de n é {n}')
print(x) # type: ignore da erro pois a variavel x é lical, não é definida fora da função 


# RETORNO DE VALORES 

def somar(a=0, b=0, c=0):
    s = a + b + c 
    return s


r1 = somar(2, 2, 5)
r2 = somar(3, 4)
r3 = somar()
print(f'Meus calculos deram {r1}, {r2} e {r3}')