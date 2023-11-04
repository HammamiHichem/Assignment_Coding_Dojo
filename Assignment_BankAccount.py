class BankAccount:
    interest_rate = 0.02  # Example interest rate (2% per transaction)

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print("Deposit of $", amount, "successfully completed.")
            self.display_account_info()

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            self.display_account_info()
        else:
            self.balance -= amount
            print("Withdrawal of $", amount, "successfully completed.")
            self.display_account_info()

    def display_account_info(self):
        print("Account Holder:", self.account_holder)
        print("Balance: $", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.interest_rate
            self.balance += interest_earned
            print("Interest of $", interest_earned, "earned.")
            self.display_account_info()

# Example usage:
user_account = BankAccount("Alice", 1000)

user_account.deposit(200)
user_account.withdraw(300)
user_account.yield_interest()
