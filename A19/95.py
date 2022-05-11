jogador = {'nome': str(input('Nome: ').capitalize()), 'partidas': int(input('Quantas partidas foram jogadas?')),
           'total': 0}
gols = list()
n = 0
for g in range(0, jogador['partidas']):
    n = int(input(f'Quantos gols foram feitos na {g+1} partida?'))
    gols.append(n)
jogador['total'] = sum(gols)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for g in range(0, jogador['partidas']):
    print(f' >>> Na partida {g+1} foram {gols[g]} gols.')
print(f'O total de gols foi {sum(gols)}')
