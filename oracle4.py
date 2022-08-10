import cx_Oracle
import os
import pandas as pd 
import warnings
import getpass 

warnings.filterwarnings('ignore')

location = input('INPUT YOUR ORACLE CLIENT LOCATION(FOR EXAMPLE: E:\oracleclient): ')

address = input('INPUT YOUR DATABASE ADDRESS(FOR EXAMPLE: koyoungsuk2.iptime.org:1521/xe) ')

id = input('INPUT YOUR DATABASE ID: ')

password = getpass.getpass('INPUT YOUR DATABASE PASSWORD: ')

print("Your DataBase Address: ", address)

print("Your DataBase ID: ", id)

sql = input("INPUT SQL QUERY: ")

#LOCATION= r"E:\oracleclient"

LOCATION=location

os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

connect = cx_Oracle.connect(id, password , address)

cursor = connect.cursor()

cursor.execute(sql)


df = pd.read_sql(sql, con = connect)

print(df)

txtfilename = input('SAVE AS TXT DOCUMENT: ')
df.to_csv(txtfilename, header=None, index=False, sep='\t')