from moeda import moeda, metade, diminuir, aumentar, dobro

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10% temos {moeda(aumentar(p, 10, False))}')
print(f'Diminuindo 13% temos {moeda(diminuir(p, 13, False))}')
