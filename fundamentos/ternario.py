# Operadores ternários
esta_chovendo = False

# a espressão está mais próxima da opção verdadeira
print(('Não preciso', 'Preciso')[esta_chovendo] + ' sair com o guarda chuva.')
print('Preciso' if esta_chovendo else 'Não preciso' + ' sair com o guarda chuva.')
