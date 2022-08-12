from tkinter import messagebox
from tkinter import *
import pymysql as mysql
import getpass
import pandas as pd

def connbtn():
    try:
        address = addressentry.get()
        id = identry.get()
        password = pwentry.get()
        database = dbentry.get()

        conn = mysql.connect(host=address, user=id, password=password, db=database)

        sql = sqlentry.get()

        cur = conn.cursor()

        cur.execute(sql)

        firstsql = sql.split()
        i = int(0)
        if (firstsql[0] == 'select'):
            messagebox.showinfo("Success!")
            for row in cur:
                i = int(0)
                for x in row:
                    i = i+1
                    print(i, ": ", x)
            print("===========================")
            print(pd.read_sql(sql, con=conn))
        else:
            messagebox.showinfo("Success!")
            print("Success!")

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)

def closebtn():
    sys.exit()

root = Tk()

root.title("MySQL Connection Python GUI")
root.geometry("700x400")


Label1 = Label(root, text="MySQL Connection Python GUI 2022-08-11")
Label1.grid(row=0, column=0)

addressLabel = Label(root, text="Address: ")
addressLabel.grid(row=2, column=0)

addressentry = Entry(root, width=30, border=1, relief='solid')
addressentry.grid(row=2, column=1)

idLabel = Label(root, text="ID: ")
idLabel.grid(row=3, column=0)

identry = Entry(root, width=30, border=1, relief='solid')
identry.grid(row=3, column=1)

pwLabel = Label(root, text="Password: ")
pwLabel.grid(row=4, column=0)

pwentry = Entry(root, show='*', width=30, border=1, relief='solid')
pwentry.grid(row=4, column=1)

dbLabel = Label(root, text="DataBase: ")
dbLabel.grid(row=5, column=0)

dbentry = Entry(root, width=30, border=1, relief='solid')
dbentry.grid(row=5, column=1)

sqlLabel = Label(root, text="SQL:  ")
sqlLabel.grid(row=6, column=0)

sqlentry = Entry(root, width=30, border=1, relief='solid')
sqlentry.grid(row=6, column=1)

connbutton = Button(root, text="Connect", command=connbtn);
connbutton.grid(row=7, column=3)

closebutton = Button(root, text="Close", command=closebtn)
closebutton.grid(row=7, column=4)

root.mainloop()