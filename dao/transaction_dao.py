from abc import ABC, abstractmethod

class TransactionDAO(ABC):

    @abstractmethod
    def transact(self, account_number: int, tran_type: str, amount: float):
        pass

    @abstractmethod
    def get_transactions(self, account_number: int):
        pass