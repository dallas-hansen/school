first_word = input()
second_word = input()

count = 0
# My code:

# if len(first_word) < len(second_word):
#     for letter in range(len(first_word)):
#         if first_word[letter] == second_word[letter]:
#             count += 1
# else:
#     for letter in range(len(second_word)):
#         if first_word[letter] == second_word[letter]:
#             count += 1
#
# if count > 1 or count == 0:
#     print(f'{count} characters match')
# else:
#     print(f'{count} character matches')


# Seng Lone's Code:

for char in range(min(len(second_word), len(first_word))):
    if first_word[char] == second_word[char]:
        count += 1
if count == 1:
    print(f'{count} character matches')
else:
    print(f'{count} characters match')
