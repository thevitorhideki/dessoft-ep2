def define_posicoes(linha: int, coluna: int, orientacao: str, tamanho: int) -> list:
    posicao = []

    for i in range(tamanho):
        if orientacao == 'vertical':
            posicao.append([linha + i, coluna])
        else:
            posicao.append([linha, coluna + i])

    return posicao


def preenche_frota(frota: dict, nome_navio: str, linha: int, coluna: int, orientacao: str, tamanho: int) -> dict:
    frota.setdefault(nome_navio, []).append(define_posicoes(linha, coluna, orientacao, tamanho))

    return frota


def faz_jogada(tabuleiro: list, linha: int, coluna: int) -> list:
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


def posiciona_frota(frota: dict) -> list:
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    for i in frota.values():
        for j in i:
            for k in j:
                tabuleiro[k[0]][k[1]] = 1

    return tabuleiro


def afundados(frota: dict, tabuleiro: list) -> int:
    n_afundados = 0
    for f in frota.values():
        for cordenadas in f:
            count = 0
            for cordenada in cordenadas:
                if tabuleiro[cordenada[0]][cordenada[1]] == 'X':
                    count += 1
            if count == len(cordenadas):
                n_afundados += 1

    return n_afundados


def posicao_valida(frota: dict, linha: int, coluna: int, orientacao: str, tamanho: int) -> bool:
    posicoes_ocupadas = []
    for i in frota.values():
        for j in i:
            for k in j:
                posicoes_ocupadas.append(k)

    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for i in posicao:
        if i[0] >= 10 or i[1] >= 10:
            return False
    for i in posicao:
        if i in posicoes_ocupadas:
            return False
    return True


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

quantidade = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}
for navio, qnt in quantidade.items():
    count = 0
    while count < qnt:
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {5 - qnt}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if navio != 'submarino':
            orientacao = int(input('Orientação - [1] Vertical [2] Horizontal: '))
            orientacao = 'vertical' if orientacao == 1 else 2
        else:
            orientacao = 1
        if posicao_valida(frota, linha, coluna, orientacao, (5 - qnt)):
            preenche_frota(frota, navio, linha, coluna, orientacao, (5 - qnt))
            count += 1
        else:
            print('Esta posição não está válida!')

posicoes = []
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha = int(input('Linha: '))
    while linha > 9 or linha < 0:
        print('Linha inválida!')
        linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    while coluna > 9 or coluna < 0:
        print('Coluna inválida')
        coluna = int(input('Coluna: '))
    while (linha, coluna) in posicoes:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        linha = int(input('Linha: '))
        while linha > 9 or linha < 0:
            print('Linha inválida!')
            linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        while coluna > 9 or coluna < 0:
            print('Coluna inválida')
            coluna = int(input('Coluna: '))
    posicoes.append((linha, coluna))
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False