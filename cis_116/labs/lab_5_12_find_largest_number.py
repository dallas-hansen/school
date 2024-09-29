num = int(input())
largest = num

while num >= 0:
    if num > largest:
        largest = num
    num = int(input())
print(largest)
