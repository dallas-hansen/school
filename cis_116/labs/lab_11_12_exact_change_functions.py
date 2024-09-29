def exact_change(user_total):
    num_quarters = user_total // 25
    num_dimes = user_total % 25 // 10
    num_nickels = user_total % 25 % 10 // 5
    num_pennies = user_total % 25 % 10 % 5
    return num_pennies, num_nickels, num_dimes, num_quarters


def print_values(input_val, change):
    if input_val == 0:
        print('no change')
        return
    for key, value in change.items():
        if value > 1 and key == 'penny':
            print(f'{value} pennies')
        elif value > 1:
            print(f'{value} {key}s')
        elif value == 1:
            print(f'{value} {key}')


def main():
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    change = {'penny': num_pennies,
              'nickel': num_nickels,
              'dime': num_dimes,
              'quarter': num_quarters
              }
    print_values(input_val, change)


if __name__ == '__main__':
    main()
