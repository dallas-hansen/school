def get_delta_x(delta_t, initial_velocity, final_velocity):
    delta_x = delta_t * (initial_velocity + final_velocity) / 2
    print(f'\u0394x = {delta_x}m')
    return delta_x

def get_delta_x(delta_t, initial_velocity, acceleration):
    delta_x = initial_velocity * delta_t + (acceleration * delta_t ** 2) / 2
    print(f'\u0394x = {delta_x}m')
    return delta_x

def get_delta_x(initial_velocity, final_velocity, acceleration):
    delta_x = (final_velocity ** 2 - initial_velocity ** 2) / (2 * acceleration)
    print(f'\u0394x = {delta_x}m')
    return delta_x



def get_delta_t(delta_x, initial_velocity, final_velocity):
    delta_t = delta_x / (initial_velocity + final_velocity)
    print(f'\u0394t = {delta_t}')
    return delta_t




def get_acceleration(delta_t, initial_velocity, final_velocity):
    acceleration = (final_velocity - initial_velocity) / delta_t
    print(f'Acceleration = {acceleration}')
    return acceleration


get_delta_x(delta_t=480, initial_velocity=4, acceleration=.05)