class Carro:
    pass


if __name__ == '__main__':
    c1 = Carro(180)
    print(c1.acelerar)

    for _ in range(25):
        print(c1.acelerar(8))

    # for _ in range(10):
    #     print(c1.frear(delta=20))
