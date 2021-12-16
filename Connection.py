import psycopg2

### Might change its name
class Connection:
    def __init__(self, host, db, user, pwd):
        self._db = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pwd
        )

    def insert(self, customer):
        name, age, balance, acc_type = customer.getCustomer()
        try:
            cursor = self._db.cursor()
            sql_statement = f"""INSERT into customers values (default, '{name}',{age},{balance}, {acc_type})"""
            cursor.execute(sql_statement)
            self._db.commit()
        except:
            print("Error 69")
        

    def pullData(self):
        try:
            cursor = self._db.cursor()
            sql_statement = """select * from customers"""
            cursor.execute(sql_statement)
            data = cursor.fetchall()
        except:
            return "That's hot"
        return data

    def updateData(self, column, value, condition):
        try:
            cursor = self._db.cursor()
            sql_statement = f"""
            UPDATE consumers
            SET {column} = {value}
            WHERE ID = {condition};
            """
            cursor.execute(sql_statement)
            self._db.commit()
        except:
            return "Spider-man is cool"

    

    def endConnection(self):
        self._db.close()