#!/usr/bin/python3
def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
