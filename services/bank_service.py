from abc import ABC, abstractmethod
from entity.Customer import Customer
from typing import List

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, accNo: int, accType: str, balance: float) -> None:
        pass

    @abstractmethod
    def list_accounts(self) -> List:
        pass

    @abstractmethod
    def calculate_interest(self,account_number) -> None:
        pass
