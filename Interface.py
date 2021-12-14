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

        2 - HOLDER

        3 - HOLDER
        """
        print(TEXT)

        action = int(input("What will you do? "))
        
        if action == 1:
            createAccount(connection)

    except:
        print("Wrong username or password")

def createAccount(connection):
    name = input("Insert the customer's name: ")
    age = int(input("Insert the customer's age: "))
    income = float(input("Insert the customer's income: "))
    acc_type = int(input("Insert the customer's account type: "))

    C = Customer(name,age,income,acc_type)
    Registor = Register(C, connection)
    Registor.register()



if __name__ == "__main__":
    main()