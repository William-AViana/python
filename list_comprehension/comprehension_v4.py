# Generator - gera os dados sob demanda e consome menos memória
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
