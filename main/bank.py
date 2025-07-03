from dao.account_dao_impl import AccountDaoImpl
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.invalid_account_exception import InvalidAccountException
from dao.transaction_dao_impl import TransactionDAOImpl
from dao.bank_dao_impl import BankDAOImpl
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount
from entity.Customer import Customer


class Bank:
    def __init__(self):
        self.account_service = AccountDaoImpl()
        self.transaction_dao = TransactionDAOImpl()
        self.dao = BankDAOImpl()

    def is_valid_password(self,password,account_number):

        account = self.account_service.get_account(account_number)
        if account:
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                return False
            if not any(char.isupper() for char in password):
                print("Password must contain at least one uppercase letter.")
                return False
            if not any(char.isdigit() for char in password):
                print("Password must contain at least one digit.")
                return False
            return True
        else:
            print("Account not found!")
            return None

    def deposit(self, account_number, amount):

        account = self.account_service.get_account(account_number)
        if account:
            account.deposit(amount)
            self.account_service.update_account(account)
            self.transaction_dao.transact(account_number,'deposit',amount)  # Update DB
            print("Deposit successful!")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):

        try:
            account = self.account_service.get_account(account_number)
            if not account:
                print(f"Debug: Account {account_number} not found!")
                raise InvalidAccountException("Account does not exist!")

            if amount % 500 != 0 and amount % 100 != 0:
                print("Enter amount in multiples of 500 or 100!")
                return

            success = account.withdraw(amount)
            if success:
                self.account_service.update_account(account)
                self.transaction_dao.transact(account_number, 'withdrawal', amount)
                print("Withdrawal successful!")

        except InsufficientFundsException as e:
            print(e)

    def calculate_interest(self, account_number):

        account = self.account_service.get_account(account_number)
        if account and account.get_account_type().lower() == "savings":
            interest = account.calculate_interest()
            account.deposit(interest)  # Add interest to balance
            self.account_service.update_account(account)  # Update DB
            print("Interest added to account balance.")
        else:
            print("Interest applies only to savings accounts or account not found.")

    def check_loan_eligibility(self):

        try:
            credit_score = int(input("Enter your credit score: "))
            annual_income = float(input("Enter your annual income ($): "))

            if credit_score > 700 and annual_income >= 50000:
                print("Congratulations! You are eligible for a loan.")
            else:
                print("Sorry, you are not eligible for a loan.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    def calculate_compound_interest(self,initial_balance, annual_interest_rate, years):
        return initial_balance * (1 + annual_interest_rate / 100) ** years

    def print_account_details(self, account_number):
        account = self.account_service.get_account_details(account_number)

    def check_balance(self, account_number):
        account = self.account_service.get_account(account_number)
        if account:
            account.print_balance()
        else:
            raise InvalidAccountException("Account not found! Please enter a valid account number.")

    def show_transaction_history(self, account_number):
        transactions = self.transaction_dao.get_transactions(account_number)
        if not transactions:
            print("No transactions found.")
        else:
            print(f"\nTransaction History for Account {account_number} ")
            for tran_type, amount, tran_date in transactions:
                print(f"{tran_type.title()} | ₹{amount} | {tran_date} ")

    def find_or_create_customer(self, first_name, last_name, dob, email, phone, address):
        customer_id = self.dao.find_customer_by_phone_or_email(phone, email)
        if customer_id:
            print("Existing customer found.")
            try:
                customer = Customer(customer_id, first_name, last_name, dob, email, phone, address)
            except ValueError as e:
                print("Validation Error:", e)
                return None
            return customer
        else:
            try:
                customer = Customer(None, first_name, last_name, dob, email, phone, address)
            except ValueError as e:
                print("Validation Error:", e)
                return None
            return customer

    def create_account(self, customer, balance, account_type, interest_rate=None):
        if customer is None:
            print("Failed to create/find customer. Aborting account creation.")
            return None

        if customer.get_customer_id() is None:
            inserted_id = self.dao.insert_customer(
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_dob(),
                customer.get_email(),
                customer.get_phone(),
                customer.get_address()
            )
            if inserted_id:
                customer.set_customer_id(inserted_id)
                print("New customer inserted with ID:", inserted_id)
            else:
                print(" Failed to insert new customer into DB.")
                return None
        account_number = self.dao.get_next_account_number()

        if account_type == "Savings":
            account = SavingsAccount(account_number, balance,  interest_rate)
        else:
            account = CurrentAccount(account_number, balance)

        self.dao.insert_account(account_number, customer.get_customer_id(), account_type, balance)
        return account_number

    def transfer(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return False

        from_account = self.account_service.get_account(from_account_number)
        to_account = self.account_service.get_account(to_account_number)

        if not from_account or not to_account:
            print("One or both account numbers are invalid.")
            return False

        if from_account.get_balance() < amount:
            print("Insufficient balance in the source account.")
            return False

        from_account.set_balance(from_account.get_balance() - amount)
        to_account.set_balance(to_account.get_balance() + amount)

        self.account_service.update_account(from_account)
        self.account_service.update_account(to_account)

        print(f"{amount} transferred from Account {from_account_number} to Account {to_account_number}.")
        return True

