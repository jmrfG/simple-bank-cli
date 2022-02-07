from Connection import Connection
from Customer import Customer
from Register import Register
import os
import getpass

#INITIALIZE DATABASE HERE
HOST = ""
DB = ""



def main():
    
    TEXT = """
        ------ Please login into your account ------
    """
    print(TEXT)
    host = HOST
    db = DB
    user = input("Insert your username: ")          #User and password used in the database.
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

        5 - Transfer
        """
        print(TEXT)

        action = int(input("What will you do? "))
        
        if action == 1:
            createAccount(connection)
        
        elif action == 2:
            printCostumers(connection)

        elif action == 3:
            c = int(input("What's the customer's ID? "))
            val = float(input("How much would you like to deposit? "))
            Deposit(connection, c, val)
        
        elif action == 4:
            c = int(input("What's the customer's ID? "))
            val = float(input("How much would you like to withdraw? "))
            Withdraw(connection, c, val)

        elif action == 5:
            fromCustomer = int(input("Transfer from customer_ID: "))
            toCustomer = int(input("Transfer to customer_ID: "))
            val = float(input("How much would you like to transfer? "))
            Transfer(connection, fromCustomer, toCustomer, val)

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

def Deposit(connection,c,val):
    try:
        data = connection.pullData()
        for d in data:
            if d[0] == c:
                connection.updateData(d[3]+val,c)
    except:
        print("The operation has failed")
    

def Withdraw(connection, c, val):
    try:
        data = connection.pullData()
        for d in data:
            if d[0] == c:
                if d[3] - val > 0:
                    connection.updateData(d[3]-val,c)
                else:
                    return False
    except:
        print("Insuficient funds")
        

def Transfer(connection,fromC, toC, val):
    try:
        Withdraw(connection, fromC, val)
        if Withdraw(connection, fromC, val) is not False:
            Deposit(connection, toC, val)
            print(f"{val} transfered from {fromC} to {toC}")
    except:
        return "Invalid operation"


if __name__ == "__main__":

    main()
