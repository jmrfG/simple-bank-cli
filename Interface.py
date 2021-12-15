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

        3 - HOLDER
        """
        print(TEXT)

        action = int(input("What will you do? "))
        
        if action == 1:
            createAccount(connection)
        
        elif action == 2:
            printCostumers(connection)

    except:
        print("Wrong username or password")


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
        Name: {d[1]}
        Age: {d[2]}
        Balance: {d[3]} 
        -----------------------
        """
        print(T)

if __name__ == "__main__":
    main()