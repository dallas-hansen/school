from kinematics import Kinematic
from conversions import Conversion
import numpy as np

a, b = Conversion.polar_to_cartesian(8, Conversion.degrees_to_radians(45))
c, d = Conversion.polar_to_cartesian(12, Conversion.degrees_to_radians(90))

matrix = np.array([
    [a, b],
    [c, d]
])

print(matrix.sum(axis=0) / (1 + 1.2))
