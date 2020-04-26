

def nome(argumento_posicional, *pacote_de_argumentos):
    print(
        argumento_posicional,
        pacote_de_argumentos
    )

def nome2(
    argumento_nomeado='n tem nada',
    **pacote_nomeado
):
    print(
        argumento_nomeado,
        pacote_nomeado
    )
