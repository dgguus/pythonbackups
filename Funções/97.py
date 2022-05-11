# tamanho adáptavel
def write():
    cont = len(frase)+2
    print('~'*cont)
    print(f' {frase.capitalize()}')
    print('~'*cont)


# simplesmente ler tamanho da frase adicionar +1 '-' no começo e outro no fim em cima e embaixo

frase = str(input(' Frase: '))
write()
