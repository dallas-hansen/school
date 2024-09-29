word1 = input()
word2 = input()
num1 = int(input())

pass1 = f'{word1}_{word2}'
pass2 = f'{num1}{word1}{num1}'

print(f'You entered: {word1} {word2} {num1}\n')

print(f'First password: {pass1}')
print(f'Second password: {pass2}\n')

print(f'Number of characters in {pass1}: {len(pass1)}')
print(f'Number of characters in {pass2}: {len(pass2)}')


