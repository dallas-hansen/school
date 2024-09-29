user_input = input()
character = user_input[0]
phrase = user_input[1:]


# Easy Way

# if phrase.count(character) == 1:
#     print(f'{phrase.count(character)} {character}')
# else:
#     print(f"{phrase.count(character)} {character}'s")

# With For Loops
count = 0
for i in phrase:
    if i == character:
        count += 1

if count == 1:
    print(f'{count} {character}')
else:
    print(f"{count} {character}'s")