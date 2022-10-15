#!/usr/bin/python3
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{iten}</li>' for iten in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
