from account import Account


class Bank:
    def __init__(self):
        self.accounts: list[Account] = []

    def create_account(self, acct_name: str, acct_num: int, balance: float = 0, pin: str = ""):
        act = Account(acct_name, acct_num, balance, pin)
        self.accounts.append(act)
        return act

    def num_account(self):
        return len(self.accounts)

    def search_account_by_number(self, account_number):
        for account in self.accounts:
            if account.get_account_num() == account_number:
                print("Account number exists")
                return account

    def deposit_money(self, account_number: int, amount: float):
        account = self.search_account_by_number(account_number)

        if account:
            account.deposit(amount)
            return account.get_account_balance()
        else:
            print(f"{account_number} does not exist")

    def withdraw_money(self, account_number: int, pin: str, amount: float):
        account = self.search_account_by_number(account_number)
        if account and account.get_account_balance() >= amount:
            account.set_pin(pin)
            account.withdraw(amount)
            return account.get_account_balance()
        else:
            return account.get_account_balance()
            print(f"{account_number} does not exist")

    def transfer_money(self, sender_account, recipient_account, amount, pin):
        account1 = self.search_account_by_number(sender_account)
        account2 = self.search_account_by_number(recipient_account)
        if account1 and account2:
            account1.withdraw(amount)
            account2.deposit(amount)
        else:
            print("invalid transfer")
