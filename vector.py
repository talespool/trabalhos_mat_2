class Vetor:
    def __init__(self, dim):
        self.dim = dim  # Define a dimensão do vetor
        self.elements = []  # Inicializa uma lista vazia para os elementos

    def adicionar_elementos(self):
        for i in range(self.dim):
            elem = float(input(f"Digite o elemento {i + 1}: "))
            self.elements.append(elem)  # Adiciona cada elemento à lista

    def get(self, pos):
        if 0 <= pos < self.dim:  # Verifica se a posição é válida
            return self.elements[pos]
        else:
            print("Posição inválida!")
            return None

    def set(self, pos, valor):
        if 0 <= pos < self.dim:  # Verifica se a posição é válida
            self.elements[pos] = valor
        else:
            print("Posição inválida!")

    def exibir_vetor(self):
        print("\nElementos do vetor:")
        for elem in self.elements:
            print(elem, end="  ")
        print()

def main():
    # Solicita a dimensão do vetor
    dim = int(input("Digite a dimensão do vetor: "))

    # Cria um objeto da classe Vetor
    vetor = Vetor(dim)

    # Adiciona os elementos ao vetor
    vetor.adicionar_elementos()

    # Exibe o vetor
    vetor.exibir_vetor()

    # Modifica um elemento no vetor usando o método set
    pos = int(input("Posição que deseja alterar (1 a {}): ".format(dim )))
    pos -= 1
    valor = float(input("Novo valor: "))
    vetor.set(pos, valor)

    # Exibe o vetor novamente para mostrar a alteração
    vetor.exibir_vetor()

    # Exemplo de uso do método get
    pos = int(input("Posição do elemento que deseja visualizar (1 a {}): ".format(dim )))
    pos -= 1
    elemento = vetor.get(pos)
    if elemento is not None:
        print(f"Elemento na posição {pos}: {elemento}")

if __name__ == "__main__":
    main()
