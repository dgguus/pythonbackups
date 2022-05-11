import random
import time
result = {}
for j in range(1, 5):
    n = random.randint(1, 6)
    result[f'jogador{j}'] = n
    time.sleep(1)
    print(f'Jogador {j}: {n}')
print('Ranking:')
teste = (sorted(result.values()))

