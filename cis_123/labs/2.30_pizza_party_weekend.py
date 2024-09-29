import math

days = ['Friday', 'Saturday', 'Sunday']
sales_tax = .07
delivery_fee = .2
slices_per_pizza = 8
weekend_total = 0

for i in range(3):
    values = input().split()
    number_of_people = int(values[0])
    average_slices_per_person = float(values[1])
    cost_of_one_pizza = float(values[2])
    
    num_of_pizzas_needed = math.ceil(number_of_people * average_slices_per_person / slices_per_pizza)
    
    total_pizza_cost = num_of_pizzas_needed * cost_of_one_pizza
    delivery_cost = (total_pizza_cost * (sales_tax + 1)) * delivery_fee
    total = total_pizza_cost * (sales_tax + 1) * (1 + delivery_fee)
    
    print(f'{days[i]} Night Party')
    print(f'{num_of_pizzas_needed} Pizzas: ${num_of_pizzas_needed * cost_of_one_pizza:.2f}')
    print(f'Tax: ${total_pizza_cost * sales_tax:.2f}')
    print(f'Delivery: ${delivery_cost:.2f}')
    print(f'Total: ${total:.2f}')
    print()
    weekend_total += total

print(f'Weekend Total: ${weekend_total:.2f}')