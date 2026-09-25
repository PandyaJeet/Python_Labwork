class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("Current Balance:", self.balance)


def main():
    account = BankAccount(1000)
    print("Initial Balance:", account.balance)
    account.deposit(500)
    print("Deposit:", 500)
    account.withdraw(200)
    print("Withdraw:", 200)
    account.display_balance()


main()
