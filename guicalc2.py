from tkinter import *

def plusbutton():
    try:
       x = int(entry1.get())
       y = int(entry2.get())
       ResultLabel.config(text = "Result: " + str(x) + "+" + str(y) + "=" + str(x+y))
    except Exception as e:
       ResultLabel.config(text = "Result: " + str(e))
def minusbutton():
    try:
       x = int(entry1.get())
       y = int(entry2.get())
       ResultLabel.config(text="Result: " + str(x) + "-" + str(y) + "=" + str(x - y))
    except Exception as e:
       ResultLabel.config(text = "Result: " + str(e))
def multiplebutton():
    try:
       x = int(entry1.get())
       y = int(entry2.get())
       ResultLabel.config(text="Result: " + str(x) + "*" + str(y) + "=" + str(x*y))
    except Exception as e:
       ResultLabel.config(text = "Result: " + str(e))
def dividebutton():
    try:
       x = int(entry1.get())
       y = int(entry2.get())
       ResultLabel.config(text="Result: " + str(x) + "/" + str(y) + "=" + str(x/y))
    except Exception as e:
       ResultLabel.config(text = "Result: " + str(e))
def closebutton():
    quit()


root = Tk()

root.title("Python GUI Calculator (Test Program)")
root.geometry("500x300")
root.resizable(False, False)

Label1 = Label(root, text="Python GUI Calculator")
Label1.pack(side='top')

Label2 = Label(root, text="2022-08-09")
Label2.pack(side='top')


entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack(side='top')

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.pack(side='top')

ButtonLabel1 = Label(root, width=50, height=33)
ButtonLabel1.pack(side='left')
button1 = Button(ButtonLabel1, text="PLUS", command=plusbutton)
button1.pack(side='left')

ButtonLabel2 = Label(root, width=50, height=33)
ButtonLabel2.pack(side='left')
button2 = Button(ButtonLabel2, text="MINUS",command=minusbutton)
button2.pack(side='left')


ButtonLabel3 = Label(root, width=50, height=33)
ButtonLabel3.pack(side='left')
button3 = Button(ButtonLabel3, text="MULTIPLE", command=multiplebutton)
button3.pack(side='left')


ButtonLabel4 = Label(root, width=50, height=33)
ButtonLabel4.pack(side='left')
button4 = Button(ButtonLabel4, text="DIVISION", command=dividebutton)
button4.pack(side='left')

ButtonLabel5 = Label(root, width=50, height=33)
ButtonLabel5.pack(side='left')
button5 = Button(ButtonLabel5, text="CLOSE", command=closebutton)
button5.pack(side='left')

ResultLabel = Label(root, width=30, text="Result: ")
ResultLabel.pack(side='bottom')

root.mainloop()