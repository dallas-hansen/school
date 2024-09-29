class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f'Inventory: {self.bottles} bottles')


def main():
    cafe = VendingMachine()
    cafe.purchase(int(input()))
    cafe.restock(int(input()))
    cafe.report()

# TODO: Create VendingMachine object
# TODO: Purchase input number of drinks
# TODO: Restock input number of bottles
# TODO: Report inventory


if __name__ == "__main__":
    main()
