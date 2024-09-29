num_pizzas = int(input())
cost = 14.99
tax = .08

print(f'Pizzas: {num_pizzas}')
print(f'Subtotal: ${num_pizzas * cost:.2f}')
print(f'Total due: ${(num_pizzas * cost) * (1 + tax):.2f}')