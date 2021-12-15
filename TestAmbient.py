from Connection import Connection

C = Connection("localhost", "banky_boy", "postgres", "asd151707")
data = C.pullData()

for d in data:
    T = f"""-----------------------
    Name: {d[1]}
    Age: {d[2]}
    Balance: {d[3]} 
    -----------------------
    """
    print(T)