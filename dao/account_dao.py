from abc import ABC, abstractmethod
from entity.Account import Account

class AccountDAO(ABC):

    @abstractmethod
    def get_account(self, account_number: int) -> Account:
        pass

    @abstractmethod
    def update_account(self, account: Account):
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float):
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float):
        pass
