import math

class Kinematic:
    
    # Finding displacement
    @staticmethod
    def displacement__v0_a_t(v0, a, t):
        displacement = v0 * t + 0.5 * a * t**2
        # print(f'Displacement: {displacement} m')
        return displacement

    @staticmethod
    def displacement__v0_v_a(v0, v, a):
        displacement = (v**2 - v0**2) / (2 * a)
        # print(f'Displacement: {displacement} m')
        return displacement

    @staticmethod
    def displacement__v0_v_t(v0, v, t):
        displacement = ((v0 + v) / 2) * t
        # print(f'Displacement: {displacement} m')
        return displacement
    
    
    # Finding initial velocity
    @staticmethod
    def v0__v_a_t(v, a, t):
        initial_velocity = (v - a * t)
        # print(f'Initial velocity: {initial_velocity} m/s')
        return initial_velocity
    
    @staticmethod
    def v0__displacement_v_a(displacement, v, a):
        initial_velocity = math.sqrt(v**2 - 2 * a * displacement)
        # print(f'Initial velocity: {initial_velocity} m/s')
        return initial_velocity
    
    @staticmethod
    def v0__displacement_a_t(displacement, a, t):
        initial_velocity = (displacement - (0.5 * a * t**2)) / t
        # print(f'Initial velocity: {initial_velocity} m/s')
        return initial_velocity
    
    @staticmethod
    def v0__displacement_v_t(displacement, v, t):
        initial_velocity = (2 * displacement / t) - v
        # print(f'Initial velocity: {initial_velocity} m/s')
        return initial_velocity
    
    
    # Finding final velocity
    @staticmethod
    def v__displacement_v0_t(displacement, v0, t):
        final_velocity = (2 * displacement / t) - v0
        # print(f'Final velocity: {final_velocity} m/s')
        return final_velocity
    
    @staticmethod
    def v__v0_a_t(v0, a, t):
        final_velocity = v0 + a * t
        # print(f'Final velocity: {final_velocity} m/s')
        return final_velocity
    
    @staticmethod
    def v__displacement_v0_a(displacement, v0, a):
        final_velocity = math.sqrt(v0**2 + 2 * a * displacement)
        # print(f'Final velocity: {final_velocity} m/s')
        return final_velocity
    
    
    # Finding acceleration
    @staticmethod
    def a__v0_v_t(v0, v, t):
        acceleration = (v - v0) / t
        # print(f'Acceleration: {acceleration} m/s/s')
        return acceleration
    
    @staticmethod
    def a__displacement_v0_t(displacement, v0, t):
        acceleration = (2 * (displacement - v0 * t)) / t**2
        # print(f'Acceleration: {acceleration} m/s/s')
        return acceleration
    
    @staticmethod
    def a__displacement_v0_v(displacement, v0, v):
        acceleration = (v**2 - v0**2) / (2 * displacement)
        # print(f'Acceleration: {acceleration} m/s/s')
        return acceleration
    
    
    # Finding time
    @staticmethod
    def t__v0_v_a(v0, v, a):
        time = (v - v0) / a
        # print(f'Time: {time} s')
        return time
    
    @staticmethod
    def t__displacement_v0_v(displacement, v0, v):
        time = (2 * displacement) / (v + v0)
        # print(f'Time: {time} s')
        return time
    
    @staticmethod
    def t__displacement_v0_a(displacement, v0, a):
        if a == 0:
            return "Acceleration cannot be zero"
        
        discriminant_value = v0**2 + (2 * a * displacement)

        if discriminant_value < 0:
            return "No real solution"

        discriminant = math.sqrt(discriminant_value)
        
        pos = (-v0 + discriminant) / a
        neg = (-v0 - discriminant) / a
        # print(pos, neg)
        if pos > 0 and neg > 0:
            return max(pos, neg) - min(pos, neg)
            # print(f'Time: {max(pos, neg)-min(pos, neg)} s')
        elif pos > 0 or neg > 0:
            return max(pos, neg)
            # print(f'Time: {max(pos, neg)} s')
        else:
            return 0
            # print('No solution')

# Each is named in the order of the parameters. 
# In the example below v0 is unknown 
# displacement, v=final velocity, a=acceleration are the known parameters.
# Make sure you have them in the correct order
# Kinematic.v0__displacement_v_a(1.25, 0, -9.81)

print(Kinematic.t__displacement_v0_a(1.25, 0, 9.81))