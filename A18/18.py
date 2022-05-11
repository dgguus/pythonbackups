#Listas compostas
meninos = list()
meninas = list()
todos = list()
for c in range(0, 3):
    meninas.append(str(input('Nome: ')))
    meninas.append(int(input('Idade: ')))
    todos.append(meninas[:])
    meninas.clear()
print(todos)