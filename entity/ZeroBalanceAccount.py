from entity.Account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number, "zero_balance", 0.0)

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: {amount:.2f}. New balance: {self.get_balance():.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() >= amount:
                self.set_balance(self.get_balance() - amount)
                print(f"Withdrawn: {amount:.2f}. Remaining balance: {self.get_balance():.2f}")
                return True
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdraw amount")
        return False
