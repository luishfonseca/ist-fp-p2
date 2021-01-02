# 99266 Luis Fonseca

###############################################################################
# FUNCOES AUXILIARES
###############################################################################
def pertence(el, els, teste):
    # pertence: el x iter x func -> bool
    """Verifica se um elemento pertence a um iteravel usando o teste dado."""

    return any(teste(el, el2) for el2 in els)


def conta(el, els, teste):
    #conta: el x iter x func -> N
    """Retorna a quantidade de elementos el num iteravel usando o teste dado."""

    cnt = 0
    for el2 in els:
        if teste(el, el2):
            cnt += 1

    return cnt


def eh_adjacente(p1_c, p1_l, p2_c, p2_l):
    # eh_adjacente: inteiro x inteiro x inteiro x inteiro -> booleano
    """Devolve um booleano caso a pseudo posicao p2 representada por p2_c e
        p2_l seja valida e tenha uma relacao de adjacencia com a pseudo posicao
        representada por p1_c e p2_l"""

    delta_c = p2_c - p1_c
    delta_l = p2_l - p1_l

    return (
        (p1_c != p2_c or p1_l != p2_l) and  # p1 != p2
        0 <= p2_c < 3 and 0 <= p2_l < 3 and # p2 eh valida
        (delta_c == 0 or delta_l == 0 or    # p2 eh horizontal ou vertical a p1
        (p1_l * 3 + p1_c) % 2 == 0)     # p2 eh canto ou centro e diagonal a p1
    )


def eh_vitoria(vet):
    # eh_vitoria: tuplo de pecas -> booleano
    """Devolve True caso o tuplo de pecas consista em 3 pecas do mesmo
        jogador."""

    return (
        conta_pecas(cria_peca('X'), vet) == 3 or
        conta_pecas(cria_peca('O'), vet) == 3
    )


def linha_para_str(t, l):
    # linha_para_str: tabuleiro x str -> str
    """Devolve a cadeia de caracteres que representa a linha do tabuleiro."""

    out = l + ' '

    for j in obter_vetor(t, l):
        out += peca_para_str(j) + '-'

    return out[:-1] + '\n'


###############################################################################
# TAD POSICAO
# Rep. Interna: Lista de dois elementos. O primeiro corresponde a coluna ('a',
#               'b' ou 'c'), o segundo correponde a linha ('1', '2' ou '3').
# Operacoes basicas:
#   cria_posicao: str x str -> posicao
#   cria_copia_posicao: posicao -> posicao
#   obter_pos_c: posicao -> str
#   obter_pos_l: posicao -> str
#   eh_posicao: universal -> booleano
#   posicoes_iguais: posicao x posicao -> booleano
#   posicao_para_str: posicao -> str
# Funcoes de alto nivel:
#   obter_posicoes_adjacentes: posicao -> tuplo de posicoes
#   posicao_para_inteiro: posicao -> N
#   pertence_pos: posicao x iter de posicoes -> bool
###############################################################################
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    """Recebe duas cadeias de carateres correspondentes a coluna c e a linha l
        de uma posicao e devolve a posicao correspondente."""

    if c not in ('a', 'b', 'c') or l not in ('1', '2', '3'):
        raise ValueError('cria_posicao: argumentos invalidos')

    return [c, l]

def cria_copia_posicao(p):
    # cria_copia_posicao: posicao -> posicao
    """Recebe uma posicao e devolve uma copia nova da posicao."""

    return p.copy()


def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    """Devolve a componente coluna c da posicao p."""

    return p[0]


def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    """Devolve a componente linha l da posicao p."""

    return p[1]


def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD posicao e False caso
        contrario."""

    return (
        isinstance(arg, list) and len(arg) == 2 and
        arg[0] in ('a','b','c') and arg[1] in ('1','2','3')
    )


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
    """Devolve um inteiro de 0 a 8 que corresponde ao indice da posicao p na
        sucessao 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'."""

    pos_c = ord(obter_pos_c(p)) - ord('a')
    pos_l = ord(obter_pos_l(p)) - ord('1')
    return pos_l * 3 + pos_c


