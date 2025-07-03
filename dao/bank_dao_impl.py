from util.db_conn_util import DBConnection
from dao.bank_dao import BankDAO

class BankDAOImpl(BankDAO):

    def __init__(self):
        self.conn = DBConnection.get_connection()

    def find_customer_by_phone_or_email(self, phone, email):
        cursor = self.conn.cursor()
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = "SELECT customer_id FROM customers WHERE phone_number = %s OR email = %s"
            cursor.execute(query, (phone, email))
            result = cursor.fetchone()
            return result[0] if result else None

        except Exception as e:
            print(f"Error occurred :{e}")
            return None

        finally:
            cursor.close()
            cursor.close()

    def insert_customer(self, first_name, last_name, dob, email, phone, address):

        cursor = self.conn.cursor()
        query = """INSERT INTO customers (first_name, last_name, dob, email, phone_number, address) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (first_name, last_name, dob, email, phone, address))
        cursor.commit()
        customer_id = cursor.lastrowid
        cursor.close()
        cursor.close()
        return customer_id

    def get_next_account_number(self):

        cursor = self.conn.cursor()
        query = "SELECT MAX(account_id) FROM accounts"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        cursor.close()
        return max(1001, result[0] + 1 if result[0] is not None else 1001)


    def insert_account(self, account_number, customer_id, account_type, balance):

        cursor = self.conn.cursor()
        query = """INSERT INTO accounts (account_id, customer_id, account_type, balance)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (account_number, customer_id, account_type, balance))
        cursor.commit()
        cursor.close()
        cursor.close()
