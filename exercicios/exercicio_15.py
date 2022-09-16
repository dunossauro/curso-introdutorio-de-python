'''
Faça um programa que dada a entrada de uma lista o programa calcule a
combinatória de dois elementos e nos retorne as combinações em uma nova lista.
'''


def combinatoria():
    numbers = [1, 2, 3, 4]
    output = []

    for i in range(len(numbers)):

        step = numbers[i]

        lista_1 = [step for _ in numbers[i + 1:]]

        output.extend(list(zip(lista_1, numbers[i + 1:])))

    return output
