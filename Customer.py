class Customer:
    def __init__(self, name, age, income, acc_type):
        self.name = name
        self.age = age
        self.income = income
        self.acc_type = acc_type
        
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getIncome(self):
        return self.income

    def getAccType(self):
        return self.acc_type

    def getCustomer(self):
        return (self.name, self.age, self.income, self.acc_type)



