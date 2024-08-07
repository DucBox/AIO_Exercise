import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([[1, 2], [3, 4], [5, 6]])

def mul_matrix_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

print(mul_matrix_vector(matrix, vector))