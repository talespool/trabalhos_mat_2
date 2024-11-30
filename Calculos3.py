from Matriz import Matriz

class Calculos:
    def __init__(self, matriz):
        self.matriz = matriz

    
    def dividir_matriz(self, matriz):
        # Linhas
        linhas = [linha for linha in matriz]
        
        # Colunas
        colunas = []
        for i in range(len(matriz[0])):
            coluna = [linha[i] for linha in matriz]
            colunas.append(coluna)
        
        return linhas, colunas
    
    def ler_matriz(self, matriz):
        linhas = len(matriz)  # Número de linhas
        colunas = len(matriz[0]) if linhas > 0 else 0  # Número de colunas (caso a matriz não esteja vazia)
        return linhas, colunas
    
    def soma(self, matriz1, matriz2):
        """
        Soma duas matrizes e retorna o resultado.
        As matrizes devem ser listas de listas com as mesmas dimensões.
        """
        # Obtém as dimensões das matrizes
        linhas1, colunas1 = self.dividir_matriz(matriz1)
        linhas2, colunas2 = self.dividir_matriz(matriz2)

        # Verifica se as dimensões são iguais
        if linhas1 != linhas2 or colunas1 != colunas2:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

        # Soma as matrizes elemento a elemento
        matriz_resultante = []
        for i in range(linhas1):
            linha_resultante = []
            for j in range(colunas1):
                valor_soma = matriz1[i][j] + matriz2[i][j]
                linha_resultante.append(round(valor_soma, 2))  # Arredonda o valor
            matriz_resultante.append(linha_resultante)

        return matriz_resultante

    def multiplicacao(matriz, vetor):
        # Verifica se o número de colunas da matriz é igual ao tamanho do vetor
        if len(matriz[0]) != len(vetor):
            raise ValueError("O número de colunas da matriz deve ser igual ao tamanho do vetor.")

        # Inicializa o vetor resultado com zeros
        resultado = [0] * len(matriz)

        # Realiza a multiplicação da matriz pelo vetor
        for i in range(len(matriz)):  # Percorre cada linha da matriz
            soma = 0
            for j in range(len(vetor)):  # Percorre cada coluna da linha
                soma += matriz[i][j] * vetor[j]  # Multiplica e soma os valores
            resultado[i] = soma  # Armazena o resultado no vetor

        return resultado
    
    
    
    def transpose(self, matriz):
        
        
        linhas, colunas = self.ler_matriz(matriz)
    
        matriz_transposta = Matriz(colunas, linhas) 
        
        for i in range(linhas):
            for j in range(colunas):
                
               
                    # Caso contrário, trata a matriz como uma lista simples
                valor = matriz[i][j]

            # Adiciona o valor transposto
            matriz_transposta = self.set_valor(j, i, valor) 
        return matriz_transposta
    
    
    
    def dot(matriz):
        dot = int(input("Qual o valor: "))
        matriz_resultante = Matriz(matriz.linhas, matriz.colunas)

        for i in range(matriz.linhas):
            for j in range(matriz.colunas):
                valor_multi = matriz.get_valor(i, j) * dot
                matriz_resultante.set_valor(i, j, valor_multi)
        return matriz_resultante


    def gauss(matriz):
        matriz_resultante = Matriz(matriz.linhas, matriz.colunas)
        # Copiar os valores da matriz original
        for i in range(matriz.linhas):
            for j in range(matriz.colunas):
                matriz_resultante.set_valor(i, j, matriz.get_valor(i, j))


        # Eliminação Gaussiana
        for i in range(matriz.linhas):
            # Normaliza a linha atual pelo pivô
            pivo = matriz_resultante.get_valor(i, i)
            for j in range(i, matriz.colunas):
                valor = matriz_resultante.get_valor(i, j) / pivo
                matriz_resultante.set_valor(i, j, valor)
            
            # Elimina os elementos abaixo da diagonal
            for k in range(i + 1, matriz.linhas):
                fator = matriz_resultante.get_valor(k, i)
                for j in range(i, matriz.colunas):
                   valor = matriz_resultante.get_valor(k, j) - matriz_resultante.get_valor(i, j) * fator
                   matriz_resultante.set_valor(k, j, round(valor, 2))

            return matriz_resultante

    def solve(matriz,matriz2):
            """Resolve o sistema linear Ax = b usando a eliminação de Gauss e retorna o vetor solução."""
            n = matriz.linhas
            matriz_resultante = Matriz(n, matriz.colunas + 1)

            # Matriz aumentada A|b (anexa b à matriz A)
            for i in range(n):
                for j in range(matriz.colunas):
                    matriz_resultante.set_valor(i, j, matriz.get_valor(i, j))
                matriz_resultante.set_valor(i, n, matriz2.get_valor(i, 0))  # Coloca b como última coluna

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
        
    def norma(vetor):
        """
        Calcula a norma L2 (norma euclidiana) de um vetor.
        """
        soma_quadrados = sum(x ** 2 for x in vetor)
        return soma_quadrados ** 0.5
    
    def normalizar_vetor(vetor):
        """
        Normaliza um vetor dividindo cada elemento pela sua norma.
        """
        norma = calcular_norma(vetor)
        if norma == 0:
            return vetor  # Evita divisão por zero
        return [x / norma for x in vetor]
    
    def set_valor(self , linha, coluna, valor):
        """Define o valor de um elemento específico na matriz."""
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            Matriz[linha][coluna] = valor
        else:
            raise IndexError("Índice fora dos limites da matriz.")
