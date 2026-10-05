'''
Parte 2: Desafio Prático em Python

Escreva uma função `detectar_rotas_circulares(linhas: dict[str, list[str]]) -> set[tuple[str, str]]` que utilize operações de conjuntos e produto cartesiano para identificar todas as conexões bidirecionais diretas entre pares de estações.
'''

from itertools import product

def detectar_rotas_circulares(linhas: dict[str, list[str]]) -> set[tuple[str, str]]:
    # Cria um conjunto com todas as estações cadastradas:
    estacoes = set(linhas)

    # Cria pares ordenados com todas as combinações possíveis de estações:
    pares_possiveis = set(product(estacoes, repeat=2))

    # Registra todas as conexões diretas informadas no dicionário.
    conexoes_diretas = {
        (origem, destino)
        for origem, destinos in linhas.items()
        for destino in destinos
        if origem != destino and destino in estacoes
    }

    # Identifica pares em que existe conexão de ida e de volta:
    conexoes_bidirecionais = {
        (origem, destino)
        for origem, destino in pares_possiveis
        if (
            (origem, destino) in conexoes_diretas
            and (destino, origem) in conexoes_diretas
        )
    }

    # Ordena cada par para evitar duplicação entre ida e volta:
    return {
        tuple(sorted((origem, destino)))
        for origem, destino in conexoes_bidirecionais
    }

linhas_metro = {
    "Central": ["Norte", "Sul"],
    "Norte": ["Central", "Leste"],
    "Sul": ["Central"],
    "Leste": ["Norte", "Oeste"],
    "Oeste": ["Leste"],
    "Parque": ["Museu"],
    "Museu": []
}

rotas_circulares = detectar_rotas_circulares(linhas_metro)

print("Rotas circulares encontradas:")
for rota in sorted(rotas_circulares):
    print(rota)