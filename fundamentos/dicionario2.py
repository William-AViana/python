pessoa = {'nome': 'Prof. Alberto', 'idade': 45, 'cursos': ['Python', 'IA']}
pessoa['idade'] = 40
print(pessoa)

pessoa['cursos'].append('Angular')
print(pessoa)

pessoa.pop('idade')
print(pessoa)

pessoa.update({'idade': 44, 'Sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)