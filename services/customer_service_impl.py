from services.customer_service import ICustomerServiceProvider
from dao.account_dao import AccountDAO
from dao.bank_dao import BankDAO
from exception.insufficient_funds_exception import InsufficientFundsException

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self, account_dao: AccountDAO, bank_dao: BankDAO):
        self.account_dao = account_dao
        self.bank_dao = bank_dao

    def get_account_balance(self, account_number: int) -> float:
        account = self.account_dao.get_account(account_number)
        return account.get_balance()

    def deposit(self, account_number: int, amount: float) -> float:
        account = self.account_dao.get_account(account_number)
        account.set_balance( account.get_balance() +amount)
        self.account_dao.update_account(account)
        return account.get_balance()

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.account_dao.get_account(account_number)
        if account.get_account_type().lower() == "savings" and (account.get_balance() - amount) < 500:
            raise InsufficientFundsException("Minimum balance requirement not met.")
        if account.get_balance() < amount:
            raise InsufficientFundsException("Insufficient funds.")
        account.set_balance(account.get_balance()- amount)
        self.account_dao.update_account(account)
        return account.get_balance()

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number: int) :
        account = self.account_dao.get_account_details(account_number)
        return account


