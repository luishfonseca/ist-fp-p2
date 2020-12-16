# 99266 Luis Fonseca

###############################################################################
# TAD POSICAO
###############################################################################
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    """Recebe duas cadeias de carateres correspondentes a coluna c e a linha l
        de uma posicao e devolve a posicao correspondente."""

    if not (
        isinstance(c, str) and isinstance(l, str) and
        len(c) == len(l) == 1 and
        ord('a') <= ord(c) <= ord('c') and
        ord('1') <= ord(l) <= ord('3')
    ):
        raise ValueError('cria_posicao: argumentos invalidos')

    return [ord(c) - ord('a'), ord(l) - ord('1')]

def cria_posicao_copia(p):
    # cria_posicao_copia: posicao -> posicao
    """Recebe uma posicao e devolve uma copia nova da posicao."""

    return p.copy()


def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    """Devolve a componente coluna c da posicao p."""

    return chr(p[0] + ord('a'))


def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    """Devolve a componente linha l da posicao p."""

    return chr(p[1] + ord('1'))


def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD posicao e False caso
        contrario."""

    return (
        isinstance(arg, list) and len(arg) == 2 and
        all(map(lambda x: isinstance(x, int) and 0 <= x <= 2, arg))
    )

def posicoes_iguais(p1, p2):
    # posicoes_iguais: posicao x posicao -> booleano
    """Devolve True apenas se p1 e p2 sao posicoes e sao iguais."""

    return (
        eh_posicao(p1) and eh_posicao(p2) and
        obter_pos_c(p1) == obter_pos_c(p2) and
        obter_pos_l(p1) == obter_pos_l(p1)
    )


def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    """Devolve a cadeia de carateres 'cl' que representa o seu argumento, sendo
        os valores c e l as componentes coluna e linha de p."""

    return obter_pos_c(p) + obter_pos_l(p)


def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    """Devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
        ordem de leitura do tabuleiro."""

    pass


