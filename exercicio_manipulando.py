'''nome = str(input('Digite seu nome:')).strip()
print('Seu nome maiusculo é {}'. format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'. format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'. format(nome.find(' ')))

num = int(input('Digite um numero de ate 4 digitos'))
n = str(num)
print('Analisando o número {}'. format(num))
print('Unidade: {}'. format(num[3]))
print('Dezenas : {}'. format(num[2]))
print('Centenas: {}'. format([1]))
print('Milhar: {}'.format([0]))
#Essa é uma maneira usa os elementos aprendidos na aula 9, mas eles tem uma limitação que é o fato dele so conseguir ler 4 digitos, mas não menos que isso 
 
num = int(input('Digite um numero de ate 4 digitos'))
print('Analisando o número {}'. format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'. format(u))
print('Dezenas : {}'. format(d))
print('Centenas: {}'. format(c))
print('Milhar: {}'.format(m))'''

