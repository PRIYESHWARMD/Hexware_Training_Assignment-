from entity.Account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        if balance < 500:
            raise ValueError("Savings account have a minimum balance of ₹500.")
        super().__init__(account_number, "savings", balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance()+amount)
            print(f"Deposited {amount:.2f}. New balance: {self.get_balance():.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount % 500 == 0 or amount % 100 == 0:
                if self.get_balance() >= amount:
                    self.set_balance(self.get_balance() - amount)
                    print(f"Withdrawn {amount:.2f}. Remaining balance: {self.get_balance():.2f}")
                    return True
                else:
                    print("Insufficient funds!")
            else:
                print("Enter amount in multiples of 500 or 100")
        else:
            print("Invalid withdraw amount")
        return False

    def calculate_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        return interest