def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    """Devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
        ordem de leitura do tabuleiro."""

    pos_c = ord(obter_pos_c(p)) - ord('a')
    pos_l = ord(obter_pos_l(p)) - ord('1')

    pos_adjs = ()

    for adj_rel_l in range(-1, 2):
        for adj_rel_c in range(-1, 2):

            adj_c = pos_c + adj_rel_c
            adj_l = pos_l + adj_rel_l

            if eh_adjacente(pos_c, pos_l, adj_c, adj_l):
                adj_c = chr(adj_c + ord('a'))
                adj_l = chr(adj_l + ord('1'))
                adj = cria_posicao(adj_c, adj_l)
                pos_adjs += (adj,)

    return pos_adjs


def pertence_pos(p, ps):
    # pertence_pos: posicao x iter de posicoes -> bool
    """Verifica se uma posicao p pertence a um iteravel de posicoes."""

    return pertence(p, ps, posicoes_iguais)


###############################################################################
# TAD PECA
# Rep. Interna: lista de um elemento ('X', 'O' ou ' ').
# Operacoes basicas:
#   cria_peca: str -> peca
#   cria_copia_peca: peca -> peca
#   eh_peca: universal -> booleano
#   pecas_iguais: peca x peca -> booleano
#   peca_para_str: peca -> str
# Funcoes de alto nivel:
#   peca_para_inteiro: peca -> N
#   inteiro_para_peca: N -> peca
#   obter_oponente: peca -> peca
###############################################################################
def cria_peca(s):
    # cria_peca: str -> peca
    """Recebe uma cadeia de carateres correspondente ao identificador de um dos
        dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca
        correspondente."""

    if s not in ('X', 'O', ' '):
        raise ValueError('cria_peca: argumento invalido')

    return [s]


def cria_copia_peca(j):
    # cria_copia_peca: peca -> peca
    """Recebe uma peca e devolve uma copia nova da peca."""

    return j.copy()


