# pedir o preço de 3 produtos e escolher o menor preço

preço_1 = float(input("Preço 1: "))
preço_2 = float(input("Preço 2: "))
preço_3 = float(input("Preço 3: "))

if preço_1 > preço_2 and preço_2 > preço_3:
    print('Compre o 3')
elif preço_2 > preço_1 and preço_1 < preço_3:
    print('Compre o 1')
