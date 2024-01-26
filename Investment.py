#Romika Chaudhary
#C0921918
#Assignment 1
#Jan 25, 2024

from Account import Account

class Investment(Account):
    stockList = {
        'SHOP': [994.70, 'CAD'],
        'IBM': [129.87, 'USD'],
        'OTEX': [58.44, 'CAD'],
        'JD': [60.70, 'USD'],
        'MSFT': [196.84, 'USD']
    }

    def __init__(self, owner, currency='CAD', balance=0):
        super().__init__(owner, currency, balance)
        self.cash = 0
        self.stockHoldings = {ticker: 0 for ticker in self.stockList}

    def update_stock_price(self, ticker_symbol, value):
        if ticker_symbol in self.stockList and value >= 0:
            self.stockList[ticker_symbol][0] = value
            self.balance = self.calculate_balance()
        else:
            print("ERROR: Stock price could not be updated!")

    def buy(self, ticker_symbol, amt):
        if ticker_symbol in self.stockList and self.cash >= self.stockList[ticker_symbol][0] * amt and amt >= 0:
            self.stockHoldings[ticker_symbol] += amt
            self.cash -= self.stockList[ticker_symbol][0] * amt
            self.balance = self.calculate_balance()
        else:
            print("ERROR: Stock purchase could not be completed!")

    def sell(self, ticker_symbol, amt):
        if ticker_symbol in self.stockList and self.stockHoldings[ticker_symbol] >= amt and amt >= 0:
            self.stockHoldings[ticker_symbol] -= amt
            self.cash += self.stockList[ticker_symbol][0] * amt
            self.balance = self.calculate_balance()
        else:
            print("ERROR: Stock sale could not be completed!")

    def calculate_balance(self):
        return self.cash + sum(self.stockHoldings[ticker] * self.stockList[ticker][0] for ticker in self.stockList)

    def deposit(self, amount):
        if amount < 0:
            print("ERROR: Value for deposit is restricted to positive values")
        else:
            self.cash += amount
            self.balance = self.calculate_balance()

    def withdraw(self, amount):
        if amount < 0:
            print("ERROR: Value for withdraw is restricted to positive values")
        elif self.cash < amount:
            print("ERROR: Withdrawal amount exceeds available cash")
        else:
            self.cash -= amount
            self.balance = self.calculate_balance()

    def __str__(self):
        base_info = super().__str__()
        stock_info = "\nStock Holdings:"
        for ticker, amt in self.stockHoldings.items():
            stock_info += f"\n{ticker} - {amt} @ {self.stockList[ticker][1]}{self.stockList[ticker][0]:.2f} {self.stockList[ticker][1]}"
        return f"{base_info}{stock_info}"

