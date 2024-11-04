class Product:

    def __init__(self, name, code, price, count):
        self.__name = name
        self.__code = code
        self.__price = price
        self.__count = count

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_price(self):
        return self.__price

    def get_count(self):
        return self.__count

    def set_name(self, name):
        self.__name = name

    def set_code(self, code):
        self.__code = code

    def set_price(self, price):
        self.__price = price

    def set_count(self, count):
        self.__count = count

    def add_inventory(self, num):
        self.__count += num

    def sell_inventory(self, num):
        self.__count -= num
    

if __name__ == "__main__":
    name = 'Apple'
    code = 'SKU234'
    price = 0.40
    num = 3
    p = Product(name, code, price, num)

    # Test 1 - Are instance attributes set/returned properly?
    print(f'Name: { p.get_name() }')
    print(f'Code: { p.get_code() }')
    print(f'Price: {p.get_price():.2f}')
    print(f'Count: { p.get_count() }')

    # Test 2 - Are attributes set/returned properly after adding and selling?
    num = 10
    p.add_inventory(num)
    num = 5
    p.sell_inventory(num)
    print(f'Name: { p.get_name() }')
    print(f'Code: { p.get_code() }')
    print(f'Price: {p.get_price():.2f}')
    print(f'Count: { p.get_count() }')

    # Test 3 - Do setters work properly?
    name = 'Golden Delicious'
    code = 'SKU555'
    p.set_name(name)
    p.set_code(code)
    price = 0.55
    p.set_price(price)
    num = 4
    p.set_count(num)
    print(f'Name: { p.get_name() }')
    print(f'Code: { p.get_code() }')
    print(f'Price: {p.get_price():.2f}')
    print(f'Count: { p.get_count() }')