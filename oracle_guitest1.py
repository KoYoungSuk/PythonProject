import cx_Oracle
import pandas as pd
from tkinter import *
import os

def btncmd():
    location = entry0.get()
    address = entry1.get()
    id = entry2.get()
    password = entry3.get()
    sqlcommand = entry4.get()
    LOCATION = location

    try:
        os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]
        connect = cx_Oracle.connect(id, password, address)
        cursor = connect.cursor()
        cursor.execute(sqlcommand)
        df = pd.read_sql(sqlcommand, con=connect)
        text.insert(1.1, df)
        Label6.config(text="Status: success")
    except Exception as e:
        print(e)
        Label6.config(text="Status: " + str(e))
def closecmd():
    quit()

root = Tk()

root.title("Python GUI DataBase Tool(Test Only, Only For Oracle)")
root.geometry("700x600")
#root.resizable(False, False)

Label1 = Label(root, text="Python GUI DataBase Tool(Test Only, Only For Oracle)")
Label1.pack()

Label2 = Label(root, text="2022-08-09")
Label2.pack()

Label0 = Label(root, text="Oracle Instant Client Location: ")
Label0.pack()

entry0 = Entry(root, width=30, border=1, relief='solid')
entry0.pack()

Label3 = Label(root, text="Input DataBase Address, port and sid(F.E: koyoungsuk2.iptime.org:1521/xe")
Label3.pack()

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack()

Label4 = Label(root, text="ID")
Label4.pack()

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.pack()

Label5 = Label(root, text="Password")
Label5.pack()

entry3 = Entry(root, show='*', width=30, border=1, relief='solid')
entry3.pack()

Label7 = Label(root, text="SQL Command")
Label7.pack()

entry4 = Entry(root, width=30, border=1, relief='solid')
entry4.pack()

Label6 = Label(root, text="Status:  ")
Label6.pack()

Button1 = Button(root, text="Connect", command=btncmd)
Button1.pack()

Button2 = Button(root, text="Close", command=closecmd)
Button2.pack()

text = Text(root)
text.pack()

root.mainloop()