num1 = int(input())
num2 = int(input())
num3 = int(input())

lowest_num = num1
if num2 < lowest_num:
    lowest_num = num2
if num3 < lowest_num:
    lowest_num = num3
print(lowest_num)