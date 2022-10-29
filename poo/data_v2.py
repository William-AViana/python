class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 11, 2010)
# d1.dia = 10
# d1.mes = 10
# d1.ano = 1990

print(d1)

d2 = Data(dia=15)
# d2.dia = 11
# d2.mes = 11
# d2.ano = 1990

print(d2)
