class Number:
    def __init__(self):
        self.num = 0

    # TODO: define your __str__() instance method here
    
    def get_num(self):
        return self.num
        
    def set_num(self, num):
        self.num = num
    
if __name__ == "__main__":
    my_number = Number()
    my_number.set_num(int(input()))
    print(my_number)