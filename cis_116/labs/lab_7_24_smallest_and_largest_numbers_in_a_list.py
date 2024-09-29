num = int(input())
tmp = []

while num > 0:
    tmp.append(num)
    num = int(input())

print(f'{min(tmp)} and {max(tmp)}')