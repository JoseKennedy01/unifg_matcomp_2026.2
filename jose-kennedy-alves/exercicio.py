from itertools import product

def calcular_saida_alarme(porta_aberta, ignicao_ligada, farois_ligados):
    # Regra 1: farois ligados e ignicao desligada.
    alerta_bateria = farois_ligados and not ignicao_ligada

    # Regra 2: porta aberta e ignicao ligada.
    alerta_seguranca = porta_aberta and ignicao_ligada

    # O alarme toca se uma das regras for verdadeira.
    return int(alerta_bateria or alerta_seguranca)


def calcular_mintermo(porta_aberta, ignicao_ligada, farois_ligados):
    return porta_aberta * 4 + ignicao_ligada * 2 + farois_ligados


def main():
    mintermos = []

    print("A B C | S")
    print("----------")

    for porta_aberta, ignicao_ligada, farois_ligados in product((0, 1), repeat=3):
        saida = calcular_saida_alarme(
            porta_aberta,
            ignicao_ligada,
            farois_ligados
        )

        print(f"{porta_aberta} {ignicao_ligada} {farois_ligados} | {saida}")

        if saida == 1:
            mintermo = calcular_mintermo(
                porta_aberta,
                ignicao_ligada,
                farois_ligados
            )
            mintermos.append(mintermo)

    mintermos_formatados = ", ".join(map(str, mintermos))

    print()
    print(f"S(A, B, C) = soma de mintermos m({mintermos_formatados})")

if __name__ == "__main__":
    main()