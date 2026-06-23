# import é para importa bibliotecas para py 
# # from biblioteca import elemento especifica, isso para usar um elemento isolado da biblioteca 
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual á {}.'. format(num, raiz))
# codigo que mostra o verdadeiro resultado

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual á {}.'. format(num, math.ceil(raiz)))
#esse codigo arrendoda o valor para mais 
