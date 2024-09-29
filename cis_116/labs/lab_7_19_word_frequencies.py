words = input().split()
lower_words = [x.lower() for x in words]

for i, index in enumerate(lower_words):
    print(words[index], lower_words.count(i))
