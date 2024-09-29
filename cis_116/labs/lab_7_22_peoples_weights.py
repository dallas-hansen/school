w_list = []

# Loops 4 times asking for weights, then adds them to list w_list
for i in range(4):
    weight = (float(input(f'Enter weight {i + 1}:\n')))
    w_list.append(weight)

# Creates variables for average weight in list, and max weight in list.
avg = sum(w_list)/len(w_list)
highest = max(w_list)

print(f'Weights: {w_list}\n')
print(f'Average weight: {avg:.2f}')
print(f'Max weight: {highest:.2f}\n')

# Asks for a number to index list, then prints that index in lbs and kgs
list_location = int(input('Enter a list location (1 - 4):\n'))

lbs = w_list[list_location - 1]
kgs = w_list[list_location - 1] / 2.2

print(f'Weight in pounds: {lbs:.2f}')
print(f'Weight in kilograms: {kgs:.2f}\n')
print(f'Sorted list: {sorted(w_list)}')
