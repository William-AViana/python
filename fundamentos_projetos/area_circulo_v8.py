#!/usr/bin/python3
from math import pi, pow


def circulo(raio):
    print('Área do cículo: ', pi * pow(float(raio), 2))


if __name__ == '__main__':
    raio = input('Digite o raio: ')
    circulo(raio)
