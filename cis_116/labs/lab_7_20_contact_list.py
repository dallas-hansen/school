pairs = input().split()
name = input()

numbers = [x.split(',') for x in pairs]

n = []
for x in pairs:
    n.append(x.split(','))

for i in n:
    if i[0] == name:
        print(i[1])
