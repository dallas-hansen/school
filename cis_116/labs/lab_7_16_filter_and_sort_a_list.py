num = sorted(list(map(int, input().split())), reverse=True)

for i in num:
    if i < 0:
        print(i, end=' ')
    else:
        continue
