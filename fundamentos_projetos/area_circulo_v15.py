#!/usr/bin/python3
from math import pi, pow
import sys
import errno


class TerminalColor:
    ERROR = '\033[91m'
    STANDARD = '\033[0m'


def circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERROR + 'O raio deve ser um valor numérico.' +
              TerminalColor.STANDARD)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
