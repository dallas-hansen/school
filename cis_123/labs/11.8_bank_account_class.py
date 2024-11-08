# TODO: Define BankAccount class
class BankAccount:
    def __init__(self, name, checking_balance, savings_balance):
        self.name = name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
    
    def is_positive(self, amount):
        if amount > 0:
            return True
        else:
            return False        
        
    def checking_deposit(self, amount):
        if self.is_positive(amount):
            self.checking_balance += amount

    def savings_deposit(self, amount):
        if self.is_positive(amount):
            self.savings_balance += amount

    def checking_withdraw(self, amount):
        if self.is_positive(amount):
            self.checking_balance -= amount

    def savings_withdraw(self, amount):
        if self.is_positive(amount):
            self.savings_balance -= amount

    def transfer_to_checking(self, amount):
        if self.is_positive(amount):
            self.savings_balance -= amount
            self.checking_balance += amount

if __name__ == "__main__":
    account = BankAccount("Mickey", 500.00, 1000.00)
    account.savings_withdraw(100)
    account.checking_withdraw(100)
    account.transfer_to_checking(300)

    print(account.name)
    print(f'${account.checking_balance:.2f}')
    print(f'${account.savings_balance:.2f}')