
#sum -> soma
#len -> tamanho


def soma(numero_1, numero_2):
    return numero_1 + numero_2


def média(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)


def imprime_replaorio(nome, cpf, telefone):
    return f"""
    Relátio parcial

    {nome}, portador do cpf {cpf}, que usa o número {telefone}

    Está oficialmente de férias

    Ass. Direção
    """


print(
    imprime_replaorio(
        nome='Eduardo Mendes',
        cpf=123456789,
        telefone=98547857
    )
)
