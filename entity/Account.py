from abc import abstractmethod

class Account:

    lastAccNo = 1000

    def __init__(self, account_number=None, account_type=None, balance=0.0,customer=None):
        Account.lastAccNo += 1
        self.__account_number = Account.lastAccNo
        self.__account_type = account_type
        self.__balance = balance
        self.__customer = customer

    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def get_customer(self):
        return self.__customer

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance

    def set_customer(self, customer):
        self.__customer = customer

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Balance: {self.__balance:.2f}")
        print("---- Customer Info ----")
        if self.__customer:
            self.__customer.print_customer_info()
        else:
            print("No customer associated with this account.")

    def print_balance(self):
        print(f"Balance: {self.__balance:.2f}")


