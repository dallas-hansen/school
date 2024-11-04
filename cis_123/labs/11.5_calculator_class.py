class Calculator:

    def __init__(self, calc_value=0.0):
        self.value = calc_value

    def get_value(self):
        return self.value

    def addition(self, num):
        self.value += num

    def multiplication(self, num):
        self.value *= num

    def subtraction(self, num):
        self.value -= num

    def division(self, num):
        self.value /= num

    def clear(self):
        self.value = 0

if __name__ == "__main__":

    calc = Calculator()
    num1 = float(input())
    num2 = float(input())

    # 1. The initial value
    print(f'{calc.get_value():.1f}')

    # 2. The The value after adding num1
    calc.addition(num1)
    print(f'{calc.get_value():.1f}')

    # 3. The value after multiplying by 3
    calc.multiplication(3)
    print(f'{calc.get_value():.1f}')

    # 4. The value after subtracting num2
    calc.subtraction(num2)
    print(f'{calc.get_value():.1f}')

    # 5. The value after dividing by 2
    calc.division(2)
    print(f'{calc.get_value():.1f}')

    # 6. The value after calling the clear() method
    calc.clear()
    print(f'{calc.get_value():.1f}')