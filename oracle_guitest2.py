from tkinter import messagebox

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
        messagebox.showinfo("Message", "Success!")
    except Exception as e:
        print(e)
        Label6.config(text="Status: " + str(e))
        messagebox.showerror("Message", e)
def closecmd():
    sys.exit()

root = Tk()

root.title("Python GUI DataBase Tool(Test Only, Only For Oracle)")
root.geometry("720x560")
root.resizable(False, False)

Label1 = Label(root, text="Python GUI DataBase Tool(Test Only, Only For Oracle)")
Label1.grid(row=0, column=0)

Label2 = Label(root, text="2022-08-09")
Label2.grid(row=0, column=1)

Label0 = Label(root, text="Oracle Instant Client Location: ")
Label0.grid(row=2, column=0)

entry0 = Entry(root, width=30, border=1, relief='solid')
entry0.grid(row=2, column=1)

Label3 = Label(root, text="Input DataBase Address, port and sid(F.E: koyoungsuk2.iptime.org:1521/xe")
Label3.grid(row=3, column=0)

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.grid(row=3, column=1)

Label4 = Label(root, text="ID")
Label4.grid(row=4, column=0)

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.grid(row=4, column=1)

Label5 = Label(root, text="Password")
Label5.grid(row=5, column=0)

entry3 = Entry(root, show='*', width=30, border=1, relief='solid')
entry3.grid(row=5, column=1)

Label7 = Label(root, text="SQL Command")
Label7.grid(row=6, column=0)

entry4 = Entry(root, width=30, border=1, relief='solid')
entry4.grid(row=6, column=1)

Label6 = Label(root, text="Status:  ")
Label6.grid(row=11, column=0)

Button1 = Button(root, text="Connect", command=btncmd)
Button1.grid(row=10, column=0)

Button2 = Button(root, text="Close", command=closecmd)
Button2.grid(row=10, column=1)

text = Text(root)
text.configure(state='disabled')
text.place(x=80, y=200)

root.mainloop()