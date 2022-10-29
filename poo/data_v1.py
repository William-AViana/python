class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 10
d1.mes = 10
d1.ano = 1990

print(d1.to_str())

d2 = Data()
d2.dia = 11
d2.mes = 11
d2.ano = 1990

print(d2.to_str())
