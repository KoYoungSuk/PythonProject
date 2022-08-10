from tkinter import messagebox
import qrcode
from tkinter import *

def btncommand():
    try:
        img_url = entry2.get()
        filename = entry1.get()
        qr_gen = qrcode.make(img_url)
        qr_gen.save(filename)
        Label5.config(text = "Result: Success")
        messagebox.showinfo("Message", "Success!")
    except Exception as e:
        Label5.config(text = "Result: Failed")
        messagebox.showerror("Message", e)
def closecommand():
    quit()

root = Tk()
root.title("Python QR Code Generator v0.1")
root.resizable(False, False)
root.geometry("360x120")

Label1 = Label(root, text="Python QR Code Generator v0.1")
Label1.grid(row=0, column=2)

Label2 = Label(root, text="Image File name: ")
Label2.grid(row=1, column=1)

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.grid(row=1, column=2)

Label3 = Label(root, text="QR Code Address: ")
Label3.grid(row=2, column=1)

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.grid(row=2, column=2)

Button1 = Button(root, text="GENERATE", command=btncommand)
Button1.grid(row=3, column=1)

Button2 = Button(root, text="CLOSE", command=closecommand)
Button2.grid(row=3, column=2)

Label5 = Label(root, text="RESULT: ")
Label5.grid(row=4, column=1)

root.mainloop()