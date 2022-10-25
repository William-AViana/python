#!/usr/bin/python3
def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('apan', 'Curso de Python, por '),
            tag('strong', 'Juracy', id='j'),
            tag('span', ' e '),
            tag('strong', 'Leonardo', id='l'),
            tag('span', '.'),
            html_class='alert')
    )
