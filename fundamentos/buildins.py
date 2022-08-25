# __buildins__ é de escopo global e um módulo com várias funcionalidades
import math
print(type(1))
print(__builtins__.type('Fala Dev'))
print(__builtins__.print(10 / 3))

# ajuda sobre a função dir do escopo global
# print(__builtins__.help(__builtins__.dir))

# retorna um array com objetos presentes no escopo global da aplicação
print(dir())

a = 5

# variavel "a" e o módulo "math" estão no escopo global
print(dir())

# print(dir(__builtins__))

nome = 'William'
print(type(nome))
print(__builtins__.len(nome))
