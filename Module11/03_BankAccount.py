class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit_money(self, amount):
        """Deposit money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw_money(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def show_balance(self):
        """Show account balance"""
        print(f"Account Balance: {self.balance}")

# Example usage
account = BankAccount("John Doe", 1000)
account.deposit_money(500)
account.withdraw_money(200)
account.show_balance()
account.withdraw_money(1500)
account.show_balance()