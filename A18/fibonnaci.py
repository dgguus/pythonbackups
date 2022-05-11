x = 0
y = 1
z = 0
while z != 377:
    z = x + y
    print(f' {z} ', end="")
    x = y
    y = z
