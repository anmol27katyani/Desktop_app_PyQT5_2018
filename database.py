import sqlite3

def createTable():
    connection=sqlite3.connect("login1.db")
    connection.execute("CREATE TABLE USERS1(USERNAME TEXT NOT NULL,PASSWORD TEXT NOT NULL)")
    connection.execute("INSERT INTO USERS1 VALUES(?,?)",('9916103031','anmol1234'))
    connection.commit()
    
    result=connection.execute("SELECT * FROM USERS1")
    for data in result:
        print("Username: ", data[0])
        print("Password: ",data[1])
    connection.close()
createTable()
