class Matriz:
    def __init__(self, linhas, colunas):
        """Inicializa a matriz com número de linhas e colunas especificados, preenchendo com zeros."""
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    def __str__(self):
        """Retorna uma representação em string da matriz para fácil visualização."""
        return '\n'.join([' '.join(map(str, linha)) for linha in self.matriz])

    def set_valor(self, linha, coluna, valor):
        """Define o valor de um elemento específico na matriz."""
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            self.matriz[linha][coluna] = valor
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def get_valor(self, linha, coluna):
        """Obtém o valor de um elemento específico da matriz."""
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            return self.matriz[linha][coluna]
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def preencher_matriz_com_input(self):
        """Preenche a matriz com valores fornecidos pelo usuário."""
        print("Preenchendo a matriz:")
        for i in range(self.linhas):
            for j in range(self.colunas):
                valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
                self.set_valor(i, j, valor)

    def alterar_valor_na_matriz(self):
        """Permite ao usuário alterar o valor de uma célula específica da matriz."""
        print("Alterando valor na matriz:")
        linha = int(input("Digite o número da linha (começando de 1): ")) - 1
        coluna = int(input("Digite o número da coluna (começando de 1): ")) - 1
        novo_valor = int(input("Digite o novo valor: "))
        self.set_valor(linha, coluna, novo_valor)
        print("Valor alterado com sucesso!")

    def pegar_valor_na_matriz(self):
        """Permite ao usuário pegar o valor de uma célula específica da matriz."""
        linha = int(input("Digite o número da linha (começando de 1): ")) - 1
        coluna = int(input("Digite o número da coluna (começando de 1): ")) - 1
        valor = self.get_valor(linha, coluna)
        print(f"O valor na posição ({linha+1}, {coluna+1}) é: {valor}")



if __name__ == "__main__":
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    matriz = Matriz(linhas, colunas)

    # Preenchendo a matriz com valores do usuário
    matriz.preencher_matriz_com_input()

    # Exibindo a matriz
    print("\nMatriz preenchida:")
    print(matriz)

    # Alterando valor de uma célula
    matriz.alterar_valor_na_matriz()

    # Exibindo a matriz após alteração
    print("\nMatriz após alteração:")
    print(matriz)

    # Pegando valor de uma célula
    matriz.pegar_valor_na_matriz()
