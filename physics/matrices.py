import numpy as np
import math

def matrix_sum(matrix) -> np.ndarray:
    return np.sum(matrix, axis=0)

def displacement(vector) -> float:
    return np.linalg.norm(vector)

def distance(matrix) -> float:
    return sum(np.linalg.norm(vector) for vector in matrix)

matrix = np.array([
    [0, 10, 50],
    [0, 10, 0]
])

variables = np.array([1, 2.0, 2.0])
position = matrix @ variables
print(f'Final position: {position}')

# disp = matrix_sum(matrix)
# print(f'displacement: {disp[0]}m')
# print(f'average velocity: {disp[0] / disp[1]} m/s')