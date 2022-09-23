#!/usr/bin/python3
from math import pi, pow


def circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    raio = input('Digite o raio: ')
    area = circulo(raio)
    print('Área do círculo é ', area)
