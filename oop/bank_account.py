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

    def __sub__(self, amount):
        return self.withdraw(amount) # BanckAccount.withdraw(self, amount)
    def __getitem__(self, obj):
        print (obj)
        print (obj.step)
        print (obj.start)
        print (obj.stop)
        print("Slicing Method on Bank Account, but nothing to Slice")

c1 =  BankAccount("jeetendra",10000)
c2 =  BankAccount("bharat",10000)
c3 = BankAccount("Mahesh")
c1.deposit(10000)
c1 + 10000 # c1.__add__(10000)
print( c1.balance)
c1 - 5000
print (c1.balance)
c1[1:2:3] # c1.__getitem__(slice(1,2,3))
#del c1
print (c1.account_no, c2.account_no)
