red = int(input())
green = int(input())
blue = int(input())

if blue > red < green:
    green = green - red
    blue = blue - red
    red = 0

elif blue > green < red:
    red = red - green
    blue = blue - green
    green = 0

else:
    red = red - blue
    green = green - blue
    blue = 0

print(red, green, blue)