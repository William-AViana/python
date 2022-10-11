#!/usr/bin/python3

# The resource allocated inside the block will be closed
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Closed file!')
