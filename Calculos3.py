import numpy as np


class Calculos3:
    def __init__(self):
        pass

    def transposta(self, matriz):
        """Calcula a transposta de uma matriz."""
        linhas = len(matriz)
        colunas = len(matriz[0])
        matriz_transposta = [[matriz[j][i] for j in range(linhas)] for i in range(colunas)]
        return matriz_transposta

    def soma(self, matriz1, matriz2):
        """Calcula a soma de duas matrizes."""
        if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
            raise ValueError("As matrizes devem ter as mesmas dimensões para a soma.")
        matriz_soma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
        return matriz_soma

    def multiplicacao(self, matriz1, matriz2):
        """Calcula a multiplicação de duas matrizes ou entre matriz e vetor."""
        # Caso matriz2 seja unidimensional (vetor).
        if isinstance(matriz2[0], (int, float)):
            if len(matriz1[0]) != len(matriz2):
                raise ValueError("O número de colunas da matriz deve ser igual ao tamanho do vetor.")
            resultado = [[sum(matriz1[i][k] * matriz2[k] for k in range(len(matriz2)))] for i in range(len(matriz1))]
            return resultado

        # Caso matriz2 seja bidimensional.
        if len(matriz1[0]) != len(matriz2):
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        linhas = len(matriz1)
        colunas = len(matriz2[0])
        matriz_resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2))) for j in range(colunas)] for i in range(linhas)]
        return matriz_resultado

    def normalizar_vetor(self, vetor):
        """Normaliza um vetor para que seu comprimento seja igual a 1 usando numpy."""
        vetor = np.array(vetor)  # Converte a lista em um array numpy
        norma = np.linalg.norm(vetor)  # Calcula a norma do vetor
        if norma == 0:
            raise ValueError("Não é possível normalizar um vetor de norma zero.")
        vetor_normalizado = vetor / norma  # Divide o vetor pela norma
        return vetor_normalizado.tolist()
    
    #.....
    
    def dot(self):
        dot = int(input("Qual o valor: "))
        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)

        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                valor_multi = self.matriz1.get_valor(i, j) * dot
                matriz_resultante.set_valor(i, j, valor_multi)
        return matriz_resultante


    def gauss(self):
        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)
        # Copiar os valores da matriz original
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                matriz_resultante.set_valor(i, j, self.matriz1.get_valor(i, j))


        # Eliminação Gaussiana
        for i in range(self.matriz1.linhas):
            # Normaliza a linha atual pelo pivô
            pivo = matriz_resultante.get_valor(i, i)
            for j in range(i, self.matriz1.colunas):
                valor = matriz_resultante.get_valor(i, j) / pivo
                matriz_resultante.set_valor(i, j, valor)
            
            # Elimina os elementos abaixo da diagonal
            for k in range(i + 1, self.matriz1.linhas):
                fator = matriz_resultante.get_valor(k, i)
                for j in range(i, self.matriz1.colunas):
                   valor = matriz_resultante.get_valor(k, j) - matriz_resultante.get_valor(i, j) * fator
                   matriz_resultante.set_valor(k, j, round(valor, 2))

            return matriz_resultante

    def solve(self):
            """Resolve o sistema linear Ax = b usando a eliminação de Gauss e retorna o vetor solução."""
            n = self.matriz1.linhas
            matriz_resultante = Matriz(n, self.matriz1.colunas + 1)

            # Matriz aumentada A|b (anexa b à matriz A)
            for i in range(n):
                for j in range(self.matriz1.colunas):
                    matriz_resultante.set_valor(i, j, self.matriz1.get_valor(i, j))
                matriz_resultante.set_valor(i, n, self.matriz2.get_valor(i, 0))  # Coloca b como última coluna

            # Eliminação Gaussiana
            for i in range(n):
                # Normaliza o pivô
                pivo = matriz_resultante.get_valor(i, i)
                for j in range(i, n + 1):  # Inclui a última coluna (termos independentes)
                    valor = matriz_resultante.get_valor(i, j) / pivo
                    matriz_resultante.set_valor(i, j, valor)
                
                # Elimina os elementos abaixo da diagonal
                for k in range(i + 1, n):
                    fator = matriz_resultante.get_valor(k, i)
                    for j in range(i, n + 1):
                        valor = matriz_resultante.get_valor(k, j) - matriz_resultante.get_valor(i, j) * fator
                        matriz_resultante.set_valor(k, j, round(valor, 2))

            # Substituição retroativa
            x = [0 for _ in range(n)]
            for i in range(n - 1, -1, -1):
                x[i] = matriz_resultante.get_valor(i, n)
                for j in range(i + 1, n):
                    x[i] -= matriz_resultante.get_valor(i, j) * x[j]

            return matriz_resultante
