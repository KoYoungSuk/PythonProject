import smtplib
from email.mime.text import MIMEText
import getpass
from tkinter import *
#from tkinter import filedialog
from tkinter import messagebox

def sendbtn():
    try:
        address = addressEntry.get()
        s = smtplib.SMTP(address, 587)
        s.ehlo()
        s.starttls()
        #id = input("Input Your Gmail Account: ")
        id = identry.get()
        pw = pwentry.get()
        s.login(id, pw) #Gmail App Password
        subject = subjectentry.get()
        message = text.get("1.0", "end")
        msg = MIMEText(message)
        msg['Subject'] = subject
        toemail = toEntry.get()
        forwardemail = forwardEntry.get()
        s.sendmail(forwardemail, toemail, msg.as_string())
        print("Success!")
        messagebox.showinfo("Python", "Success Transfered!")
        s.quit()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)

def closebtn():
    sys.exit()

root = Tk()
root.title("Python Mail Test Program GUI")
root.geometry("640x530")
root.resizable(True, True)

Label1 = Label(root, text="Python Mail Test Program GUI 2022-08-12")
Label1.grid(row=0, column=0)

addressLabel = Label(root, text="SMTP Address: ")
addressLabel.grid(row=1, column=0)

addressEntry = Entry(root, width=30, border=1, relief='solid')
addressEntry.grid(row=1, column=1)

idLabel = Label(root, text="ID: ")
idLabel.grid(row=2, column=0)

identry = Entry(root, width=30, border=1, relief='solid')
identry.grid(row=2, column=1)

pwLabel = Label(root, text="Password: ")
pwLabel.grid(row=3, column=0)

pwentry = Entry(root, show='*', width=30, border=1, relief='solid')
pwentry.grid(row=3, column=1)

forwardLabel = Label(root, text="Forward Email Address: ")
forwardLabel.grid(row=4, column=0)

forwardEntry = Entry(root, width=30, border=1, relief='solid')
forwardEntry.grid(row=4, column=1)

toLabel = Label(root, text="To Email Address: ")
toLabel.grid(row=5, column=0)

toEntry = Entry(root, width=30, border=1, relief='solid')
toEntry.grid(row=5, column=1)

subjectlabel = Label(root, text="Subject: ")
subjectlabel.grid(row=7, column=0)

subjectentry = Entry(root, width=30, border=1, relief='solid')
subjectentry.grid(row=7, column=1)

messageLabel = Label(root, text="Message: ")
messageLabel.grid(row=8, column=0)

text = Text(root)
text.configure()
text.place(x=50, y=180)

sendbutton = Button(root, text="Send", command=sendbtn)
sendbutton.grid(row=2, column=3)
closebutton = Button(root, text="Close", command=closebtn)
closebutton.grid(row=5, column=3)

root.mainloop()