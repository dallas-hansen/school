from random import randint


class RandomNumbers:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0

    def set_random_values(self, low, high):
        self.var1, self.var2, self.var3 = self.get_random_values(low, high)

    def get_random_values(self):
        return random.randint()


def main():
    low = int(input())
    high = int(input())

    numbers = RandomNumbers()
    numbers.set_random_values(low, high)
    numbers.get_random_values()


if __name__ == "__main__":
    main()
