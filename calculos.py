from matriz import Matriz

class Calculos:
    def __init__(self, matriz1, matriz2):
        """Inicializa a classe com duas matrizes para operações."""
        self.matriz1 = matriz1
        self.matriz2 = matriz2

    def soma(self):
        """Soma duas matrizes e retorna o resultado."""
        if self.matriz1.linhas != self.matriz2.linhas or self.matriz1.colunas != self.matriz2.colunas:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                valor_soma = self.matriz1.get_valor(i, j) + self.matriz2.get_valor(i, j)
                matriz_resultante.set_valor(i, j, valor_soma)
        
        return matriz_resultante

    def multiplicacao(self):
        """Multiplica duas matrizes e retorna o resultado."""
        if self.matriz1.colunas != self.matriz2.linhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para multiplicação.")

        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz2.colunas)
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz2.colunas):
                valor_multiplicacao = 0
                for k in range(self.matriz1.colunas):
                    valor_multiplicacao += self.matriz1.get_valor(i, k) * self.matriz2.get_valor(k, j)
                matriz_resultante.set_valor(i, j, valor_multiplicacao)
        
        return matriz_resultante
