num = int(input())

numbers = []
while num > 0:
    numbers.append(num)
    num = int(input())

print(f'{min(numbers)} and {max(numbers)}')



num = int(input())

smallest = num
largest = num

while num > 0:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    num = int(input())

print(f'{smallest} and {largest}')