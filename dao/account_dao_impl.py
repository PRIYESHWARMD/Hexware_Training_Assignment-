import mysql.connector
from dao.account_dao import AccountDAO
from util.db_conn_util import DBConnection
from entity.Account import Account
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.invalid_account_exception import InvalidAccountException
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount


class AccountDaoImpl(AccountDAO):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def get_account(self, account_number: int):
        cursor = self.conn.cursor()

        try:


            sql = """
                SELECT account_id, account_type, balance
                FROM Accounts
                WHERE account_id = %s
            """
            cursor.execute(sql, (account_number,))
            row = cursor.fetchone()

            if not row:
                raise InvalidAccountException("Account does not exist!")

            account_number, acc_type, balance= row

            if acc_type.lower() == 'savings':
                interest_rate = 3.5
                try:
                    return SavingsAccount(account_number, balance, interest_rate)
                except ValueError as e:
                    raise InsufficientFundsException("Insufficient min balance for savings account.Couldn't perform withdrawal")

            if acc_type.lower() == 'current':
                return CurrentAccount(account_number, balance)

        except InvalidAccountException:
            print("Account does not exist!")

        except mysql.connector.Error as e:
            print(f"Database error: {e}")

        finally:
            cursor.close()
            self.conn.close()

    def update_account(self, account: Account):

        cursor = self.conn.cursor()
        try:


            sql = """
                UPDATE Accounts SET balance = %s WHERE account_id = %s
            """
            values = (account.get_balance(), account.get_account_number())
            cursor.execute(sql, values)

            if cursor.rowcount == 0:
                raise InvalidAccountException(" Account does not exist!")

            self.conn.commit()
            print("Account updated successfully!")

        except mysql.connector.Error as e:
            print(f" Database error: {e}")
        finally:
            cursor.close()
            self.conn.close()

    def deposit(self, account_number: int, amount: float):
        cursor = self.conn.cursor()
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive!")

            account = self.get_account(account_number)

            account.set_balance(account.get_balance()+amount)

            self.update_account(account)
            print(f"Successfully deposited {amount}. New balance: {account.get_balance()}")

        except InvalidAccountException as ex:
            print("Account does not exist!")

    def withdraw(self, account_number: int, amount: float):
        cursor = self.conn.cursor()
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive!")

            account = self.get_account(account_number)

            if amount > account.get_balance():
                raise InsufficientFundsException("Insufficient funds!")

            if amount>0 and (amount % 500 == 0 or amount % 100 == 0):
                account.set_balance(account.get_balance()-amount)
                self.update_account(account)
                print(f"Successfully withdrew {amount}. New balance: {account.get_balance}")

        except InvalidAccountException as ex:
            print("Account does not exist!")

    def get_account_details(self, account_number: int):
        cursor = self.conn.cursor()
        try:


            sql = """
                SELECT a.account_id, a.account_type, a.balance,
                       c.customer_id, c.first_name, c.last_name, c.dob, c.email, c.phone_number, c.address
                FROM Accounts a
                JOIN Customers c ON a.customer_id = c.customer_id
                WHERE a.account_id = %s
            """
            cursor.execute(sql, (account_number,))
            row = cursor.fetchone()

            if not row:
                print("Account does not exist!")
                return None

            (acc_no, acc_type, balance,
             cust_id, first_name, last_name, dob, email, phone, address) = row

            print("Account Details:")
            print(f"  Account ID : {acc_no}")
            print(f"  Account Type   : {acc_type}")
            print(f"  Balance        : {balance}")
            print("Customer Details:")
            print(f"  Customer ID    : {cust_id}")
            print(f"  Name           : {first_name} {last_name}")
            print(f"  DOB            : {dob}")
            print(f"  Email          : {email}")
            print(f"  Phone          : {phone}")
            print(f"  Address        : {address}")
            return {
                "account_id": acc_no,
                "account_type": acc_type,
                "balance": balance,
                "customer_id": cust_id,
                "first_name": first_name,
                "last_name": last_name,
                "dob": dob,
                "email": email,
                "phone": phone,
                "address": address
            }

        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            cursor.close()
            self.conn.close()

