def aumentar(v=0, taxa=0, format=False):
    res = v + (v * taxa/100)
    
    return res if format == False else moeda(res)

def diminuir(v=0, taxa=0, format=False):
    res = v - (v * taxa/100)

    return res if  format == False else moeda(res)

def dobro(v=0, format=False):
    res = v * 2

    return res if  format == False else moeda(res)

def metade(v=0, format=False):
    res = v * 0.5

    return res if  format == False else moeda(res)

def moeda(v=0, moe='R$'):

    return f'{moe}{v:.2f}'.replace('.', ',')

def resumo(v=0, d=0,meno=0):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)

    print(f'{"Preço analisado:":<30}{moeda(v)}')
    print(f'{"Dobro do preço:":<30}{dobro(v, True)}')
    print(f'{"Metade do preço:":<30}{metade(v, True)}')
    print(f'{f"{d}% de aumento:":<30}{aumentar(v, d, True)}')
    print(f'{f"{meno}% de redução:":<30}{diminuir(v, meno, True)}')

    print('-'*40)