import random


def number_guess(num):
    x = random.randint(1, 101)
    if num > x:
        print(f'{num} is too high. Random number was {x}.')
    elif num < x:
        print(f'{num} is too low. Random number was {x}.')
    elif num == x:
        print(f'{num} is correct!')


def main():
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)


if __name__ == "__main__":
    main()
