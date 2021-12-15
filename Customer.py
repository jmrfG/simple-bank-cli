class Customer:
    def __init__(self, name, age, balance, acc_type):
        self.name = name
        self.age = age
        self.income = balance
        self.acc_type = acc_type
        
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccType(self):
        return self.acc_type

    def getCustomer(self):
        return (self.name, self.age, self.balance, self.acc_type)



