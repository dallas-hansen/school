# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
from kinematics import Kinematic

    
photogate_distance = float(input("Enter the distance between the two photogates (cm):\n"))
time = float(input("Enter the time on the photogate (s):\n"))
gravity = 9.81
mass_1 = float(input("Enter the mass of the first object (kg):\n"))
mass_2 = float(input("Enter the mass of the second object (kg):\n"))

acceleration = Kinematic.a__displacement_v0_t(photogate_distance, 0, time)
coefficient_of_friction = ((-mass_1 * acceleration) + (mass_2 * gravity) - (mass_1 * acceleration)) / mass_1 * gravity

friction_acceleration = ((coefficient_of_friction * mass_1 * gravity) - (mass_2 * gravity)) / (-mass_2 - mass_1)

print(f"The frictional acceleration is {friction_acceleration}")
print(f"The coefficient of friction is {coefficient_of_friction}")