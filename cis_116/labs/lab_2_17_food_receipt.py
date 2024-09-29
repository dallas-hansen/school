def food_info():
    # takes input - appends to list - prints out receipt
    global total
    if total != 0:
        item = input('Enter next food item name:\n')
    else:
        item = input('Enter food item name:\n')
    price = float(input('Enter item price:\n'))
    quantity = int(input('Enter item quantity:\n'))

    food.append(item)
    how_many.append(quantity)
    cost.append(price)

    food_receipt()
    total += price * quantity
    print(f'Total cost: ${total:.2f}')


def food_receipt():
    # this does the receipt printing
    print(f'\nRECEIPT')
    for i in range(len(food)):
        sub_total = how_many[i] * cost[i]
        print(f'{how_many[i]} {food[i]} @ ${cost[i]:.2f} = ${sub_total:.2f}')


if __name__ == '__main__':
    # these lists keep track of the order over time
    food = []
    how_many = []
    cost = []
    tip = 15 / 100
    total = 0
    order = 'y'

    while order == 'y':
        food_info()
        print()
        print()
        order = input('Is there more? (y/n):\n')


    # food_info()  # calls function
    # print()  # these print statements are to format it with spaces
    # print()
    # food_info()  # calls function

    print(f'''
15% gratuity: ${total * tip:.2f}
Total with tip: ${total * (1 + tip):.2f}''')
