from random import randint

class RandomNumbers:
    def __init__(self):
        self.var1 = None
        self.var2 = None
        self.var3 = None
    
    def set_random_values(self, low, high):
        # Set var1, var2, and var3 to random values between low and high (inclusive)
        self.var1 = randint(low, high)
        self.var2 = randint(low, high)
        self.var3 = randint(low, high)
    
    def get_random_values(self):
        # Print the random values in the required format
        print(f"Random values: {self.var1} {self.var2} {self.var3}")

if __name__ == "__main__":
    low = int(input())
    high = int(input())

    numbers = RandomNumbers()
    numbers.set_random_values(low, high)
    numbers.get_random_values()