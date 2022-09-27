palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')

aprovados = ['Rafaela', 'keila', 'Samuel', 'Grazi']
for nome in aprovados:
    print(f'Nome: {nome}.')

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Heje é {dia}')


for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