def eh_peca(arg):
    # eh_peca: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD peca e False caso
        contrario."""

    return isinstance(arg, list) and len(arg) == 1 and arg[0] in ('X', 'O', ' ')


def pecas_iguais(j1, j2):
    # pecas_iguais: peca x peca -> booleano
    """Devolve True apenas se p1 e p2 sao pecas e sao iguais."""

    return eh_peca(j1) and eh_peca(j2) and j1 == j2


def peca_para_str(j):
    # peca_para_str: peca -> str
    """Devolve a cadeia de caracteres que representa o jogador dono da peca,
        isto e, '[X]', '[O]' ou '[ ]'."""

    return '[' + j[0] + ']'


def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> N
    """Devolve um inteiro com valor 1, -1 ou 0 dependendo se a peca e do
        jogador 'X', 'O' ou livre, respetivamente."""

    pecas = {'[X]': 1, '[O]': -1, '[ ]': 0}

    return pecas[peca_para_str(j)]


def inteiro_para_peca(n):
    # inteiro_para_peca: N -> peca
    """Devolve a peca do jogador 'X', 'O' ou livre dependendo se o inteiro eh
        1, -1 ou 0, respetivamente."""

    pecas = {1: 'X', -1: 'O', 0: ' '}

    return cria_peca(pecas[n])


def obter_oponente(j):
    # obter_oponente: peca -> peca
    """Devolve a peca que corresponde ao oponente do jogador dono da peca j"""

    oponente = -peca_para_inteiro(j)

    return inteiro_para_peca(oponente)


def conta_pecas(j, js):
    # conta_pecas: peca x iter de pecas -> N
    """Retorna a quantidade de pecas j num iteravel."""

    return conta(j, js, pecas_iguais)


###############################################################################
# TAD TABULEIRO
# Rep. Interna: lista de nove pecas. Indices correspondem a ordem de leitura
#               definida da esquerda para a direita seguida de cima para baixo.
# Operacoes basicas:
    # cria_tabuleiro: {} -> tabuleiro
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    # obter_peca: tabuleiro x posicao -> peca
    # obter_vetor: tabuleiro x str -> tuplo de pecas
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    # remove_peca: tabuleiro x posicao -> tabuleiro
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    # eh_tabuleiro: universal -> booleano
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    # tabuleiro_para_str: tabuleiro -> str
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
# Funcoes de alto nivel:
    # obter_ganhador: tabuleiro -> peca
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
###############################################################################
def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    """Devolve um tabuleiro de jogo do moinho do 3x3 sem posicoes ocupadas por
        pecas de jogador."""

    return [cria_peca(' ')] * 9


def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    """Recebe um tabuleiro e devolve uma copia nova do tabuleiro."""

    copia = []
    for j in t:
        copia.append(cria_copia_peca(j))

    return copia


def obter_peca(t, p):
    # obter_peca: tabuleiro x posicao -> peca
    """Devolve a peca na posicao p do tabuleiro. Se a posicao nao estiver
        ocupada, devolve umaa peca livre."""

    pos = posicao_para_inteiro(p)

    return t[pos]


def obter_vetor(t, s):
    # obter_vetor: tabuleiro x str -> tuplo de pecas
    """Devolve todas as pecas da linha ou coluna especificada pelo seu
        argumento."""

    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    pecas = ()

    if s in cs:
        for l in ls:
            pecas += (obter_peca(t, cria_posicao(s, l)), )

    else:
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

    j = obter_peca(t, p1)
    remove_peca(t, p1)
    return coloca_peca(t, j, p2)


def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD tabuleiro e False caso
        contrario."""

    if not (
        isinstance(arg, list) and len(arg) == 9 and
        all(eh_peca(j) for j in arg)
    ):
        return False

    ss = ('a','b','c','1','2','3')
    ganhadores = 0

    for s in ss:
        vet = obter_vetor(arg, s)
        if eh_vitoria(vet):
            ganhadores += 1

    Xs = conta_pecas(cria_peca('X'), arg)
    Os = conta_pecas(cria_peca('O'), arg)

    return ganhadores <= 1 and abs(Xs - Os) <= 1 and Xs <= 3 and Os <= 3


