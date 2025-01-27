import numpy as np
import math

test_matrix = np.array([
    [0, 40, 0], 
    [-20, 0, 0], 
    [60*math.cos(math.pi/4), 60*math.sin(math.pi/4), 0],
    [0, 50, 0]
])

def matrix_sum(matrix) -> np.ndarray:
    return np.sum(matrix, axis=0)

def displacement(vector) -> float:
    return np.linalg.norm(vector)

def distance(matrix) -> float:
    return sum(np.linalg.norm(vector) for vector in matrix)

total_displacement = displacement(matrix_sum(test_matrix))
total_distance = distance(test_matrix)

# print(f'Total displacement: {total_displacement}')
# print(f'Total distance: {total_distance}')
A = np.array([-19.2e3*math.cos(np.radians(25)), -19.2e3*math.sin(np.radians(25)), 800])
B = np.array([-17.6e3*math.cos(np.radians(20)), -17.6e3*math.sin(np.radians(20)), 1100])

M = A - B

print(displacement(A - B))