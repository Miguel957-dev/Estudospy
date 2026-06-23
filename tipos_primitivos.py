#aula 06a
n1 = input('Digite um numero')
n2 = input('Digite mais um numero')
s = n1+n2 
print('A soma vale', s)
# o codigo acima não funcionou pois não envolve os tipos primitivos 
n1 =  int(input('Digite um numero'))
n2 = int(input('Digite mais um numero'))
s = n1+n2 
print('A soma vale{}'.format(s))
#int é um comando primitivo que tudo o que estiver dentro do () vai ser considerado um numero inteiro. A seguir vai ser colocado os tipos primitivos a seguir 
#int ('numeros inteiros ex:', 7, -4, 0)float('numeros quebrado', 4.5 , 5.5 , -6.5)bool('True= verdadeiro e False= valores falsos')str('Olá')
#A gente so coloca '' para o que vai ser considerado texto, o que for numero não põem aspas 
print('A soma vale', s)
#ou 
print('A soma vale {}'. format(s))

n3 = int(input('Digite um valor'))
n4 = int(input('Digite outro valor'))
s2 = n3+n4 
print('A soma entre{}'.format(n3), 'mais{}'. format(n4), 'é igual a:{}'. format(s2))

