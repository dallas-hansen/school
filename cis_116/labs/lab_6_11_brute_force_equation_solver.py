# Equation 1 Coefficients  (8x + 7y = 38)
a =int(input())
b =int(input())
c =int(input())

# Equation 2 Coefficients  (3x - 5y = -1)
d =int(input())
e =int(input())
f =int(input())

solution = False

# runs two loops, one for x -10 to 10 and then y -10 to 10
for x in range(-10, 11):
    for y in range(-10, 11):
        # checks if solution works for both equations
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(f'x = {x} , y = {y}')
            # sets bool to True
            solution = True
if solution is False:
    print('There is no solution')