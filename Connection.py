import psycopg2

class Connection:
    def __init__(self, host, db, user, pwd):
        self._db = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pwd
        )

    def insert(self, customer):
        name, age, income = customer
        try:
            cursor = self._db.cursor()
            sql_statement = f"""INSERT into customers values (default, '{name}',{age},{income})"""
            cursor.execute(sql_statement)
            cursor.commit()
        except:
            return "Error 69"

    def pullData(self):
        try:
            cursor = self._db.cursor()
            sql_statement = """select * from customers"""
            cursor.execute(sql_statement)
            data = cursor.fetchall()
        except:
            return "That's hot"
        return data