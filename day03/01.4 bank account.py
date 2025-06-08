class BankAccount:
    def __init__(self, initial_amount=0):
        self._balance = initial_amount

    def deposit(self, amount):
        if amount < 0:
            print("We cannot deposit negative amounts")
        else:
            self._balance += amount
    def withdraw(self, amount):
        if amount < 0:
            print("We cannot withdraw negative amounts")
        elif amount > self._balance:
            print("We cannot withdraw more than the balance")
        else:
            self._balance -= amount

    def print_balance(self):
        print(self._balance)

