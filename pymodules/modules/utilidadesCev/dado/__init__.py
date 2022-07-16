def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(f'{msg}')).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '' or entrada.isnumeric() == False:
            print(f'\033[0;31mERRO!"{entrada}" é um Preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
