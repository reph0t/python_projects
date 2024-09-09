class BankAccount():

    def __init__(self, account, balance = 0):
        self.account = account
        self.balance = balance

    def bank_info(self):
        """Reads the Bank Information to the client"""
        print(f"Account: {self.account}")
        print(f"Current Balance: ${self.balance}")

    def make_deposit(self, amount):
        """Deposits money to the bank account """
        if amount > 0:
            self.balance += amount

    def make_withdraw(self,amount):
        """Withdraws money from the bank account"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount: .2f}")

        else:
            print("Canceled Request: Withdrawal exceeds the current balance.")

    def make_transfer(self,amount, other_account):
        """Making a transfer to another account"""
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred ${amount:.2f} to {other_account.account}")

        else:
            print("Canceled Request: Transfer over exceeds the current balance. ")

# Creating Instances
account1 = BankAccount("Account 1", 1_000)
account2 = BankAccount("Account 2", 4_000)

# Calling Methods
account1.bank_info()
account2.make_deposit(200)

account2.make_withdraw(500)

account1.make_transfer(500,account2)

