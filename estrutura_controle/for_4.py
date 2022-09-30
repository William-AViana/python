from random import randint


def sortear_dado():
    return randint(1, 7)


for x in range(1, 7):
    if x % 2 == 1:
        continue

    if sortear_dado() == x:
        print('Acertou!', x)
        break

else:
    print('Não acertou o número!')
