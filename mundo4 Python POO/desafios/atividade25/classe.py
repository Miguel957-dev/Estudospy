

class Usuario:
    def __init__(self, nome:str , email:str):
        self.nome = nome
        self.email = email


class Aluno:
    def __init__(self, nome:str, curso:str, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class XML:
    print("<?xml version='1.0' encoding='utf-8'?>")
    print('<dados>')
    def converter(self, objeto):
        if isinstance(objeto, Usuario):
            print('     <usuario>')
            print(f'         <nome>{objeto.nome}</nome>')
            print(f'         <email>{objeto.email}</email>')
            print('     </usuario>')

        elif isinstance(objeto, Aluno):
            print('     <aluno>')
            print(f'         <nome>{objeto.nome}</nome>')
            print(f'         <curso>{objeto.curso}</curso>')
            print(f'         <serie>{objeto.serie}</serie>')
            print('     </aluno>')
        else:
            raise TypeError('Não existe essa classe definida')
        print('</dados>')
class JSON:
    def converter(self, objeto):
        if isinstance(objeto, Usuario):
            print('[ \n'
                '   { \n'
            f'        "nome":{objeto.nome},\n'         
            f'        "email":{objeto.email}\n'
            '   }\n'
            ']\n')
        elif isinstance(self, Aluno):
            print('[\n'
            '   {\n' 
            f'        "nome":{objeto.nome},\n'
            f'        "curso":{objeto.curso},\n'
            f'        "serie":{objeto.serie}\n'
            '   }\n'
            ']\n')  

def exportar_dados(formatar, dados:list):
    for msg in dados:
        formatar.converter(msg)
        
     

