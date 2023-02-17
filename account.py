class Account:
    def __init__(self, acct_name="", acct_num=0, balance=0.0, pin: str = ""):
        self.acct_name = acct_name
        self.acct_num = acct_num
        self.balance = balance
        self.pin = pin

    def get_account_num(self):
        return self.acct_num

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def get_account_balance(self):
        return self.balance

    def set_pin(self, pin):
        self.pin = pin

    def withdraw(self, amount: float):
        self.balance -= amount
        print(self.balance)
