import random
from time import sleep
jogos = int(input('Quantos jogos?'))
lista = list()
total = list()
n = 0
for c in range(jogos):
        while len(lista) != 6:
                n = random.randint(1, 60)
                if n not in lista:
                    lista.append(n)
                lista.sort()
        total.append(lista[:])
        lista.clear()
print(f'-='*15)
print(f'MEGA SENA!')
print(f'-='*15)
for c in range(jogos):
        sleep(1)
        print(f'Jogo {c+1} : {total[c]}')
print(f'-='*15)




