class NullPointerException(Exception):
    def __init__(self, message="Null value encountered."):
        super().__init__(message)
