from entity.Account import Account
from decimal import Decimal
from exception.overdraft_limit_exceeded_exception import OverDraftLimitExcededException

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = Decimal(1000.00)

    def __init__(self, account_number, balance):
        super().__init__(account_number, "current", balance)

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance()+amount)
            print(f"Deposited {amount:.2f}. New balance: {self.get_balance():.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if (amount % 500 == 0 or amount % 100 == 0):
                if (self.get_balance()+ self.OVERDRAFT_LIMIT >= amount):
                    self.set_balance(self.get_balance()- amount)
                    print(f"Withdrawn {amount:.2f}.")
                    if self.get_balance() < 0:
                        overdraft_used = abs(self.get_balance())
                        print(f"Overdraft used: {overdraft_used:.2f}")
                        print(f"Remaining overdraft limit: {self.OVERDRAFT_LIMIT - overdraft_used:.2f}")
                    return True
                else:
                    raise OverDraftLimitExcededException("Overdraft limit exceeded!")
            else:
                print("Enter amount in multiples of 500 or 100")
        else:
            print("Invalid withdraw amount")
        return False


