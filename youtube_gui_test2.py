from tkinter import messagebox

from pytube import YouTube
from tkinter import *

def btncmd():
    try:
        yt = YouTube(entry1.get())
        print(yt.title)
        label2.config(text = "Title: " + yt.title)
        print(yt.length)
        label3.config(text = "Length: " + str(yt.length))
        print(yt.rating)
        label4.config(text = "Rating: " + str(yt.rating))
        Label6.config(text = "Author: " + str(yt.author))
        Label7.config(text = "Publish Date: " + str(yt.publish_date))
        #Label8.config(text = "Description: " + str(yt.description))
        yt.streams.first().download()
        print("Success!")
        messagebox.showinfo("Message", "Success!")
        label5.config(text = "Success!")
    except Exception as e:
        print(e)
        messagebox.showinfo("Message", e)
        label5.config(text = "Error")
def closecmd():
    quit()

root = Tk()
root.title("Python GUI YouTube Download(Test Only)")
root.geometry("520x500")
#root.resizable(False, False)

label1 = Label(root, text="Python GUI YouTube Downloader")
label1.grid(row=0, column=0)

entrylabel = Label(root, text="Youtube Address")
entrylabel.grid(row=1, column=0)

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.grid(row=1, column=1)

btn1 = Button(root, text="Download", command=btncmd)
btn1.grid(row=2, column=0)

btn2 = Button(root, text="Close", command=closecmd)
btn2.grid(row=2, column=1)

label2 = Label(root, text="Title: ")
label2.grid(row=3, column=0)

label3 = Label(root, text="Length: ")
label3.grid(row=4, column=0)

label4 = Label(root, text="Rating: ")
label4.grid(row=5, column=0)

Label6 = Label(root, text="Author: ")
Label6.grid(row=6, column=0)

Label7 = Label(root, text="Publish Date: ")
Label7.grid(row=7, column=0)

#Label8 = Label(root, text="Description: ")
#Label8.grid(row=8, column=0)

label5 = Label(root, text="")
label5.grid(row=12, column=0)

root.mainloop()

