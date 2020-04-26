"""
Faça um programa que peça 2 números inteiros e um número float. Calcule e mostre:

A produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
"""

numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
numero_3 = float(input('Digite um número float: '))

resultado_1 = (numero_1 * 2) * (numero_2 / 2)

resultado_2 = numero_1 * 3 + numero_3

resultado_3 = numero_3 ** 3

print(f'Resultado 1: {resultado_1}')
print(f'Resultado 2: {resultado_2}')
print(f'Resultado 3: {resultado_3}')
