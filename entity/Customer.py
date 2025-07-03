import re

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, dob=None ,email=None, phone=None, address=None, password=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.set_email(email)
        self.set_phone(phone)
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__dob

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_dob(self, dob):
        self.__dob = dob

    def set_email(self, email):
        if email is not None and re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', email):
            self.__email = email
        else:
            raise ValueError("Invalid email address")

    def set_phone(self, phone):
        if phone is not None and re.match(r'^\d{10}$', phone):
            self.__phone = phone
        else:
            raise ValueError("Invalid phone number, must be 10 digits")

    def set_address(self, address):
        self.__address = address

    def print_customer_info(self):
        """Prints customer details except password for security reasons."""
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phone}")
        print(f"Address: {self.__address}")

