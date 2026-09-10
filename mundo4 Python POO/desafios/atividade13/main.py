from termostato import *
from rich import inspect


def main():
    t = Termostato()
    t.temperatura = 22
    print(t.ftemperatura)
    inspect(t, private=True)


if __name__=="__main__":
    main()