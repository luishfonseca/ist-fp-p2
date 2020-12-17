# 99266 Luis Fonseca

###############################################################################
# TAD POSICAO
###############################################################################
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    """Recebe duas cadeias de carateres correspondentes a coluna c e a linha l
        de uma posicao e devolve a posicao correspondente."""

    if not (
        isinstance(c, str) and isinstance(l, str) and len(c) == len(l) == 1 and
        ord('a') <= ord(c) <= ord('c') and ord('1') <= ord(l) <= ord('3')
    ):
        raise ValueError('cria_posicao: argumentos invalidos')

    return (ord(l) - ord('1')) * 3 + ord(c) - ord('a')

def cria_posicao_copia(p):
    # cria_posicao_copia: posicao -> posicao
    """Recebe uma posicao e devolve uma copia nova da posicao."""

    return p


def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    """Devolve a componente coluna c da posicao p."""

    return chr(p % 3 + ord('a'))


def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    """Devolve a componente linha l da posicao p."""

    return chr(p // 3 + ord('1'))


def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD posicao e False caso
        contrario."""

    return isinstance(arg, int) and 0 <= arg < 9


def posicoes_iguais(p1, p2):
    # posicoes_iguais: posicao x posicao -> booleano
    """Devolve True apenas se p1 e p2 sao posicoes e sao iguais."""

    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    """Devolve a cadeia de carateres 'cl' que representa o seu argumento, sendo
        os valores c e l as componentes coluna e linha de p."""

    return obter_pos_c(p) + obter_pos_l(p)


def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    """Devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
        ordem de leitura do tabuleiro."""

    adjacencias = (
        (1, 3, 4),
        (0, 2, 4),
        (1, 4, 5),
        (0, 4, 6),
        (0, 1, 2, 3, 5, 6, 7, 8),
        (2, 4, 8),
        (3, 4, 7),
        (4, 6, 8),
        (4, 5, 7)
    )

    pos_c = ord(obter_pos_c(p)) - ord('a')
    pos_l = ord(obter_pos_l(p)) - ord('1')
    pos = pos_l * 3 + pos_c

    adjs = ()
    for adj in adjacencias[pos]:
        adj_c = chr(adj % 3 + ord('a'))
        adj_l = chr(adj // 3 + ord('1'))
        adjs += (cria_posicao(adj_c, adj_l),)

    return adjs

"""
def obter_posicoes_adjacentes(p):

    pos_c = ord(obter_pos_c(p)) - ord('a')
    pos_l = ord(obter_pos_l(p)) - ord('1')

    pos_adjs = ()

    for adj_rel_l in range(-1, 2):
        for adj_rel_c in range(-1, 2):

            adj_c = pos_c + adj_rel_c
            adj_l = pos_l + adj_rel_l

            if not (
                (pos_c == adj_c and pos_l == adj_l) or # adj eh a pos
                adj_c < 0 or adj_c >= 3 or
                adj_c < 0 or adj_l >= 3 or             # adj nao eh valida
                ((pos_l * 3 + pos_c) % 2 != 0 and      # pos fora das diagonais
                adj_rel_c != 0 and adj_rel_l != 0)     # adj eh diagonal a pos
            ):

                adj_c = chr(adj_c + ord('a'))
                adj_l = chr(adj_l + ord('1'))
                print(adj_c + adj_l)
                adj = cria_posicao(adj_c, adj_l)
                pos_adjs += (adj,)

    return pos_adjs
"""


###############################################################################
# TAD PECA
###############################################################################
def cria_peca(s):
    # cria_peca: str -> peca
    """Recebe uma cadeia de carateres correspondente ao identificador de um dos
        dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca
        correspondente."""

    if s not in ('X', 'O', ' '):
        raise ValueError('cria_peca: argumento invalido')

    return s


def cria_copia_peca(j):
    # cria_copia_peca: peca -> peca
    """Recebe uma peca e devolve uma copia nova da peca."""

    return j


def eh_peca(arg):
    # eh_peca: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD peca e False caso
        contrario."""

    return arg in ('X', 'O', ' ')


def pecas_iguais(j1, j2):
    # pecas_iguais: peca x peca -> booleano
    """Devolve True apenas se p1 e p2 sao pecas e sao iguais."""

    return eh_peca(j1) and eh_peca(j2) and j1 == j2


def peca_para_str(j):
    # peca_para_str: peca -> str
    """Devolve a cadeia de caracteres que representa o jogador dono da peca,
        isto e, '[X]', '[O]' ou '[ ]'."""

    return '[' + j + ']'


def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> N
    """Devolve um inteiro valor 1, -1 ou 0 dependendo se a peca e do jogador
        'X', 'O' ou livre, respetivamente."""

    pecas = {'X': 1, 'O': -1, ' ': 0}

    return {cria_peca(k): v for k, v in pecas.items()}[j]


