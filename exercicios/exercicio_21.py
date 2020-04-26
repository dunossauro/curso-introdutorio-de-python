

def eleva_numero(lista_de_numeros, numero_elevado):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** numero_elevado)

    return lista_resposta


lista_valores = []

for valor in range(10):
    lista_valores.append(
        int(input('Fala um número aí:   '))
    )


dicionario = {
    'lista padrão': lista_valores,
    'lista quadrada': eleva_numero(lista_valores, 2),
    'lista cúbica': eleva_numero(lista_valores, 3)
}

print(dicionario)
