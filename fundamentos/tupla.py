tupla = tuple()
tupla = ()

print(type(tupla))
# print(dir(tupla)) # dicionario
# print(help(tupla)) # funções

tupla = ('um') # para ser uma tupla é necessário a virgula apos o valor (,)
print(type(tupla))
tupla = ('um',)
print(type(tupla))

print(tupla[0])
# tupla[0] = 'novo'

cores = ('verde', 'amarele', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('azul'))
print(cores.count('branco'))
print(len(cores))