def eh_posicao_livre(t, p):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """Devolve True apenas no caso da posicao p do tabuleiro corresponder a uma
        posicao livre."""

    return pecas_iguais(obter_peca(t, p), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """Devolve True apenas se t1 e t2 sao tabuleiros e sao iguais."""

    return (
        eh_tabuleiro(t1) and eh_tabuleiro(t2) and
        all(pecas_iguais(t1[n], t2[n]) for n in range(9))
    )


def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    """Devolve a cadeia de carateres que representa o tabuleiro."""

    separador = '| \ | / |'

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

    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    tabuleiro = cria_tabuleiro()

    for l in range(3):
        for c in range(3):
            j = inteiro_para_peca(t[l][c])
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
        if eh_vitoria(vet):
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


###############################################################################
# FUNCOES ADICIONAIS
###############################################################################
def obter_fase(t):
    # obter_fase: tabuleiro -> str
    """Devolve 'colocar' ou 'mover' de acordo com a fase em que se
        encontra o tabuleiro dado."""

    Xs = obter_posicoes_jogador(t, cria_peca('X'))
    Os = obter_posicoes_jogador(t, cria_peca('O'))

    if len(Xs) == len(Os) == 3:
        return 'mover'
    else:
        return 'colocar'


def eh_movimento_valido(t, j, mov):
    # eh_movimento_valido: tabuleiro x peca x tuplo de posicoes -> booleano
    """Devolve True caso o movimento introduzido pelo jogador seja valido."""

    ps_adjs = obter_posicoes_adjacentes(mov[0])
    ps_livres = obter_posicoes_livres(t)

    return (
        pecas_iguais(obter_peca(t, mov[0]), j) and
        pertence_pos(mov[1], ps_livres) and pertence_pos(mov[1], ps_adjs) or
        (all(not pertence_pos(p, ps_livres) for p in ps_adjs) and
        posicoes_iguais(*mov))
    )


def obter_movimento_manual(t , j):
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    """Devolve um tuplo com uma ou duas posicoes que representam uma posicao ou
        um movimento introduzido manualmente pelo jogador."""

    if obter_fase(t) == 'colocar':
        mov = obter_colocacao_manual(t)
        if mov:
            return mov
    else:
        m_str = input('Turno do jogador. Escolha um movimento: ')

        if (
            len(m_str) == 4 and
            m_str[0] in ('a', 'b', 'c') and m_str[1] in ('1', '2', '3') and
            m_str[2] in ('a', 'b', 'c') and m_str[3] in ('1', '2', '3')
        ):
            p1 = cria_posicao(m_str[0], m_str[1])
            p2 = cria_posicao(m_str[2], m_str[3])
            mov = (p1, p2)

            if eh_movimento_valido(t, j, mov):
                return mov

    raise ValueError('obter_movimento_manual: escolha invalida')


def obter_colocacao_manual(t):
    # obter_colocacao_manual: tabuleiro -> tuplos de posicoes
    """Devolve um tuplo com uma posicao que representa uma posicao introduzida
        manualmente pelo jogador durante a fase de colocacao."""

    p_str = input('Turno do jogador. Escolha uma posicao: ')

    if (
        len(p_str) == 2 and
        p_str[0] in ('a', 'b', 'c') and p_str[1] in ('1', '2', '3')
    ):

        ps_livres = obter_posicoes_livres(t)

        p = cria_posicao(p_str[0], p_str[1])

        if pertence_pos(p, ps_livres):
            return (p, )


def obter_movimento_auto(t, j, s):
    # obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    """Devolve um tuplo com uma ou duas posicoes que representam uma posicao ou
        um movimento escolhido automaticamente."""

    if obter_fase(t) == 'colocar':
        return obter_colocacao_auto(t, j)

    elif s == 'facil':
        return obter_movimento_auto_facil(t, j)

    elif s == 'normal':
        return minimax(t, j, 1)

    elif s == 'dificil':
        return minimax(t, j, 5)


def obter_movimento_auto_facil(t, j):
    # obter_movimento_auto_facil: tabuleiro x peca x str -> tuplo de posicoes
    """Devolve um tuplo com duas posicoes que representam uma posicao ou
        um movimento escolhido automaticamente na fase de movimento na
        dificuldade facil."""

    ps_livres = obter_posicoes_livres(t)
    ps_jogador = obter_posicoes_jogador(t, j)

    for p in ps_jogador:
        ps_adjacentes = obter_posicoes_adjacentes(p)
        for adj in ps_adjacentes:
            if pertence_pos(adj, ps_livres):
                return (p, adj)
    return (ps_jogador[0], ps_jogador[0])


def eh_melhor(j, novo_val, max_val):
    # eh_melhor: peca x N x N -> booleano
    """Devolve True caso, da perspectiva do jogador j, o valor do novo
        tabuleiro seja melhor que melhor valor anterior."""

    return ((pecas_iguais(j, cria_peca('X')) and novo_val > max_val) or
            (pecas_iguais(j, cria_peca('O')) and novo_val < max_val))


def minimax(t, j, profundidade):
    # minimax: tabuleiro x peca x N -> tuplo de posicoes
    """Devolve um tuplo de duas posicoes que representam um movimento escolhido
        pelo algoritmo de minimax."""

    def aux_minimax(t, j, d, movs):
        if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or d == 0:
            return peca_para_inteiro(obter_ganhador(t)), movs
        melhor_movs = ()
        ps_livres = obter_posicoes_livres(t)
        oponente = obter_oponente(j)
        max_val = peca_para_inteiro(oponente)
        for p in obter_posicoes_jogador(t, j):
            for adj in obter_posicoes_adjacentes(p):
                if pertence_pos(adj, ps_livres):
                    mov = (p, adj)
                    novo_t = move_peca(cria_copia_tabuleiro(t), *mov)
                    novo_val, novo_movs = \
                        aux_minimax(novo_t, oponente, d - 1, movs + (mov,))
                    if not melhor_movs or eh_melhor(j, novo_val, max_val):
                        max_val, melhor_movs = novo_val, novo_movs
        return max_val, melhor_movs

    val, movs = aux_minimax(t, j, profundidade, ())
    if len(movs) != 0:
        return movs[0]


def obter_colocacao_auto(t, j):
    # obter_colocacao_auto: tabuleiro x peca -> tuplo de posicoes
    """Devolve um tuplo com uma posicao que representam uma posicao escolhida
        automaticamente na fase de colocacao."""

    acoes = (
        vitoria,
        bloqueio,
        centro,
        canto_vazio,
        lateral_vazio
    )

    for acao in acoes:
        p = acao(t,j)
        if p:
            return (p, )


def vitoria(t, j):
    # bloqueio: tabuleiro x peca -> posicao
    """Se o jogador dono da peca j tiver um dois em linha devolve a posicao
        livre restante."""

    dois_em_linha = ()

    for s in ('a', 'b', 'c', '1', '2', '3'):
        vec = obter_vetor(t, s)
        if conta_pecas(j, vec) == 2:
            dois_em_linha += (s, )

    for p in obter_posicoes_livres(t):
        if obter_pos_c(p) in dois_em_linha or obter_pos_l(p) in dois_em_linha:
            return p


def bloqueio(t, j):
    # bloqueio: tabuleiro x peca -> posicao
    """Se o oponente do jogador dono da peca j tiver um dois em linha devolve a
        posicao livre restante."""

    return vitoria(t, obter_oponente(j))


def centro(t, _):
    # centro: tabuleiro -> posicao
    """Devolve a posicao central se esta estiver livre."""

    p = cria_posicao('b', '2')

    if pertence_pos(p, obter_posicoes_livres(t)):
        return p


def canto_vazio(t, _):
    # canto_vazio: tabuleiro -> posicao
    """Devolve o canto que e uma posicao livre caso exista."""

    cs = ('a', 'c')
    ls = ('1', '3')

    ps_livres = obter_posicoes_livres(t)

    for l in ls:
        for c in cs:
            p = cria_posicao(c, l)
            if pertence_pos(p, ps_livres):
                return p


def lateral_vazio(t, _):
    # lateral_vazio: tabuleiro -> posicao
    """Devolve a primeira lateral que e uma posicao livre caso exista."""

    cs = ('a', 'b', 'c')
    ls = ('1', '2', '3')

    ps_livres = obter_posicoes_livres(t)

    for c in cs:
        for l in ls:
            p = cria_posicao(c, l)
            if posicao_para_inteiro(p) != 0 and pertence_pos(p, ps_livres):
                return p


def moinho(j, dif):
    # moinho: str x str -> str
    """Funcao principal que permite jogar um jogo completo do jogo do moinho de
        um jogador contra o computador."""

    if j not in ('[X]', '[O]') or dif not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')

    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dif))

    t = cria_tabuleiro()
    turno = cria_peca('X')

    if j == peca_para_str(turno):
        j = cria_copia_peca(turno)
    else:
        j = obter_oponente(turno)

    while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
        print(tabuleiro_para_str(t))
        jogar_turno(t, j, dif, turno)
        turno = obter_oponente(turno)

    print(tabuleiro_para_str(t))
    return peca_para_str(obter_ganhador(t))


def jogar_turno(t, j, dif, turno):
    # jogar_turno: tabuleiro x peca x str x peca -> {}
    """Altera destrutivamente o tabuleiro de acordo com a jogada realizada."""

    if pecas_iguais(j, turno):
        mov = obter_movimento_manual(t, turno)
    else:
        print('Turno do computador ({}):'.format(dif))
        mov = obter_movimento_auto(t, turno, dif)

    if len(mov) == 1:
        coloca_peca(t, turno, mov[0])
    else:
        move_peca(t, mov[0], mov[1])
