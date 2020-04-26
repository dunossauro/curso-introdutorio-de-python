
# apoia.se/livedepython
# @livedepython

carteira = int(input('Quanto eu tenho?  '))
tenis = int(input('Quanto custa o tênis?  '))
necessidade = input('Preciso mesmo disso [s/n]??  ')

if carteira >= tenis and necessidade == 's':
    print('Luxei, comprei um boot novo')
else:
    print('É, deixa pro mês que vem')
