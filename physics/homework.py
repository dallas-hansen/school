from kinematics import Kinematic
from projectiles import Projectile
from forces import Force

# angle = -10
# distance = Projectile.distance__no_air_resistance(.122, angle, 6)

# while distance < .5938:
#     angle += 1
#     distance = Projectile.distance__no_air_resistance(.122, angle, 6)

# print(f'Angle: {angle} degrees')

# distance = 3.26
# height = .122
# angle = 28.5
# initial_velocity = 5.639
# acceleration = 9.81

# Projectile.distance__no_air_resistance(.122, 28.5, 5.795)

M = [[300, 500],[-200, 0], [0, -800]]
s = Force.sum(M)
mag = Force.magnitude(s)
dir = Force.direction(s)
print(mag)
print(dir)