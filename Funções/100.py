import random
import time

lista = list()
def sorteia():
    print('Foram sorteados: ',end='')
    for c in range(0, 5):
        n = random.randint(1, 50)
        if n % 2 == 0:
            lista.append(n)
        print(n, end=' ')
        time.sleep(0.5)
    print('\n')
def somaPar():
    print(f'Somando os valores pares temos {sum(lista)}')


sorteia()
somaPar()



