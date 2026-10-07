'''Parte 2 da aula de polimorfismo
SOBRECARGA DE MÉTODO
varios metodos com o mesmo metodo com o mesmo nome, e depedendo da assinatura do metodo vai fazer tarefas diferentes 

SOBRECARGA DE OPERADOR 
Substituir o jeito que um operador funciona para o meu interesse, ou seja como eu quero que ele funcione 

Equal to                 p1 == p2                p1.__eq__(p2) PARA IGUALDADE
Not equal to             p1 != p2                p1.__ne__(p2)
Less than                p1 < p2                 p1.__lt__(p2)
Less than or equal to    p1 <= p2                p1.__le__(p2)
Greater than             p1 > p2                 p1.__gt__(p2)
Greater than or equal to p1 >= p2                p1.__ge__(p2)
In-place Addition        p1 += p2                p1.__iadd__(p2)
In-place Subtract        p1 -= p2                p1.__isub__(p2)

'''