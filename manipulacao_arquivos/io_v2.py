#!/usr/bin/python3
arquivo = open('pessoas.csv')
# consumir os dados conforme o necessário sem a necessidade de
# carrega-lo na memória do computador
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
