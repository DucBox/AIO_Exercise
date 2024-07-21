import numpy as np

def compute_vector_length(vector):
  len_of_vector = np.linalg.norm(vector)
  return len_of_vector

vector = np.array([np.sqrt(3), 2, 3])
len_vector = compute_vector_length(vector)
print(len_vector)