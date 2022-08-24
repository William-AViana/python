# Desafio operadores lógicos

# trabalhos
trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # XOR
mais_saudavel = not sorvete

print('Tv50={}, Tv32={}, Sorvete={}, Saudável={}'
      .format(tv_50, tv_32, sorvete, mais_saudavel))
