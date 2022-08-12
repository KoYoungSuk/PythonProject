from tkinter import *
from tkinter import messagebox
import pymysql as mysql

def writebtn():
    try:
        name = nameentry.get()
        number = numberentry.get()
        address = "koyoungsuk2.iptime.org"
        id = "kys"
        password = "pw"; #censored
        database = "phonenumber"
        conn = mysql.connect(host=address, user=id, password=password, db=database)
        vals = (name, number)
        sql = "insert into phonenumbertable values (%s, %s, NOW())"
        cur = conn.cursor()
        cur.execute(sql, vals)
        conn.commit()
        conn.close()
        print("Success!")
        messagebox.showinfo("PhoneBook", "Success!")
    except Exception as e:
        print("Error Message: ", e)
        messagebox.showerror("PhoneBook", e)

def closebtn():
    sys.exit()


root = Tk()
root.title("PhoneBook Test")
root.geometry("400x400")
#root.resizable(False, False)

mainLabel = Label(root, text="PhoneBook 2022-08-12 Test")
mainLabel.grid(row=0, column=0)

nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=1, column=0)

nameentry = Entry(root, width=30, border=1, relief='solid')
nameentry.grid(row=1, column=1)

numberlabel = Label(root, text="Phone Number: ")
numberlabel.grid(row=2, column=0)

numberentry = Entry(root, width=30, border=1, relief='solid')
numberentry.grid(row=2, column=1)

WriteButton = Button(root, text="WRITE", command=writebtn)
WriteButton.grid(row=4, column=0)

CloseButton = Button(root, text="CLOSE", command=closebtn)
CloseButton.grid(row=4, column=1)

root.mainloop()