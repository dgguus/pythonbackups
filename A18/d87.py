# Matriz APRIMORADA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
         pares.append(matriz[l][c])
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
# Soma de todos os valores pares
print(f'Os números pares são: {pares} e sua soma é : {sum(pares)}')
# Maior valor da segunda linha
maior2 = matriz[1][0]
if matriz[1][1] > maior2:
    maior2 = matriz[1][1]
if matriz[1][2] > maior2:
    maior2 = matriz[1][2]
print(f'O maior número da segunda linha é {maior2}.')
# Soma dos números da terceira coluna
soma3 = matriz[2][0] + matriz[2][1] + matriz[2][2]
print(f'A soma dos números da terceira coluna {matriz[2]} é : {soma3}')