import numpy as np
class Resolucao():
    #def __init__(self, matriz):
        #self.matriz = matriz
        

    def analisar_matriz_adjacencia(matriz):
        """
        Analisa uma matriz de adjacência e retorna informações sobre o grafo.
        """
        n = len(matriz)
        graus = [sum(matriz[i]) for i in range(n)]
        conexoes = [(i, j) for i in range(n) for j in range(n) if matriz[i][j] != 0]

        return {
            "graus": graus,
            "total_arestas": sum(graus) // 2,
            "conexoes": conexoes,
        }
        
    def calcular_hub_autoridade(matriz, iteracoes=100, tol=1e-6):
        """
        Calcula os vetores de hub e autoridade usando o algoritmo HITS.
        """
        n = len(matriz)
        matriz = np.array(matriz, dtype=float)
        
        # Inicializando os vetores
        autoridade = np.ones(n)
        hub = np.ones(n)

        for _ in range(iteracoes):
            nova_autoridade = matriz.T @ hub
            nova_hub = matriz @ autoridade

            # Normalizando os vetores
            nova_autoridade /= np.linalg.norm(nova_autoridade, 2)
            nova_hub /= np.linalg.norm(nova_hub, 2)

            # Verificando convergência
            if (np.allclose(nova_autoridade, autoridade, atol=tol) and
                np.allclose(nova_hub, hub, atol=tol)):
                break
            
            autoridade, hub = nova_autoridade, nova_hub

        return autoridade, hub
    
    def ordenar_nos(vetor):
        """
        Ordena os nós com base nos valores de um vetor (ex: hub ou autoridade).
        """
        return sorted(enumerate(vetor), key=lambda x: x[1], reverse=True)
    
    
