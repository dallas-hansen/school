red = int(input())
green = int(input())
blue = int(input())

lowest = min(red, green, blue)

# remove lowest value
red -= lowest
green -= lowest
blue -= lowest

print(red, green, blue)