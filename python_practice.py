num1 = int(input())
num2 = 10.06
num3 = 5.66
num4 = 0

lowest = num1
if num2 < lowest:
    lowest = num2
if num3 < lowest:
    lowest = num3
if num4 < lowest:
    lowest = num4
print(lowest)