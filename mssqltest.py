import pymssql as mssql
import getpass

address = input("Input Microsoft SQL DataBase Address: ")
id = input("Input Your Microsoft SQL DataBase ID: ")
password = getpass.getpass("Input Your Microsoft SQL DataBase Password: ")
database = input("Input Your Microsoft SQL DataBase DataBase: ")

conn = mssql.connect(server=address, username=id, password=password, database=database)
cur = conn.cursor()

sql = input("Input SQL Query:  ")
cur.execute(sql)


for row in cur:
    print(row)