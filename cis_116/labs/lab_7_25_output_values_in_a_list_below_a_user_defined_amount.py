quantity = int(input())
tmp = []

while len(tmp) != quantity:
    num = int(input())
    tmp.append(num)

threshold = int(input())

for i in tmp:
    if i <= threshold:
        print(i, end=',')