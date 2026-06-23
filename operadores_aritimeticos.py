# + adição 
# - subtração 
# * mutiplicação 
# / divisão 
# ** potenciação 
# // Divisão inteira
# % resto da divisão 
# lembrese que o simbolo de = solo é pra receber informação para ver se algo é igual a outra coisa em questão de número usa dois iguais 
# quando voce coloca '.end='' '   dentro do parentese do print ele não quebra a linha 
# ja o \n é justamente para quebrar a barra sem necessidade de um monte de print 
 
N = int(input('Digite um número: '))
A = N - 1
S = N + 1
print('O antecessor do número digitado é {} e o sucessor do número digitado é {} !'. format(A, S))

n = int(input('Digite um número: '))
D = n * 2
T = n * 3
R = n **(1/2)
print('O dobro do número digitado é {} o triplo é {} e a raiz quadrada é {}'. format(D, T, R))

N1 = float(input('Digite a nota de português: '))
N2 = float(input('Digite sua nota em matemática: '))
MN = (N1 + N2)/2 
print('A média do alunos nas duas materias é de {}!'. format(MN))

AL =  float(input('Digite a altura da parede: '))
CO = float(input('Digite o comprimento da parede: '))
AR = AL * CO 
LI = AR / 2
print('A quantidade de tinta para pintar essa parede em litros é de {}!'.format(LI))

S = int(input('Digite seu sálario: '))
SR = S + (S * 0.15)
print('O seu salario com reajuste de 15% é de {}'. format(SR))


C = float(input('Qual a temperatura em graus C°'))
F = float((C * 1.8)+ 32) 
print('A temperatura em F é de {}!'. format(F))


KM = int(input('Quantos KM você andou com o carro? '))
D = float(input('Quantos dias ficou com ele? '))
VP = (D * 60) + (KM * 0.15)
print('O valor total a pagar do aluguel do carro é de {}!'. format(VP))

