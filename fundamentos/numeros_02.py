from decimal import Decimal, getcontext

print(1.1 + 2.2)
print(Decimal(1) / Decimal(7))

# mudar o contexto do resultado com getcontext
getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))
# print(dir(Decimal))

print(1.1 + 2.2)
print(Decimal(1.1) + Decimal(2.2))

# verificar o escopo global e as funções que foram inseridas
print(dir())