from Connection import Connection


class Register:
    def __init__(self, customer, Connection) -> None:
        self.customer = customer
        self.connector = Connection

    def register(self):
        try:
            self.connector.insert(self.customer)
        except:
            return "Impossible to register"
        print("Successfully registerd")

