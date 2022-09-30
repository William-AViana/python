def get_dia(dia):
    semana = {
        1: 'Fim de Semana',
        2: 'Dia da semana',
        3: 'Dia da semana',
        4: 'Dia da semana',
        5: 'Dia da semana',
        6: 'Dia da semana',
        7: 'Fim de Semana'
    }
    return semana.get(dia, '--- inválido ---')


if __name__ == '__main__':
    for x in range(9):
        print(f'{x} : {get_dia(x)}')
