from datetime import date
print("Bank Related Project\n")

class account:
    def __init__(self, name, account_num, account_bal):
        self.name = name
        self.account_num = account_num
        self.account_bal = account_bal

    def show_menu(self):
        print(f"{self.name}, Welcome to your Dashboard \nAvailable Balance = {self.account_bal}\n Date: {date.today()}\n")
        return "Done"

    @property
    def get_balance(self):
        print(f"Available Balance = {self.account_bal} \n")
        return "Done"

    def deposit(self, amount):
        self.account_bal += amount
        print(f"Deposit Successful \nCurrent Balance = {self.account_bal} \n")
        return "Done"

    def withdraw(self, amount):
        if amount > self.account_bal:
            return "Insufficient Funds"
        elif amount < self.account_bal:
            self.account_bal -= amount
            print(f"Withdrawal Successful \nCurrent balance = {self.account_bal} \n")
            return "Done"

    def transfer(self, account, amount):
        if amount > self.account_bal:
            return "Insufficient Funds"
        elif amount < self.account_bal:
            self.account_bal -= amount
            account.account_bal += amount
            print(f"Transferred {amount} to {account.name} Successfully\n")
            return "Done"

emmanuel = account("Emmanuel Joseph", "00000000000", 1000000)
david = account("David Abraham", "00000000001", 1000000)
print(emmanuel.get_balance)
print(emmanuel.transfer(david,30000))
print(emmanuel.get_balance)
print(david.get_balance)