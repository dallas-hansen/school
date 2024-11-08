class BankAccount:
    def __init__(self, new_name, ch_balance, s_balance):
        self.name = new_name
        self.checking_balance = ch_balance
        self.savings_balance = s_balance
    
    # TODO: Define checking_deposit()
    def checking_deposit(self, amount):
        if amount > 0:
            self.checking_balance += amount
    
    # TODO: Define savings_deposit()
    def savings_deposit(self, amount):
        if amount > 0:
            self.savings_balance += amount
    
    # TODO: Define checking_withdraw()
    def checking_withdraw(self, amount):
        if amount > 0:
            self.checking_balance -= amount
    
    # TODO: Define savings_withdraw()
    def savings_withdraw(self, amount):
        if amount > 0:
            self.savings_balance -= amount
    
    # TODO: Define transfer_to_checking()
    def transfer_to_checking(self, amount):
        if amount > 0:
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