'''
Faça um programa que dada a entrada de uma lista o programa calcule a
combinatória de dois elementos e nos retorne as combinações em uma nova lista.

Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
'''


def combinatoria():
    numbers = [1, 2, 3, 4]
    output = []

    for i in range(len(numbers)):

        step = numbers[i]

        lista_1 = [step for _ in numbers[i + 1:]]

        output.extend(list(zip(lista_1, numbers[i + 1:])))

    return output
