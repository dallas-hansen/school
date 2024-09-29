import math

num_of_people = int(input())
cost = 14.95
slices_per_person = 2
total_slices = 12
total_pizzas = math.ceil(num_of_people * slices_per_person / total_slices)


print(f'People: {num_of_people}')
print(f'Pizza(s): {total_pizzas}')
print(f'Cost for {total_pizzas} pizza(s): ${total_pizzas * cost:.2f}')