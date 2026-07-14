class BankAccount:
    def __init__(self, account_number, accounty_name, balance):
        self.account_number = account_number # public
        self._accounty_name = accounty_name # protected
        self.__balance = balance # private
    
    def get_balance(self):
        return self.__balance
    
acc1 = BankAccount("ACC00001", "Anish", 1200000.00)
print(acc1.account_number)
print(acc1._accounty_name)
#print(acc1.__balance)
print(acc1.get_balance())