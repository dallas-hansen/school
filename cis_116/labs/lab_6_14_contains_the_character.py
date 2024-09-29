character = input()
phrase = input()

words = phrase.split()

for i in words:
    if character in i:
        print(i, end=',')