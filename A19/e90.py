nome = str(input('Qual o nome do aluno? ')).capitalize()
media = float(input('Qual a média do aluno? '))
dic = {'nome': nome, 'media': media, 'situacao': ''}
if media >= 7.0:
    dic['situacao'] = 'Aprovado'
else:
    dic['situacao'] = 'Reprovado'
print(f'O nome é igual a {dic["nome"]}')
print(f'Média é igual a: {dic["media"]} ')
print(f'A situação é: {dic["situacao"]}')
