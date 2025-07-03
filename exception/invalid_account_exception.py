class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number!"):
        super().__init__(message)
