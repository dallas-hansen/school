triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

i = 0
while i <= triangle_height:
    print((triangle_char + ' ') * i)
    i += 1