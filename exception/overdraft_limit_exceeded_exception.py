class OverDraftLimitExcededException(Exception):
    def __init__(self, message="Overdraft limit exceeded for current account."):
        super().__init__(message)
