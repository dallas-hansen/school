import math
from conversions import Conversion

class Projectile:
    @staticmethod
    def distance__no_air_resistance(height, angle, initial_velocity, acceleration=9.81):
        """Determines the distance a projectile will travel without air resistance

        Args:
            v0 (float): Initial velocity
            height (float): Starting height
            angle (float, degrees): Will be converted to radians
            acceleration (float, optional): Defaults to 9.81.
        """
        angle = Conversion.degrees_to_radians(angle)
        velocity_x = initial_velocity * math.cos(angle)
        velocity_y = initial_velocity * math.sin(angle)
        
        discriminant = velocity_y**2 + (2 * acceleration * height)
        
        # Makes sure we're getting a real number
        if discriminant > 0:
            delta_t_add = (velocity_y + math.sqrt(discriminant)) / acceleration
            delta_t_min = (velocity_y - math.sqrt(discriminant)) / acceleration
            
            delta_t = max(delta_t_add, delta_t_min)
            delta_x = velocity_x * delta_t
            print(f'Split velocitys: {velocity_x} m/s, {velocity_y} m/s')
            print(f'Time = {delta_t} s')
            print(f'\u0394X = {delta_x:.4f} m')
            print(f'Min/Max: {delta_t_min:.4f} s, {delta_t_add:.4f} s')
            print(f'Discriminant: {discriminant:.4f}')
        else:
            print('No real solution')
        
        return delta_x
   
    
    @staticmethod
    def velocity__no_air_resistance(height, displacement, angle, acceleration=9.81):
        angle = Conversion.degrees_to_radians(angle)
        
        numerator = acceleration * (displacement ** 2)
        denominator = 2 * -math.cos(angle) ** 2 * (height - displacement * math.tan(angle))
        
        initial_velocity = math.sqrt(numerator / denominator)
        
        print(f'Initial velocity: {initial_velocity:.4f} m/s')
        return initial_velocity
    
Projectile.distance__no_air_resistance(.115, 28.5, 6)