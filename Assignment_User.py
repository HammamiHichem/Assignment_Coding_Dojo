class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def make_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds. Your current balance is:", self.balance)
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successfully completed. Your new balance is:", self.balance)

# Example usage:
user_account = BankAccount("Hichem Hammami", 1000)
user_account.make_withdrawal(500)  # This will withdraw $500 from the account.

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def make_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds. Your current balance is:", self.balance)
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successfully completed. Your new balance is:", self.balance)

    def display_user_balance(self):
        print("User:", self.account_holder, "Balance: $" + str(self.balance))

# Example usage:
user_account = BankAccount("Guido van Rossum", 150)
user_account.display_user_balance()  # This will display "User: Guido van Rossum, Balance: $150"

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def make_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds. Your current balance is:", self.balance)
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successfully completed. Your new balance is:", self.balance)

    def display_user_balance(self):
        print("User:", self.account_holder, "Balance: $" + str(self.balance))

    def transfer_money(self, other_user, amount):
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds for the transfer. Your current balance is:", self.balance)
        else:
            self.balance -= amount
            other_user.balance += amount
            print("Transfer of $", amount, "to", other_user.account_holder, "successful.")
            self.display_user_balance()
            other_user.display_user_balance()

# Example usage:
user1 = BankAccount("Hichem", 1000)
user2 = BankAccount("Mourad", 500)

user1.transfer_money(user2, 300)


