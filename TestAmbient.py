from Connection import Connection

C = Connection("localhost", "banky_boy", "postgres", "asd151707")
data = C.pullData()
