class Retangulo():
    def __init__(self, base = 1, altura = 1):
        self.base = base
        self.altura = altura

        self._base = None
        self._altura = None 

    @property
    def medidas(self):
        print(f"Base = {self._base} \n",
        f"Altura = {self._altura} \n",
        f"Area = {self._base * self._altura}")

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError('Valor da base inválido')
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise ValueError("Valor da altura invalído")
        else:
            self._altura = altura

    @property
    def calculo_area(self):
        self.area = self._altura * self._base
        return self.area