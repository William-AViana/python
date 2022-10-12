# [expressão for item in list if conditional ]
dobros = [i * 2 for i in range(10)]
print(dobros)

# Versão "normal"
dobro_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobro_dos_pares.append(i * 2)
print(dobro_dos_pares)
