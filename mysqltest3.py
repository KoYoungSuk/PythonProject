import pymysql as mysql
import getpass
import pandas as pd

address = input('MySQL DataBase Address: ')
id = input("MySQL DataBase ID: ")
password = getpass.getpass("MySQL DataBase Password: ")
database = input("MySQL DataBase: ")

conn = mysql.connect(host=address, user=id, password=password, db=database)

sql = input("SQL: ")

cur = conn.cursor()

cur.execute(sql)

firstsql = sql.split()

if(firstsql[0] == 'select'):
    for row in cur:
        print(row)
    print("===============================================")
    #pd.read_sql(sql, con=conn)
    print(pd.read_sql(sql, con=conn))
else:
    print("Success!")


conn.commit()
conn.close()

print("===================================================")