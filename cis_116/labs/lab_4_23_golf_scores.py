# input from user
par = int(input())
strokes = int(input())

# calculations
eagle = par - 2
birdie = par - 1
bogey = par + 1

# invalid
if par > 5 or par < 2:
    print('Error')
# valid
else:
    if strokes == eagle:
        print('Eagle')
    elif strokes == birdie:
        print('Birdie')
    elif strokes == par:
        print('Par')
    elif strokes == bogey:
        print('Bogey')
    else:
        print('Unknown')
        