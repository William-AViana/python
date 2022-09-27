from random import randint


def gerar_cartela():
    cartelas = int(input('Quantas cartelas deseja gerar? '))

    contador = 0

    while contador < cartelas:

        cartela = set()

        while len(cartela) < 6:

            cartela.add(randint(1, 60))

        print(sorted(cartela))

        contador += 1


gerar_cartela()
