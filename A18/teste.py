class Funcionario(object):
    def __init__(self, name, age, birth):
        self.name = name
        self.age = age
        self.birth = birth


    def __repr__(self):
        return"Nome:%s Idade:%s Data de Nascimento:%s" % (self.name, self.age, self.birth)

f = Funcionario("John Cena", "44", "1975")
f1 = Funcionario('Randy Orton', "43", "1976")
funcionarios = f, f1
print(funcionarios)
