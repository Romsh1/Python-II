#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024

from Account import Account
from Chequing import Chequing
from Savings import Savings
from Investment import Investment


# Create an account with default values
account1 = Account("John Doe")
print(account1)  # Should print information about the account

# Deposit and withdraw from the account
account1.deposit(100)
print(account1)  # Should print updated balance after deposit

account1.withdraw(50)
print(account1)  # Should print updated balance after withdrawal

# Change the currency of the account
account1.set_currency('EUR')
print(account1)  # Should print updated balance and currency

# Create another account and test equality
account2 = Account("Jane Doe", 'USD', 100)
print(account1 == account2)  # Should print False


# Create a chequing account
chequing1 = Chequing("Alice", fee=5, overdraftLimit=100)

# Test deposit and withdrawal specific to chequing account
chequing1.deposit(200)
print(chequing1)  # Should print updated balance with fee

chequing1.withdraw(50)
print(chequing1)  # Should print updated balance with fee and overdraft limit

# Set fee and overdraft limit
chequing1.set_fee(8)
chequing1.set_overdraft_limit(150)
print(chequing1)  # Should print updated fee and overdraft limit


# Create a savings account
savings1 = Savings("Bob", interestRate=2.5)

# Test deposit and apply interest
savings1.deposit(1000)
print(savings1)  # Should print updated balance

savings1.applyInterest()
print(savings1)  # Should print updated balance after applying interest

# Set and get interest rate
savings1.set_interest_rate(3.0)
print(savings1.get_interest_rate())  # Should print 3.0



# Create an investment account
investment1 = Investment("Charlie")

# Test buying and selling stocks
investment1.buy('SHOP', 5)
print(investment1)  

investment1.sell('SHOP', 2)
print(investment1)  

# Update stock price
investment1.update_stock_price('SHOP', 1100)
print(investment1)  

# Test deposit and withdrawal specific to investment account
investment1.deposit(2000)
print(investment1)  

investment1.withdraw(500)
print(investment1)  
