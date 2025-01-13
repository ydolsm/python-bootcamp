class BankAccount:

    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Invalid! Cannot withdraw negative amount PHP {amount:.2f}")

        if amount > self.balance:
            print(f"Cannot withdraw PHP {amount:.2f}. Account only has PHP {self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"Account withdrew PHP {amount:.2f}. (New Balance: PHP{self.balance:.2f})")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Invalid! Cannot deposit negative amount PHP {amount:.2f}")

        self.balance += amount
        print(f"Account deposited PHP {amount:.2f}. (New Balance: PHP{self.balance:.2f})")

    def print_balance(self):
        print(f"Current Balance: {self.balance}")