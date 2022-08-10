from tkinter import *
from tkinter import messagebox

def buttoncommand():
    x = int(entry1.get())
    sum = (x * (x+1)) / 2
    Label2.config(text = "Result: 1부터 " + str(x) + "까지의 합은: " + str(sum))
    messagebox.showinfo("Message", "Result: 1부터 " + str(x) + "까지의 합은: " + str(sum))
def closecommand():
    quit()


root = Tk()
root.title("등차수열 프로그램(1부터 n까지의 합)")
root.resizable(False, False)
root.geometry("400x340")

Label1 = Label(root, text="등차수열 프로그램(1부터 n까지의 합")
Label1.pack()

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack()

button1 = Button(root, text="계산", command=buttoncommand)
button1.pack()

button2 = Button(root, text="닫기", command=closecommand)
button2.pack()

Label2 = Label(root, text="결과: ")
Label2.pack()

root.mainloop()