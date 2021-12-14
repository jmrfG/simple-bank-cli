class Customer:
    def __init__(self, name, age, income, acc_type) -> None:
        self.__name = name
        self.__age = age
        self.__income = income
        self.__acc_type = acc_type
        
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getIncome(self):
        return self.__income

    def getAccType(self):
        return self.__acc_type

    