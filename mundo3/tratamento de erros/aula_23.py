#Tratamento de erros 
x = 0

print(x)#tem um erro mas não é erro fudamental de sintaxe, mas é um erro semantico. No caso a variavel não existe, quando não é um erro sintatico chamamos de exceção.

""" n = int(input('Digite um valor: '))
print(n) """
# se ao inves de por um numeros digitar letras, vai se exceção, pois não tem erro sintatico mas sim nos dados recebidos 

#r = 2/'2' #erro de tipo

""" lst = [3,4,5]
print(lst[3])#Index erro  """
""" except Exception as erro:
    print(f'Infelizmente tivemos {erro.__class__}')
    #se falhar o que vai acontecer """

try: #operação
    n = int(input('Digite um valor: '))
    
except Exception as erro:
    print(f'Infelizmente tivemos {erro.__class__}')
    #se falhar o que vai acontecer

except ValueError:
    print('Tivemos um erro com os tipos de dados que recebemos')

else:#O que fazer se der certo 
    print(n)

finally:#Vai acontecer independente se de certo ou não 
    print('Volte sempre muito obrigado')






