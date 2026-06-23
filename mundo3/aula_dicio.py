# Dicionarios  são variaveis compostas que possibilita da nomes as listas internas 

# Dicionarios são dados em {}

dados = dict()
dados = {'nome':'Pedro','idade':25}
print(dados['nome'])
print(dados['idade'])

# Caso eu queira adicionar outra infomação 

dados['sexo'] = 'M'

# PARA eliminar um elementos usamos o comando del
'del'

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')


# Pode colocar dicionarios dentro de elementos de uma lista  

# Pratica 

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e o sexo é {pessoas["sexo"]}')
 
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)


# ==============================
# 1) Criando e manipulando "dados"
# ==============================

dados = dict()  # cria dicionário vazio
dados = {'nome': 'Pedro', 'idade': 25}

print("Nome:", dados['nome'])
print("Idade:", dados['idade'])

# Adicionando nova informação
dados['sexo'] = 'M'

# Atualizando valor existente
dados['idade'] = 26

# Removendo elemento
del dados['sexo']

# Usando get (forma segura de acessar)
print("Altura:", dados.get('altura', 'Não cadastrada'))

print("-" * 40)


# ==============================
# 2) Trabalhando com outro dicionário
# ==============================

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print("Chaves:", filme.keys())
print("Valores:", filme.values())
print("Itens:", filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

# Removendo e retornando valor
ano_removido = filme.pop('ano')
print("Ano removido:", ano_removido)

# Atualizando vários valores
filme.update({'ano': 1977, 'genero': 'Ficção Científica'})

print("-" * 40)


# ==============================
# 3) Lista de dicionários (Brasil)
# ==============================

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())  # cópia independente

print("\nEstados cadastrados:")

for e in brasil:
    print(e)

# =====================================================
# 🔹 dict() → Construtor da classe dicionário
# Cria um dicionário vazio
# =====================================================

dados = dict()  # equivalente a dados = {}
# {} é apenas a forma literal (mais curta) de criar um dicionário

dados = {'nome': 'Pedro', 'idade': 25}
# Dicionário é uma estrutura de dados no formato:
# {chave: valor}

# =====================================================
# 🔹 Acesso com []
# =====================================================

print(dados['nome'])   # Acessa o valor da chave 'nome'
print(dados['idade'])  # Acessa o valor da chave 'idade'

# ⚠ Se tentar acessar uma chave que não existe:
# print(dados['altura'])  → dará KeyError


# =====================================================
# 🔹 .get()
# Forma segura de acessar valores
# Sintaxe: dicionario.get(chave, valor_padrao)
# =====================================================

print(dados.get('altura'))  # Retorna None se não existir
print(dados.get('altura', 'Não cadastrada'))  # Retorna valor padrão

# Muito usado em sistemas reais para evitar erro.


# =====================================================
# 🔹 Adicionando e alterando valores
# =====================================================

dados['sexo'] = 'M'   # Se não existir → cria
dados['idade'] = 26   # Se existir → substitui


# =====================================================
# 🔹 del
# Remove completamente a chave e o valor
# =====================================================

del dados['sexo']
# Depois disso, 'sexo' não existe mais no dicionário


print("-" * 40)


# =====================================================
# Trabalhando com outro dicionário
# =====================================================

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

# =====================================================
# 🔹 .keys()
# Retorna todas as chaves
# Tipo retornado: dict_keys([...])
# É iterável (pode usar em for)
# =====================================================

print(filme.keys())


# =====================================================
# 🔹 .values()
# Retorna apenas os valores
# =====================================================

print(filme.values())


# =====================================================
# 🔹 .items()
# Retorna pares (chave, valor) como tuplas
# Exemplo interno: ('titulo', 'Star Wars')
# =====================================================

print(filme.items())

# Muito usado com for
for k, v in filme.items():  # ocorre desempacotamento automático da tupla
    print(f'O {k} é {v}')


# =====================================================
# 🔹 .pop()
# Remove a chave e RETORNA o valor removido
# Diferença:
# del → só remove
# pop → remove e devolve o valor
# =====================================================

ano_removido = filme.pop('ano')
print("Ano removido:", ano_removido)


# =====================================================
# 🔹 .update()
# Atualiza vários valores de uma vez
# Se existir → substitui
# Se não existir → cria
# =====================================================

filme.update({'ano': 1977, 'genero': 'Ficção Científica'})


print("-" * 40)


# =====================================================
# Lista de dicionários (estrutura mais avançada)
# =====================================================

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')

    # =================================================
    # 🔹 .copy()
    # Cria uma cópia independente do dicionário
    #
    # Se fizermos:
    # brasil.append(estado)
    #
    # Todas as posições da lista apontariam para
    # o mesmo objeto na memória.
    #
    # .copy() evita esse problema.
    # Isso é entender referência vs cópia.
    # =================================================

    brasil.append(estado.copy())

print("\nEstados cadastrados:")
for e in brasil:
    print(e)




