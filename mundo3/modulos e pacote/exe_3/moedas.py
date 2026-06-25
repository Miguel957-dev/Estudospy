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
    