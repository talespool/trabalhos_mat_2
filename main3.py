from resolucao import Resolucao
def main():
    matriz = [
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
    ]

    res = Resolucao(matriz)

    autoridade, centro = res.calcular_centro_autoridade(5)
    print(" ")
    print("Novos pesos centro:", centro)
    print("Novos pesos autoridade:", autoridade)
    print(" ")
    print("RESPOSTA", res.ordenar(autoridade))
    print("==================================")

    matriz = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
    ]

    res = Resolucao(matriz)

    autoridade, centro = res.calcular_centro_autoridade(6)
    print(" ")
    print("Novos pesos centro:", centro)
    print("Novos pesos autoridade:", autoridade)
    print(" ")
    print("RESPOSTA", res.ordenar(autoridade))
    print("==================================")

    matriz = [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ]

    res = Resolucao(matriz)

    autoridade, centro = res.calcular_centro_autoridade(7)
    print(" ")
    print("Novos pesos centro:", centro)
    print("Novos pesos autoridade:", autoridade)
    print(" ")
    print("RESPOSTA", res.ordenar(autoridade))
    print("==================================")

    matriz = [
        [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    res = Resolucao(matriz)

    autoridade, centro = res.calcular_centro_autoridade(8)
    print(" ")
    print("Novos pesos centro:", centro)
    print("Novos pesos autoridade:", autoridade)
    print(" ")
    print("RESPOSTA", res.ordenar(autoridade))
    print("==================================")
    
    
if __name__ == "__main__":
    main()
