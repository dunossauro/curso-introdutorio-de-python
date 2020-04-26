

lista_de_compras = []
reposta = ''

while reposta != 'acabou':
    reposta = input('O que temos que comprar?   ')
    if reposta != 'acabou':
        lista_de_compras.append(reposta)


print(lista_de_compras)
