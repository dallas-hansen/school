num = sorted(list(map(int, input().split())))

middle_num = num[len(num) // 2]

if len(num) > 9:
    print('Too many inputs')
else:
    print(f'Middle item: {middle_num}')


