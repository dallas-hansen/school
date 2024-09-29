text = input()
rm = [' ', '.', '!', ',']
i = 0
count = 0
while i < len(text):
    if text[i] not in rm:
        count += 1
    i += 1
print(count)


# Alternate way:

# user_text = 'Listen, Mr. Jones, calm down.'
#
# index = 0
# bad_char = 0
# while index < len(user_text):
#     if user_text[index] == ',':
#         bad_char += 1
#     elif user_text[index] == '.':
#         bad_char += 1
#     elif user_text[index] == '!':
#         bad_char += 1
#     elif user_text[index] == ' ':
#         bad_char += 1
#     index += 1
#
# print(len(user_text) - bad_char)
