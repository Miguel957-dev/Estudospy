import math 
N = float(input('Digite um número: '))
NI =  math.trunc(N)
print(NI)


CATOP = float(input('Digite o valor do cateto oposto: '))
CATAD = float(input('Digite o valor do cateto Adjacente: '))
HIPQ = (CATOP**2) + (CATAD**2)
HIP = HIPQ**(1/2)
print('O valor da medida da hipotenusa do triangulo descrito é de {}!'. format(HIP))

#sen e cos e tg 
import math 
an = float(input('Digite um angulo: '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'. format (an, seno))
cosseno = math.cos(math.radians(an))
print('O cosseno do angulo {} é igual a {:.2f}.'.format (an, cosseno))
tangente = math.tan(math.radians(an))
print('O valor da tangente do angulo que voce informou é de {:.2f}'. format (tangente))

#sorteio de nome 

import random
n1 = input('Digite nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista =[n1, n2, n3, n4 ]
#lista os alunos que vão participar os colchetes servem par sinalizar isso no py 
escolhido = random.choice(lista)
#o random é uma biblioteca que contem a função choice que escolhe uma variavel dentro do comando que ela esta, nesse caso o comando é "lista"
print('O nome sorteado foi o {}, meus parabens!'. format(escolhido))

from random import choice
n1 = input('Digite nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista =[n1, n2, n3, n4 ]
#lista os alunos que vão participar os colchetes servem par sinalizar isso no py 
escolhido = choice(lista)
#o random é uma biblioteca que contem a função choice que escolhe uma variavel dentro do comando que ela esta, nesse caso o comando é "lista"
print('O nome sorteado foi o {}, meus parabens!'. format(escolhido))
# uma maneira de simplificar sem perder a funcionalidade é usar o from ja que so estamos usando o pouco da biblioteca random 
#agora um para sorteio de ordens
from random import shuffle
print('Para o sorteio da ordem da apresentações digite o nome dos alunos')
N1 = input('Nome do aluno:')
N2 = input('Nome do outro aluno: ')
N3 = input('Noome do terceiro aluno: ')
N4 = input('Nome do quarto aluno: ')
Alunos = [N1, N2, N3, N4]
shuffle(Alunos)
print('A ordem dos alunos para a apresentação foi {}, boa sorte!'. format (Alunos))

cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')

nome = str(input('Fale seu nome completo?')).strip()
print('Seu nome tem Queiroz?{}'. format('QUEIROZ' in nome.upper()))

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição{}'.format(frase.find('A')+1))
print('A posição que ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
