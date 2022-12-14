#!/usr/bin/python3

# Garantir que o arquivo seja fechado mesmo com erro
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()

if arquivo.closed:
    print('Closed file!')
