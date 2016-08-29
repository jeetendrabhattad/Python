class BankAccount:
    auto_account_no = 1# class attribute
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.account_no = BankAccount.auto_account_no
        BankAccount.auto_account_no = BankAccount.auto_account_no + 1
    def withdraw(self, amount):
        if self.balance < amount:
            return -1
        self.balance = self.balance - amount
        return self.balance
    def deposit(self, amount):
        self.balance =self.balance + amount

    def __add__(self, amount):
        self.balance += amount

c1 =  BankAccount("jeetendra",10000)
c2 =  BankAccount("bharat",10000)
c1.deposit(10000)
c1 + 10000
print c1.balance
#del c1
print c1.account_no, c2.account_no
