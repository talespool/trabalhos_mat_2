class Matriz:
    def __init__(self, linhas, colunas, valor_inicial=0):
        # Inicializa a matriz com número de linhas e colunas especificados, preenchendo com valor_inicial
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = [[valor_inicial for _ in range(colunas)] for _ in range(linhas)]

    def __str__(self):
        # Retorna uma representação em string da matriz para fácil visualização
        return len(self.matriz)

    def set_valor(self, linha, coluna, valor):
        # Define o valor de um elemento específico na matriz
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            self.matriz[linha][coluna] = valor
        else:
            raise IndexError("Índice fora dos limites da matriz")

    def get_valor(self, linha, coluna):
        # Obtém o valor de um elemento específico da matriz
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            return self.matriz[linha][coluna]
        else:
            raise IndexError("Índice fora dos limites da matriz")

def criar_matriz_com_input():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    return [[0 for _ in range(colunas)] for _ in range(linhas)]


def preencher_matriz_com_input(matriz):
    print("\nPreenchendo a matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
            matriz[i][j] = valor
    return matriz



def alterar_valor_na_matriz(matriz):
    # Permite ao usuário escolher um valor para alterar na matriz
    print("\nEscolha um termo para ser alterado na matriz")
    l  = int(input("LINHA: "))
    c  = int(input("COLUNA: "))
    b = int(input("NOVO VALOR: "))
    l -= 1
    c  -= 1
    try:
        matriz.set_valor(l, c, b)
        print("Valor alterado com sucesso!")
    except IndexError as e:
        print(f"Erro: {e}")

# Função para pegar um valor da matriz
def pegar_valor(matriz):
    print("\nEscolha um termo para ser visualizado na matriz")
    l = int(input("LINHA: "))
    c = int(input("COLUNA: "))
    l -= 1
    c  -= 1
    try:
        valor = matriz.get_valor(l, c)
        print(f"VALOR: {valor}")
        return valor
    except IndexError as e:
        print(f"Erro: {e}")

# Função principal para executar o código
def main():
    matriz = criar_matriz_com_input()

    # Exibe a matriz inicial
    print("\nMATRIZ INICIAL")
    print(matriz)

    # Preenche a matriz com novos valores
    preencher_matriz_com_input(matriz)

    # Exibe a matriz atualizada
    print("\nMATRIZ ATUALIZADA")
    print(matriz)

    alterar_valor_na_matriz(matriz)

    print("\nMATRIZ ALTERADA")
    print(matriz)

    pegar_valor(matriz)

# Executa a função principal
if __name__ == "__main__":
    main()
