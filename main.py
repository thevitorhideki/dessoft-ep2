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
