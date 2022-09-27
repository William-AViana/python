from random import randint

numero = -1
numero_secreto = randint(0, 9)

while numero != numero_secreto:
    numero = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
