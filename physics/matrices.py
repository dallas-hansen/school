import numpy as np
import math

matrix = np.array([
    [3, -4, -2], 
    [-7, 4, 1], 
    [1, -7, 4]
])

A = matrix[0]
B = matrix[1]
C = matrix[2]

vector_sum = A + B + C
displacement = math.sqrt(vector_sum[0] ** 2 + vector_sum[1] ** 2 + vector_sum[2] ** 2)


print(f'Vector sum: {vector_sum}')
print(f'Displacement: {displacement}')