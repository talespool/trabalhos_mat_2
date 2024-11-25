from resolucao import Resolucao
def main():
    matriz = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    res = Resolucao()



    # 1. Análise da matriz de adjacência
    resultado = res.analisar_matriz_adjacencia(matriz)
    print("Análise da matriz de adjacência:", resultado)

    # 2. Cálculo de hubs e autoridades
    autoridade, hub = res.calcular_hub_autoridade(matriz)
    print("Autoridade:", autoridade)
    print("Hub:", hub)

    # 3. Ordenar os nós
    autoridade_ordenada = res.ordenar_nos(autoridade)
    hub_ordenado = res.ordenar_nos(hub)
    print("Nós ordenados por autoridade:", autoridade_ordenada)
    print("Nós ordenados por hub:", hub_ordenado)
    
    
    
    
if __name__ == "__main__":
    main()
