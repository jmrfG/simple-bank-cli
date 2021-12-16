from Connection import Connection
from Customer import Customer
from Register import Register
import os
import getpass


def main():
    TEXT = """
        ------ Please login into your account ------
    """
    print(TEXT)
    host = "localhost"
    db = "banky_boy"
    user = input("Insert your username: ")
    pwd = getpass.getpass("Insert your password: ")

    try:
        connection = Connection(host,db,user,pwd)
        os.system('cls' if os.name == 'nt' else 'clear')

        TEXT = """
        ------------- BANK -------------

        1 - Create Account

        2 - List Costumers

        3 - Deposit

        4 - Withdraw

        """
        print(TEXT)

        action = int(input("What will you do? "))
        
        if action == 1:
            createAccount(connection)
        
        elif action == 2:
            printCostumers(connection)

        elif action == 3:
            Deposit(connection)
        
        elif action == 4:
            Withdraw(connection)

    except:
        print("Wrong username or password")
        connection.endConnection()


def createAccount(connection):
    name = input("Insert the customer's name: ")
    age = int(input("Insert the customer's age: "))
    balance = float(input("Insert the customer's balance: "))
    acc_type = int(input("Insert the customer's account type: "))

    C = Customer(name,age,balance,acc_type)
    Registor = Register(C, connection)
    Registor.register()

def printCostumers(connection):
    data = connection.pullData()
    
    for d in data:
        T = f"""
        -----------------------
        ID: {d[0]}
        Name: {d[1]}
        Age: {d[2]}
        Balance: {d[3]} 
        -----------------------
        """
        print(T)

def Deposit(connection):
    try:
        c = int(input("What's the customer's ID? "))
        val = float(input("How much would you like to deposit? "))
        data = connection.pullData()

        for d in data:
            if d[0] == c:
                connection.updateData(d[3]+val,c)
    except:
        print("The operation has failed")
    

def Withdraw(connection):
    try:
        c = int(input("What's the customer's ID? "))
        val = float(input("How much would you like to withdraw? "))
        data = connection.pullData()

        for d in data:
            if d[0] == c:
                if d[3] - val > 0:
                    connection.updateData(d[3]-val,c)
                else:
                    print("Insuficient funds")
    except:
        return "The operation has failed"


if __name__ == "__main__":

    main()