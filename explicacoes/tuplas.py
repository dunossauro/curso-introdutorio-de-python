
minha_tupla = (
    'Eduardo', 27, '887848484', 'R. dos bobos', 0
)

nome, idade, *coisas_que_nao_quero = minha_tupla

nome, idade = idade, nome


def minha_func():
    return 1, 2, 3
