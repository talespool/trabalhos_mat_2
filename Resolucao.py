import numpy as np
from Calculos3 import Calculos3


class Resolucao:
    
    
    
    def __init__(self, matriz):
        """
        Inicializa a classe com uma matriz de adjacência para operações.
        """
        self.matriz = matriz
        self.calculo = Calculos3()
        
    
    def analisar_matriz_adjacencia(self):
        """
        Analisa a matriz de adjacência e retorna informações sobre o grafo.
        """
        n = len(self.matriz)
        graus = [sum(self.matriz[i]) for i in range(n)]
        conexoes = [(i, j) for i in range(n) for j in range(n) if self.matriz[i][j] != 0]

        return {
            "graus": graus,
            "total_arestas": sum(graus) // 2,
            "conexoes": conexoes,
        }

    def calcular_hub_autoridade(self, iteracoes=100, tol=1e-6):
        """
        Calcula os vetores de hub e autoridade usando o algoritmo HITS, sem bibliotecas externas.
        """
        
        n = len(self.matriz)

        # Inicializando os vetores
        autoridade = [1.0] * n
        hub = [1.0] * n

        matriz_transposta = self.calculo.transposta(self.matriz) #ERRO-------------------------

        for _ in range(iteracoes):
            # Calcula o novo vetor de autoridade
            nova_autoridade = self.calculo.multiplicacao(matriz_transposta, hub)
            # Calcula o novo vetor de hub
            nova_hub = self.calculo.multiplicacao(self.matriz, autoridade)

            # Normaliza os vetores
            nova_autoridade = self.calculo.normalizar_vetor(nova_autoridade)
            nova_hub = self.calculo.normalizar_vetor(nova_hub)

            # Verifica convergência
            
            autoridade, hub = nova_autoridade, nova_hub

        return autoridade, hub


    def ordenar_nos(self, vetor):
        """
        Ordena os nós com base nos valores de um vetor (ex: hub ou autoridade).
        Retorna uma lista de tuplas no formato (índice, valor), ordenada em ordem decrescente.
        """
        return sorted(
        [(i, float(v[0]) if isinstance(v, list) else float(v)) for i, v in enumerate(vetor)], 
        key=lambda x: x[1], 
        reverse=True
    )
