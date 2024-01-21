class MoneyMachine:

    CURRENCY = "$"
# coffee machine is of usa lol
    COIN_VALUES = {
        "quarters": 0.20,
        "dimensions":0.10,
        "Nickles":0.05,
        "pennies":0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        # prints the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        # Returns the total calculated from coins inserted
        print("Please insert coins ")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f" How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        # Returns True when payment is accepted, or FAlse if Insufficient.
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that is not enough money. Money refunded")
            self.money_received = 0
            return False
