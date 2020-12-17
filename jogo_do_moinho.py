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


def posicao_para_inteiro(p):
    # posicao_para_inteiro: posicao -> N
    """Devolve um inteiro de 0 a 8 que corresponde ao indice da posicao p
        na sucessao 'a1', 'b2', 'b3', 'a2', ..., 'b3', 'c3'."""

    pos_c = ord(obter_pos_c(p)) - ord('a')
    pos_l = ord(obter_pos_l(p)) - ord('1')
    return pos_l * 3 + pos_c


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

    pos = posicao_para_inteiro(p)

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

    for outro_j in pecas:
        if pecas_iguais(j, cria_peca(outro_j)):
            return pecas[outro_j]


###############################################################################
# TAD TABULEIRO
###############################################################################
def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    """Devolve um tabuleiro de jogo do moinho do 3x3 sem posicoes ocupadas por
        pecas de jogador."""

    return [cria_peca(' ')] * 9


def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    """Recebe um tabuleiro e devolve uma copia nova do tabuleiro."""

    return t.copy()


def obter_peca(t, p):
    # tabuleiro x posicao -> peca
    """Devolve a peca na posicao p do tabuleiro. Se a posicao nao estiver
        ocupada, devolve umaa peca livre."""

    pos = posicao_para_inteiro(p)

    return t[pos]

def obter_vetor(t, s):
    # tabuleiro x str -> tuplo de pecas
    """Devolve todas as pecas da linha ou coluna especificada pelo seu
        argumento."""

    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    pecas = ()

    if s in cs:
        for l in ls:
            pecas += (obter_peca(t, cria_posicao(s, l)), )

    if s in ls:
        for c in cs:
            pecas += (obter_peca(t, cria_posicao(c, s)), )

    return pecas


def coloca_peca(t, j, p):
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t colocando a peca j na posicao p,
        e devolve o proprio tabuleiro."""

    pos = posicao_para_inteiro(p)

    t[pos] = j
    return t


def remove_peca(t, p):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t removendo a peca da posicao p, e
        devolve o proprio tabuleiro."""

    return coloca_peca(t, cria_peca(' '), p)


def move_peca(t, p1, p2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t movendo a peca que se encontra na
        posicao p1 para a posicao p2, e devolve o proprio tabuleiro."""

    coloca_peca(t, obter_peca(t, p1), p2)
    return remove_peca(t, p1)


def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD tabuleiro e False caso
        contrario."""

    if not (
        isinstance(arg, list) and len(arg) == 9 and
        all([eh_peca(j) for j in arg])
    ):
        return False

    Xs = arg.count(cria_peca('X'))
    Os = arg.count(cria_peca('O'))

    if not (Xs - Os in (-1, 1) and Xs <= 3 and Os <= 3):
        return False

    ss = ('a','b','c','1','2','3')
    ganhadores = 0

    for s in ss:
        vet = obter_vetor(t, s)
        if vet.count(cria_peca('X')) == 3 or vet.count(cria_peca('O')) == 3:
            ganhadores += 1

    return ganhadores <= 1


def eh_posicao_livre(t, p):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """Devolve True apenas no caso da posicao p do tabuleiro corresponder a uma
        posicao livre."""

    return pecas_iguais(obter_peca(t, p), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """Devolve True apenas se t1 e t2 são tabuleiros e são iguais."""

    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def linha_para_str(t, l):
    # linha_para_str: tabuleiro x str -> str
    """Devolve a cadeia de caracteres que representa a linha do tabuleiro."""

    out = l + ' '

    for j in obter_vetor(t, l):
        out += peca_para_str(j) + '-'

    return out[:-1] + '\n'


def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    """Devolve a cadeia de carateres que representa o tabuleiro."""

    separador = '| / | \ |'

    out = ''

    for c in ('a', 'b', 'c'):
        out += '   ' + c
    out += '\n'

    out += linha_para_str(t, '1')
    out += '   ' + separador + '\n'
    out += linha_para_str(t, '2')
    out += '   ' + separador[::-1] + '\n'
    out += linha_para_str(t, '3')

    return out[:-1]


def tuplo_para_tabuleiro(t):
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    """Devolve o tabuleiro que e representado pelo tuplo t com 3 tuplos."""

    pecas = {1: 'X', -1: 'O', 0: ' '}
    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    tabuleiro = cria_tabuleiro()

    for l in range(3):
        for c in range(3):
            j = cria_peca(pecas[t[l][c]])
            p = cria_posicao(cs[c], ls[l])
            coloca_peca(tabuleiro, j, p)

    return tabuleiro


def obter_ganhador(t):
    # obter_ganhador: tabuleiro -> peca
    """Devolve uma peca do jogador que tenha as suas 3 pecas em linha na
        na vertical ou na horizontal no tabuleiro. Se nao existir nenhum
        ganhador, devolve uma peca livre."""

    ss = ('a','b','c','1','2','3')

    for s in ss:
        vet = obter_vetor(t, s)
        if vet.count(cria_peca('X')) == 3 or vet.count(cria_peca('O')) == 3:
            return vet[0]

    return cria_peca(' ')


def obter_posicoes_jogador(t, j):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    """Devolve um tuplo com as posicoes ocupadas pelas pecas j de um dos dois
        jogadores na ordem de leitura do tabuleiro."""

    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    ps = ()

    for l in ls:
        for c in cs:
            p = cria_posicao(c, l)
            if pecas_iguais(j, obter_peca(t, p)):
                ps += (p, )

    return ps


def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    """Devolve um tuplo com as posicoes nao ocupadas pelas pecas de qualquer um
        dos dois jogadores na ordem de leitura do tabuleiro."""

    return obter_posicoes_jogador(t, cria_peca(' '))


