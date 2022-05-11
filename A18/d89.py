# Boletim
ficha = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N]'))
    if resp in "Nn":
        break
print('-='*17)
print(f'No. NOME         MÉDIA')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]}{a[2]:>10}')
while True:
    print('-'*35)
    opc = int(input('Qual aluno deseja ver as notas?(999 para interromper)'))
    if opc == 999:
        print('SAINDO....')
        break
    if opc <= len(ficha) -1 :
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]} ')
print('<<<Volte sempre>>>')