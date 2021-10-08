import random

class Matrix:
    data = []
    size: int

    def __init__(self, size):
        self.size = size        
        data = []
        for i in range(0,size):
            data.append(random.sample(range(0,1000), size))
        self.data = data

    def multiply_matrices(matrix1, matrix2):
        size = matrix1.size
        new_matrix = Matrix(size)
        for i in range(0, size): #rows
            for j in range(0, size): #columns
                res = 0
                for inner in range(0, size):
                    res += matrix1.data[i][inner] * matrix2.data[inner][j]
                new_matrix.data[i][j] = res
        return new_matrix

