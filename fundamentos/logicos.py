# True or False
print(7 != 3 and 2 > 3)

# Tabela verdade do AND
print(4 * '=' + ' AND ' + 4 * '=')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabela verdade do AND
print(4 * '=' + ' OR ' + 4 * '=')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Tabela verdade do XOR
print(4 * '=' + 'XOR' + 4 * '=')
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Operação Negação (unário)
print(4 * '=' + 'NOT' + 4 * '=')
print(not True)
print(not False)
print(not 0)
print(not 1)
print(not not -1)
print(not not True)

# Cuidado com operadores Bit-a-bit
print(4 * '=' + 'bit-a-bit' + 4 * '=')
print(True & False)
print(False | True)
print(True ^ False)

# AND bit-a-bit
print('AND bit-a-bit')
# 3 = 11
# 2 = 10
# _ = 10
print(3 & 2)

# OR bit-a-bit
print('OR bit-a-bit')
# 3 = 11
# 2 = 10
# _ = 11
print(3 | 2)

# XOR bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
print(3 ^ 2)

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)
