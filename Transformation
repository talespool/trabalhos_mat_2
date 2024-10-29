from Matriz import Matriz
from Calculos import Calculos
import numpy as np

 

class Transformations:
    
    
    
    # Translação (2D e 3D)
    def translate2D(self, vetor, dx, dy):
        matrix = [[1, 0, dx],
                  [0, 1, dy],
                  [0, 0, 1]]
        homogeneous_vetor = [vetor[0], vetor[1], 1]
        result = Calculos.multiplicacao(matrix, homogeneous_vetor)
        return result[:2]  # Retorna para o sistema cartesiano 2D

    def translate3D(self, vetor, dx, dy, dz):
        matrix = [[1, 0, 0, dx],
                  [0, 1, 0, dy],
                  [0, 0, 1, dz],
                  [0, 0, 0, 1]]
        homogeneous_vetor = [vetor[0], vetor[1], vetor[2], 1]
        result = Calculos.multiplicacao(matrix, homogeneous_vetor)
        return result[:3]  # Retorna para o sistema cartesiano 3D

    # Rotação (2D e 3D)
    def rotation2D(self, vetor, angle):
        radians = np.radians(angle)
        matrix = [[np.cos(radians), -np.sin(radians)],
                  [np.sin(radians), np.cos(radians)]]
        return Calculos.multiplicacao(matrix, vetor)

    def rotation3DX(self, vetor, angle):
        radians = np.radians(angle)
        matrix = [[1, 0, 0],
                  [0, np.cos(radians), -np.sin(radians)],
                  [0, np.sin(radians), np.cos(radians)]]
        return Calculos.multiplicacao(matrix, vetor)

    def rotation3DY(self, vetor, angle):
        radians = np.radians(angle)
        matrix = [[np.cos(radians), 0, np.sin(radians)],
                  [0, 1, 0],
                  [-np.sin(radians), 0, np.cos(radians)]]
        return Calculos.multiplicacao(matrix, vetor)

    def rotation3DZ(self, vetor, angle):
        radians = np.radians(angle)
        matrix = [[np.cos(radians), -np.sin(radians), 0],
                  [np.sin(radians), np.cos(radians), 0],
                  [0, 0, 1]]
        return Calculos.multiplicacao(matrix, vetor)

    # Reflexão 
    def reflection2DX(self, vetor):
        matrix = [[1, 0], [0, -1]]
        return Calculos.multiplicacao(matrix, vetor)

    def reflection2DY(self, vetor):
        matrix = [[-1, 0], [0, 1]]
        return Calculos.multiplicacao(matrix, vetor)

    def reflection3DX(self, vetor):
        matrix = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
        return Calculos.multiplicacao(matrix, vetor)

    def reflection3DY(self, vetor):
        matrix = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
        return Calculos.multiplicacao(matrix, vetor)

    def reflection3DZ(self, vetor):
        matrix = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
        return Calculos.multiplicacao(matrix, vetor)

    # Projeção 
    def projection2DX(self, vetor):
        matrix = [[1, 0], [0, 0]]
        return Calculos.multiplicacao(matrix, vetor)

    def projection2DY(self, vetor):
        matrix = [[0, 0], [0, 1]]
        return Calculos.multiplicacao(matrix, vetor)

    def projection3DX(self, vetor):
        matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        return Calculos.multiplicacao(matrix, vetor)

    def projection3DY(self, vetor):
        matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        return Calculos.multiplicacao(matrix, vetor)

    def projection3DZ(self, vetor):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        return Calculos.multiplicacao(matrix, vetor)

    # Cisalhamento (Apenas 2D)
    def cisalhamentoX(self, vetor, kx):
        matrix = [[1, kx],
                  [0, 1]]
        return Calculos.multiplicacao(matrix, vetor)
    
    def cisalhamentoY(self, vetor, ky):
        matrix = [[1, 0],
                  [ky, 1]]
        return Calculos.multiplicacao(matrix, vetor)

