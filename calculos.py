from typing import List
class Calculos:
    
    def __init__(self, matriz1: List[List[int]], matriz2:List[List[int]]):
        self.matriz1 = matriz1
        self.matriz2 = matriz2
    
    def __str__(self):
        # Retorna uma representação em string da matriz para fácil visualização
        return '\n'.join([' '.join(f"{elemento:4}" for elemento in linha) for linha in self.matriz])
    


    def mostrar_matriz(self, matriz: List[List[int]]) -> None:
        """Imprime a matriz formatada linha por linha"""
        for linha in matriz:
            print(' '.join(map(str, linha)))  # Converte os números da linha para strings e junta com espaços
        print()  # Quebra de linha adicional após a matriz

    def sum(self) -> List[List[int]]:
        
        matriz_resultante = [[0 for _ in range(self.matriz1.colunas)] for _ in range(self.matriz1.linhas)]

        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                matriz_resultante[i][j] = self.matriz1.matriz[i][j] + self.matriz2.matriz[i][j]

        return matriz_resultante
    
    def dot(self) -> List[List[int]]:
        """Multiplica a matriz atual por outra matriz."""
        
        # Verifica se a multiplicação é possível (colunas da primeira == linhas da segunda)
        if self.matriz1.colunas != self.matriz2.linhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")

        # Inicializa a matriz resultante com zeros
        # O tamanho da matriz resultante será (linhas da matriz1) x (colunas da matriz2)
        matriz_resultante = [[0 for _ in range(self.matriz2.colunas)] for _ in range(self.matriz1.linhas)]

        # Calcula o produto das matrizes
        for i in range(self.matriz1.linhas):  # Para cada linha da primeira matriz
            for j in range(self.matriz2.colunas):  # Para cada coluna da segunda matriz
                for k in range(self.matriz1.colunas):  # Faz o produto dos elementos da linha de A com os da coluna de B
                    matriz_resultante[i][j] += self.matriz1.matriz[i][k] * self.matriz2.matriz[k][j]

        # Retorna a matriz resultante
        return matriz_resultante
    
    def solve(self) -> List[List[float]]:
        """Resolve um sistema linear representado por uma matriz aumentada."""
        # Considera matriz1 como a matriz aumentada (n x n+1)
        n = len(self.matriz)
        m = len(self.matriz[0])

        matriz = [row[:] for row in self.matriz1]  # Cria uma cópia da matriz para evitar modificar a original

        # Aplicando eliminação de Gauss-Jordan
        for i in range(n):
            # Encontra a linha com o maior valor absoluto na coluna atual
            max_row = max(range(i, n), key=lambda r: abs(matriz[r][i]))
            if i != max_row:
                matriz[i], matriz[max_row] = matriz[max_row], matriz[i]

            pivot = matriz[i][i]
            if pivot == 0:
                print("O sistema não pode ser resolvido, pivot nulo.")

            # Divide a linha do pivô para tornar o elemento pivô igual a 1
            for j in range(i, m):
                matriz[i][j] /= pivot

            # Zera os elementos nas outras linhas abaixo e acima do pivô
            for k in range(n):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(i, m):
                        matriz[k][j] -= factor * matriz[i][j]

        # A matriz resultante é a solução (a última coluna contém os resultados)
        return matriz
