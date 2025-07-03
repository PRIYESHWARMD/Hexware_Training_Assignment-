from distutils.sysconfig import customize_compiler

from util.db_conn_util import DBConnection
from dao.transaction_dao import TransactionDAO

class TransactionDAOImpl(TransactionDAO):
    def __init__(self):
        self.conn = DBConnection.get_connection()
        cursor = self.conn.cursor()
    def transact(self, account_number, tran_type, amount):

        cursor = self.conn.cursor()

        sql = """
            INSERT INTO Transactions (account_id, transaction_type, amount)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (account_number, tran_type, amount))
        cursor.commit()

        cursor.close()
        cursor.close()

    def get_transactions(self, account_number):
        cursor = self.conn.cursor()
        sql = """
            SELECT transaction_type, amount, transaction_date
            FROM Transactions
            WHERE account_id = %s
            ORDER BY transaction_date ASC
        """
        cursor.execute(sql, (account_number,))
        transactions = cursor.fetchall()

        cursor.close()
        customize_compiler().close()
        return transactions
