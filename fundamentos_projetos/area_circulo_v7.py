#!/usr/bin/python3

from math import pi, pow

if __name__ == '__main__':
    raio = input('Digite o raio: ')
    area = pi * pow(float(raio), 2)
    print(area)
