for var in range(1,101):
    output = ''
    if var % 3 == 0:
        output = "Fizz"
    if var % 5 == 0:
        output = "Buzz"
    if output == '':
        output = var
    print(output)