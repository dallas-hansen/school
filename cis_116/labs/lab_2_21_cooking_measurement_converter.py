def serving_multiplier(amount, conv=1):
    amount = amount / 6
    if conv == 1:
        container = 'cup(s)'
    else:
        container = 'gallon(s)'
    print(f'''
Lemonade ingredients - yields {amount * 6:.2f} servings
{(lemon_juice_cups * amount) / conv:.2f} {container} lemon juice
{(water_cups * amount) / conv:.2f} {container} water
{(agave_nectar_cups * amount) / conv:.2f} {container} agave nectar''')


if __name__ == '__main__':
    lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
    water_cups = float(input('Enter amount of water (in cups):\n'))
    agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
    servings = float(input('How many servings does this make?\n'))

    serving_multiplier(servings)
    print()
    serving_size = float(input('How many servings would you like to make?\n'))
    serving_multiplier(serving_size)
    serving_multiplier(serving_size, 16)

