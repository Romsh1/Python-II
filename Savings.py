#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024


from Account import Account

class Savings(Account):
    def __init__(self, owner, interestRate, currency = 'CAD', balance = 0):
        super().__init__(owner, currency, balance)
        self.rate = interestRate

        if currency not in self.conversion_rates:
            print("ERROR: Unsupported currency type")

    def applyInterest(self):
        monthly_interest = (self.balance * self.rate) / 100/ 12
        self.balance += monthly_interest

    def set_interest_rate(self, new_interest_rate):
        self.rate = new_interest_rate

    def get_interest_rate(self):
        return self.rate