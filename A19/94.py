lista = []
dicio = {}
while True:
    dicio['nome'] = str(input('Nome: ')).capitalize()
    dicio['idade'] = int(input('Idade :'))
    dicio['sexo'] = str(input('Sexo :[M/F]: ')).capitalize()
    ask = str(input('Quer continuar?[S/N]')).upper()
    lista.append(dicio.copy())
    if ask == "N":
        break
print(f'Foram cadastradas {len(lista)} Pessoas.')
for c in range(0, len(lista)):
    print(lista[c][1])



