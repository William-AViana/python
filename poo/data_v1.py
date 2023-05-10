class Data:
    # definição de um método para gerar string ou pode usar __str__
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    
    def dictionary(self):
        thisdic = dict(Dia = self.dia, Mes = self.mes, Ano = self.ano )
        return thisdic


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
print(d2.dictionary())
