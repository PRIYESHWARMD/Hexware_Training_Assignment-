from services.customer_service_impl import CustomerServiceProviderImpl
from services.bank_service import IBankServiceProvider
from entity.Account import Account
from typing import List
from dao.bank_dao_impl import BankDAOImpl
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount
from dao.account_dao_impl import AccountDaoImpl


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.accountList: List[Account] = []
        self.branchName: str = branch_name
        self.branchAddress: str = branch_address
        self.dao = BankDAOImpl()
        self.account_service = AccountDaoImpl()

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
            account = SavingsAccount(account_number, account_type, balance, interest_rate, customer)
        else:
            account = CurrentAccount(account_number, account_type, balance, customer)

        self.dao.insert_account(account_number, customer.get_customer_id(), account_type, balance)
        return account_number

    def list_accounts(self) -> List[Account]:
        return self.accountList

    def calculate_interest(self,account_number):
        account = self.account_service.get_account(account_number)
        if account and account.get_account_type().lower() == "savings":
            interest = account.calculate_interest()
            account.deposit(interest)
            self.account_service.update_account(account)
            print("Interest added to account balance.")
        else:
            print("Interest applies only to savings accounts or account not found.")
