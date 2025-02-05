import math

class Conversion:
    @staticmethod
    def degrees_to_radians(degrees):
        return degrees * math.pi / 180
    
    @staticmethod
    def radians_to_degrees(radians):
        return radians * 180 / math.pi
    
    @staticmethod
    def cartesian_to_polar(x, y):
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return r, theta
    
    @staticmethod
    def polar_to_cartesian(magnitude, theta):
        x = magnitude * math.cos(theta)
        y = magnitude * math.sin(theta)
        return x, y