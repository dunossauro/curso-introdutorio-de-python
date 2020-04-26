



palavra = 'abracadabra'
vogais = 'aeiou'

# for letra in palavra:
#     if letra == 'a':
#         print('Eduardo')
#     elif letra == 'e':
#         print('Eduardo')
#     elif letra == 'i':
#         print('Eduardo')
#     elif letra == 'o':
#         print('Eduardo')
#     elif letra == 'u':
#         print('Eduardo')
#     else:
#         print(letra)


for letra in palavra:
    if letra in vogais:
        print('Eduardo')
    else:
        print(letra)
