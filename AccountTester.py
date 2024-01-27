#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024

from Account import Account
from Chequing import Chequing
from Savings import Savings
from Investment import Investment


# Creating acccounts
account1 = Account("John Doe")
chequing1 = Chequing("Alice", fee=5, overdraftLimit=100)
savings1 = Savings("Bob", interestRate=2.5)
investment1 = Investment("Charlie")


#Printing info about account
print("Initial Account Information: ")
print(account1) 
print("\nInitial Chequing Account Information: ")
print(chequing1)  
print("\nInitial Savings Account Information: ")
print(savings1)  
print("\nInitial Investment Account Information: ")
print(investment1)  


# Deposit and withdraw Operations
account1.deposit(100)
account1.withdraw(50)

chequing1.deposit(200)
chequing1.withdraw(50)

savings1.deposit(2000)
savings1.withdraw(500)
savings1.applyInterest()

investment1.deposit(2000)
investment1.buy('IBM', 3)
investment1.sell('IBM', 2)
investment1.update_stock_price('SHOP', 1100)


#Print Updated account information
print("\nUpdated Account Information: ")
print(account1)  
print("\nUpdated Chequing Account Information: ")
print(chequing1) 
print("\nUpdated Savings Account Information: ")
print(savings1)  
print("\nUpdated Investment Account Information: ")
print(investment1)  