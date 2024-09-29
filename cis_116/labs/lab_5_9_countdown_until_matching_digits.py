number = int(input())
if 11 > number > 100:
    print('Input must be 11-100')
else:
    while number % 11 != 0:
        print(number)
        number -= 1
    print(number)
