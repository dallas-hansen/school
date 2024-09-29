def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost = (1 / miles_per_gallon) * dollars_per_gallon * miles_driven
    return cost


if __name__ == '__main__':
    mpg = float(input())
    dpg = float(input())
    miles = [10, 50, 400]
    for mile in miles:
        print(f'{driving_cost(mpg, dpg, mile):.2f}')
