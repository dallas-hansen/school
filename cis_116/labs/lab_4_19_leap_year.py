year = int(input())

if year % 100 == 0 and year % 400 != 0:
    print(f'{year} - not a leap year')
elif year % 400 == 0:
    print(f'{year} - leap year')
elif year % 100 != 0 and year % 4 == 0:
    print(f'{year} - leap year')
else:
    print(f'{year} - not a leap year')

