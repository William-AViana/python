#!/usr/bin/python3

# The resource allocated inside the block will be closed
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Closed file!')

if saida.closed:
    print('Exit file closed!')
