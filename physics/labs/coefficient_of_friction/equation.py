import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from kinematics import Kinematic
    
photogate_distance = .3 #float(input("Enter the distance between the two photogates (cm):\n"))
time = .83 #float(input("Enter the time on the photogate (s):\n"))
gravity = 9.81
mass_1 = 587 #float(input("Enter the mass of the first object (kg):\n"))
mass_2 = 351 #float(input("Enter the mass of the second object (kg):\n"))

acceleration = Kinematic.a__displacement_v0_t(photogate_distance, 0, time)
# acceleration = Kinematic.a__displacement_v0_t(photogate_distance, 0, time)
coefficient_of_friction = ((-mass_2 * acceleration) + (mass_2 * gravity) - (mass_1 * acceleration)) / (mass_1 * gravity)

friction_acceleration = ((coefficient_of_friction * mass_1 * gravity) - (mass_2 * gravity)) / (-mass_2 - mass_1)
new_time = Kinematic.t__displacement_v0_a(.34, 0, friction_acceleration)
                                          
print(f"The frictional acceleration is {friction_acceleration}")
print(f"The coefficient of friction is {coefficient_of_friction:.4f}")
print(f'The new time is {new_time:.4f}(s)')