#!/usr/bin/python3
# tuplas para usar como filtro
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


# Função para tratar os atributos
def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **atrs)
    atributos = filtrar_atrs(atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **atrs):
    lista = ''.join(f'<li>{iten}</li>' for iten in itens)
    return f'<ul {filtrar_atrs(atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    # print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='color:blue'))
