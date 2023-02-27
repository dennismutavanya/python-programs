class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Current Balance:", self.balance)


# Example usage
my_account = BankAccount("123456", 1000, "2022-01-01", "John Doe")

deposit_amount = my_account.deposit(500)
print("Deposited amount:", deposit_amount)

my_account.check_balance()

withdraw_amount = my_account.withdraw(2000)
print("Withdrawn amount:", withdraw_amount)

withdraw_amount = my_account.withdraw(1000)
print("Withdrawn amount:", withdraw_amount)

my_account.check_balance()
my_account.customer_details()
