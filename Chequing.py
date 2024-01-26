#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024


from Account import Account

class Chequing(Account):
    def __init__(self, owner, fee, overdraftLimit, currency='CAD', balance = 0):
        super().__init__(owner, currency, balance)
        self.fee = fee
        self.overdraftLimit = overdraftLimit

        if currency not in self.conversion_rates:
            print("ERROR: Unsupported currency type")

        if overdraftLimit < 0:
            print("ERROR: Overdarft limit has been exceed")

    def withdraw(self, amount):
        if amount < 0:
            print("ERROR: Value for withdraw is restricted to positive values")
        else:
            total_withdraw = amount + self.fee
            if self.balance - total_withdraw < -self.overdraftLimit:
                print("ERROR: Overdraft limit has been exceeded")
            else:
                self.balance -= total_withdraw

    def set_fee(self, new_fee):
        self.fee = new_fee
    
    def get_fee(self):
        return self.fee
    
    def set_overdraft_limit(self, new_limit):
        if self.balance - new_limit < 0:
            print("ERROR: Overdraft limit will be exceeded. Update abandones!")
        else:
            self.overdraftLimit = new_limit

    def get_overdraft_limit(self):
        return self.overdraftLimit

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nfee: {self.conversion_rates[self.currency][1]}{self.fee:.2f}\nOverdraft Limit: {self.conversion_rates[self.currency][1]}{self.overdraftLimit:.2f}"