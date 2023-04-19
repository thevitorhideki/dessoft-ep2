def define_posicoes(linha: int, coluna: int, orientacao: str, tamanho: int) -> list:
    posicao = []

    for i in range(tamanho):
        if orientacao == 'vertical':
            posicao.append([linha + i, coluna])
        else:
            posicao.append([linha, coluna + i])

    return posicao


def preenche_frota(frota: dict, nome_navio: str, linha: int, coluna: int, orientacao: str, tamanho: int) -> dict:
    frota.setdefault(nome_navio, []).append(
        define_posicoes(linha, coluna, orientacao, tamanho))

    return frota


def faz_jogada(tabuleiro: list[list], linha: int, coluna: int) -> list[list]:
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