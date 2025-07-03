from abc import ABC, abstractmethod

class BankDAO(ABC):

    @abstractmethod
    def find_customer_by_phone_or_email(self, phone, email):
        pass

    @abstractmethod
    def insert_customer(self, first_name, last_name, dob, email, phone, address):
        pass

    @abstractmethod
    def get_next_account_number(self):
        pass

    @abstractmethod
    def insert_account(self, account_number, customer_id, account_type, balance):
        pass
