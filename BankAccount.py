class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print(cls):
        for account in cls.accounts:
            account.display_account_info()


Account1=BankAccount(.03,2000)
Account2=BankAccount(.02,4000)

Account1.deposit(1000).deposit(2000).deposit(2500).withdraw(500).yield_interest()
Account2.deposit(2000).deposit(1000).withdraw(500).withdraw(800).withdraw(1000).withdraw(100).yield_interest()

BankAccount.print()