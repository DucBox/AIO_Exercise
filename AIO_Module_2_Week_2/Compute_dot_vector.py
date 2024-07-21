import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

def compute_dot(vec1, vec2):
    return np.dot(vec1, vec2)

print(compute_dot(vector_a, vector_b))