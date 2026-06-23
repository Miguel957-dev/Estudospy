#finalmente IF e ELSE
#usado para quando se tem duas possibilidades na sequencia de comando do programa, causando desvios na sequencia 
'''tempo =int(input('Quantos anos tem o seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('FIM')

#Condição simplificado 
tempo =int(input('Quantos anos tem o seu carro?'))
print('carro novo'if tempo <=3 else'carro velho')
print('FIM')
#funciona apenas para programas simples 


nome = str(input('Qual é o seu nome '))
if nome == 'Miguel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal ')
print('Bom dia, {}'. format(nome))'''

n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua segunda nota'))
media = (n1 + n2)/2
if media>=7:
    print('Você não reprovou;)')
else:
    print('reprovou :(')