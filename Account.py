#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024

class Account:
    conversion_rates = {
        'USD': [1.34607, '$'],
        'EUR' : [1.51746, '€'],
        'GBP': [1.70233, '£'],
        'CNY': [0.0189917, '¥'],
        'INR': [0.0178035, '₹'],
        'CAD': [1, '$']
    }    

    def __init__(self, owner, currency = 'CAD', balance = 0):
        self.owner = owner
        self.currency = currency
        self.balance = balance

        #Validation for currency
        if currency not in self.conversion_rates:
            print("ERROR: Unsupported currency type")

    def deposit(self, amount):
        if amount < 0:
            print("ERROR: Value for deposit is restricted to positive values")
        else:
            self.balance += amount 

    def withdraw(self, amount):
        if amount < 0:
            print("ERROR: Value for withdraw is restricted to positive values")
        else:
            self.balance -= amount

    def set_currency(self, new_currency):
        if new_currency not in self.conversion_rates:
            print("ERROR: Unsupported currency type")
        else:
            self.balance /= self.conversion_rates[self.currency][0]
            self.currency = new_currency
            self.balance *= self.conversion_rates[self.currency][0]

    def get_currency(self):
        return self.currency
    
    def __str__(self):
        return f"Owner: {self.owner}\nBalance : {self.conversion_rates[self.currency][1]}{self.balance:.2f}"

    def __eq__(self, other):
        return round(self.balance / self.conversion_rates[self.currency][0], 2) == \
                round(other.balance / self.conversion_rates[other.currency][0], 2)
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Account(self.owner, self.currency, self.balance + other.balance)
        else:
            print("ERROR: Cannot add accounts with different currencies")
            return None