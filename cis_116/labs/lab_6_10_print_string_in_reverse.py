ending = ['Done', 'done', 'd']
user_input = input()
# while user_input not in ending:
#     count = -1
#     for i in range(len(user_input)):
#         print(user_input[count], end='')
#         count -= 1
#     print()
#     user_input = input()

while user_input not in ending:
    result = ""
    for i in range(len(user_input)-1, -1, -1):
        result += user_input[i]
    print(result)
    user_input = input()

