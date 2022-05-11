from time import sleep


def contador():
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-----Iníciando------')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    while True:
        if fim > inicio:
            sleep(0.1)
            print(f' {inicio}', end='')
            inicio = inicio + passo
            if inicio > fim:
                print(' Fim!')
                break
        else:
            sleep(0.1)
            print(f' {inicio}', end='')
            inicio = inicio - passo
            if inicio < fim:
                print(' Fim!')
                break


cont = 1
print('-='*16)
print('Contagem de 1 até 10 de 1 em 1!')
while True:
    sleep(0.2)
    print(f'{cont} ', end='')
    cont += 1
    if cont > 10:
        print("FIM!")
        print('-='*16)
        break
cont = 10
print('Contagem de 10 até 0 de 2 em 2!')
while True:
    sleep(0.2)
    print(f' {cont} ', end='')
    cont -= 2
    if cont < 0:
        print('FIM!')
        break
print('-='*16)
contador()
