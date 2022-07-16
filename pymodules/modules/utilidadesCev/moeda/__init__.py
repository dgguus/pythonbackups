def aumentar(p=0, num=0, formata=False):
    pr = (num / 100) * p
    p = p + pr
    return p if formata is False else moeda(p)


def diminuir(p=0, num=0, formata=False):
    pr = (num / 100) * p
    p = p - pr
    return p if formata is False else moeda(p)


def dobro(p=0, formata=False):
    p = p * 2
    return p if formata is False else moeda(p)


def metade(p=0, formata=False):
    p = p / 2
    return p if formata is False else moeda(p)


def moeda(p, ):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, a, r):
    print(f'-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-'*30)
    print(f'Preço análisado: {moeda(p)}\n'
          f'Dobro do preço:  {dobro(p, True)}\n'
          f'Metade do preço: {metade(p, True)}\n'
          f'{a}% de aumento:  {aumentar(p, a, True)}\n'
          f'{r}% de redução:  {diminuir(p, r, True)}')
    print(f'-' * 30)
