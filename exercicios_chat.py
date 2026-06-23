n1 = int(input('Digite um numero'))
n2 = int(input('Digite mais um numero'))
s = n1 + n2
print('A soma vale {}'.format(s))

#segundo 

I = int(input('Digite um valor: '))
D = I * 2
T = I * 3
R = I ** (1/2)
print('O dobro de {} vale {}'.format(I, D))
print('O triplo de {} vale {}'.format(I, T))
print('A raiz quadrada de {} é igual a {:.2f}'.format (I, R))

#teceiro 

C = int(input('Digite um valor: '))
A = C - 1
S = C + 1 
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(C, A, S))
 
#quarto
M = int(input('Digite uma medida em metros: '))
CM = M * 100
MM = M * 1000
print('A medida que voce enviou em centimetros é {} e em milimetros é {}!'. format(CM, MM))

#quinto 

N = int(input('Digite um numero:  '))
print('A tabuada do {} de 1 até 10 é'. format(N))
print(f"{N} x 2 = {N*2}")
print(f"{N} x 3 = {N*3}")
print(f"{N} x 4 = {N*4}")
print(f"{N} x 5 = {N*5}")
print(f"{N} x 6 = {N*6}")
print(f"{N} x 7 = {N*7}")
print(f"{N} x 8 = {N*8}")
print(f"{N} x 9 = {N*9}")
print(f"{N} x 10 = {N*10}")

#sexto 

NP = float(input('Digite sua nota em português: '))
NM = float(input('Digite sua nota em matemática: '))
MDF =  (NP + NM)/2 
print('A média do aluno em matemática e português é {}!'. format(MDF))

#setimo 

R = float(input('Digite o valor de dinheiro em reais: '))
D = R /5
print('O valor que você tem de convertido de reais para dolár é de {}!'. format(D))

PSD = float(input('Informe o valor do produto: '))
PCD = PSD * 0.95
print('O valor do produro com desconto de 5% é de {}!'. format(PCD))
