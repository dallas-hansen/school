word = input()
password = ''

change = {'i': '1','a': '@','m': 'M','B': '8','s': '$'}
x = 0
while x < len(word):
    if word[x] in change:
        password += change[word[x]]
    else:
        password += word[x]
    x += 1
password += '!'
print(password)

# Below is how the professor did the problem

# word = input()
# password = ''
#
# index = 0
# while index < len(word):
#     if word[index] == 'i':
#         password += '1'
#     elif word[index] == 'a':
#         password += '@'
#     elif word[index] == 'm':
#         password += 'M'
#     elif word[index] == 'b':
#         password += '8'
#     elif word[index] == 's':
#         password += '$'
#     else:
#         password += word[index]
#     index += 1
# password += '!'
# print(password)
