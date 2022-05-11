def area(larg, comp):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é {a}m²')


print('Controle de terrenos')
print('-'*25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
