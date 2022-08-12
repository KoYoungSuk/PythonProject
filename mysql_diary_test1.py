import smtplib
from email.mime.text import MIMEText
import getpass
from tkinter import *
#from tkinter import filedialog
from tkinter import messagebox
import pymysql as mysql

def writebtn():
    try:
        title = titleEntry.get()
        content = text.get("1.0", "end")
        id = "kys"
        pw = "pw" #censored
        conn = mysql.connect(host="koyoungsuk2.iptime.org", user=id, password=pw, db="diary")
        sql = "insert into diarytable values (%s, %s, NOW(), NOW())"
        vals = (title, content)
        cur = conn.cursor()
        cur.execute(sql, vals)
        print("Success!")
        messagebox.showinfo("PersonalDiary", "Success!")
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)

def closebtn():
    sys.exit()

root = Tk()
root.title("PersonalDiary Python Test 2022-08-12")
root.geometry("640x530")
root.resizable(True, True)

Label1 = Label(root, text="PersonalDiary Python Test 2022-08-12")
Label1.grid(row=0, column=0)

titleLabel = Label(root, text="Title: ")
titleLabel.grid(row=1, column=0)

titleEntry = Entry(root, width=30, border=1, relief='solid')
titleEntry.grid(row=1, column=1)

text = Text(root)
text.configure()
text.place(x=50, y=180)

writebutton = Button(root, text="Write", command=writebtn)
writebutton.grid(row=2, column=3)
closebutton = Button(root, text="Close", command=closebtn)
closebutton.grid(row=5, column=3)

root.mainloop()