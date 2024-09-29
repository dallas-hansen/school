line1 = list(input().split())
line2 = list(input().split())

for i, word in enumerate(line1):
    if word != line2[i]:
        print(word, line2[i])
