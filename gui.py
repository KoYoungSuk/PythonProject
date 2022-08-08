from tkinter import *

def btncmd():
    print("Button is Clicked")
    label1.config(text = entry1.get())
    print(entry1.get())
    #root.config(text = "Button is Clicked")

    
root = Tk()
root.title("GUI TEST")
root.geometry("500x400")
root.resizable(False, False)

btn1 = Button(root, text="Button", command=btncmd)
btn1.pack()

label1 = Label(root, text="Text Label")
label1.pack()

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack()

root.mainloop()


