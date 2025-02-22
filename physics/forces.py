import numpy as np
from conversions import Conversion

class Force:
    @staticmethod
    def magnitude(vector):
        return np.linalg.norm(vector)
    
    @staticmethod
    def direction(vector):
        """
        Returns the direction of a 2D vector in degrees
        """
        return np.degrees(np.arctan2(vector[1], vector[0]))
    
    @staticmethod
    def dot_product(matrix1, matrix2):
        return np.dot(matrix1, matrix2)
    
    @staticmethod
    def cross_product(matrix1, matrix2):
        return np.cross(matrix1, matrix2)
    
    @staticmethod
    def sum(matrix):
        return np.sum(matrix, axis=0)