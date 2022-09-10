pessoa = {'nome': 'william', 'idade': 32, 'cursos': [ 'ADS', 'Inglês']}

print(type(pessoa))
# print(dir(pessoa))
print(len(pessoa))

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][1])
# print(pessoa['tags']) # Key error

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))