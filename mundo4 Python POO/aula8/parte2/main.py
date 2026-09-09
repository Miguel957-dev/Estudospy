from get_e_set import Avaliaçao
from rich import print, inspect

def main():
    av1 = Avaliaçao("Miguel", "matematica", 10)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")
    inspect(av1, private=True)

if __name__=="__main__":
    main()