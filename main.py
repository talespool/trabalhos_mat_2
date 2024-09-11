from matriz import criar_matriz_com_input, preencher_matriz_com_input
from teste import Calculos

#       SUM , DOT , SOLVE  [gauss]  
def main():
    print("MATRIZ 1:--------------")
    matriz11 = criar_matriz_com_input()
    matriz1 = preencher_matriz_com_input(matriz11)
    print("MATRIZ 2:--------------")
    matriz22 = criar_matriz_com_input()
    matriz2 = preencher_matriz_com_input(matriz22)
    
    calc = Calculos(matriz1, matriz2)
    
    acao = input("Digite a ação: ")
    
    if (acao == '+'): 
        result = calc.sum() # Soma  
        calc.mostrar_matriz(result)

    elif (acao == 'D'):
        result = calc.dot()  # Multiplicação 
        calc.mostrar_matriz(result)

        
    elif (acao == 'S'): # Resolver matriz ampliada (sistema linear)
        result = calc.resolver_sistema_linear()
        calc.resolver_sistema_linear(result)

    elif (acao == 'T'):
        result = calc.transposta()
        calc.transposta(result)
        pass
    
    
main()
