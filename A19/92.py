trab = {'nome': str(input('Nome: ')), 'nascimento': int(input('Ano de nascimento:  ')),
        'ctps': int(input('Carteira de Trabalho (0 não tem): ')), 'anoc': 0}
trab['idade'] = 2022 - trab['nascimento']
if trab['ctps'] >= 1:
    trab['anoc'] = int(input('Ano de contratação: '))
    trab['salario']: float(input('Salário: R$ '))
    trab['aposentadoria'] = (trab['anoc'] + 35) - trab['nascimento']
    print('-=' * 30)
    for k, v in trab.items():
        print(f'{k} tem o valor: {v}')
else:
    print('-=' * 30)
    print('Não trabalha')
