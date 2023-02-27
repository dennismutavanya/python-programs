import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount < 0:
            return "Invalid amount. Please enter a positive value."
        else:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid amount. Please enter a positive value."
        elif amount > self.balance:
            return "Insufficient funds. Please try a smaller amount."
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def customer_details(self):
        return f"Account number: {self.account_number}, Customer name: {self.customer_name}, Date of opening: {self.date_of_opening}"
account = BankAccount("1234567890", 1000, "John Doe")
print(account.deposit(500))
print(account.withdraw(200))
print(account.check_balance())
print(account.customer_details())
