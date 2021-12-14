from Connection import Connection


class Register:
    def __init__(self, customer, host, db, user, pwd) -> None:
        self.customer = customer
        self.connector = Connection(host,db,user,pwd)

    def register(self):
        try:
            self.connector.insert(self.customer)
        except:
            return "Impossible to register"

