import logging
import traceback


class BankException(Exception):
    pass

class BankAccount:
    def __init__(self, acct_name, balance):
        self.name = acct_name
        self.balance = balance
        print(f"Acount created for {self.name} and your balance is {self.balance} \n")

    def get_balance(self):
        print(f"{self.name} your account balance is {self.balance} \n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Completed \n")
        self.get_balance()

    def viable_transfer(self, amount):
        if self.balance >= amount:
            return
        
        else:
            raise BankException("Insufficient funds")
        
    def withdraw(self, amount):
        try:
            self.viable_transfer(amount)
            self.balance = self.balance - amount
            print("Withdrawal Complete")
            self.get_balance()

        except BankException as e:
            print(f"The process was interrupted, {e}")

    def transfer(self, amount, account):
        try:
            print("....Beginning Transfer 🚀........")
            self.viable_transfer(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer completed....✅")
        except BankException as e:
            # logging.debug(e, traceback.format_exc)
            # print("This is a %s ", format= traceback.format_exc)
            print(f"The process was interrupted, {e}")
            print("....Transfer failed ❌......")

Dave = BankAccount('Dave', 1000)
Sarah = BankAccount('Sarah', 1000)

Sarah.get_balance()

Sarah.transfer(2000, Dave)

            


