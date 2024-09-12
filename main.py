from matriz import preencher_matriz_com_input
from calculos import Calculos

def main():
    print("MATRIZ 1:---------------------")
    matriz1 = preencher_matriz_com_input()

    print("MATRIZ 2:---------------------")
    matriz2 = preencher_matriz_com_input()
    
    calc = Calculos(matriz1, matriz2)
    
    acao = input("Digite a ação: ")
    
    if (acao == '+'): #soma
        result = calc.soma()
        print(result)
    elif (acao == 'D'): # Multiplicação
        result = calc.multiplicacao()
        print(result)
        pass
    elif (acao == '*'):
        pass
    
    
    
main()
