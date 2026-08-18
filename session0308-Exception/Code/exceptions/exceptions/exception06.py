class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Transaction failed! Tried to withdraw ₹{self.amount}, but only ₹{self.balance} available."

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    balance = 1000
    amount = int(input("Enter amount to withdraw: "))
    balance = withdraw(balance, amount)
    print(f"Withdrawal successful! Remaining balance: ₹{balance}")
except InsufficientFundsError as e:
    print(e)
