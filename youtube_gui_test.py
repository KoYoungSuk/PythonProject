from pytube import YouTube
from tkinter import *

def btncmd():
    yt = YouTube(entry1.get())
    print(yt.title)
    label2.config(text = "Title: " + yt.title)
    print(yt.length)
    label3.config(text = "Length: " + str(yt.length))
    print(yt.rating)
    label4.config(text = "Rating: " + str(yt.rating))
    Label6.config(text = "Author: " + str(yt.author))
    Label7.config(text = "Publish Date: " + str(yt.publish_date))
    Label8.config(text = "Description: " + str(yt.description))
    yt.streams.first().download()
    print("Success!")
    label5.config(text = "Success!")

def closecmd():
    quit()

root = Tk()
root.title("Python GUI YouTube Download(Test Only)")
root.geometry("520x500")
root.resizable(False, False)

label1 = Label(root, text="Python GUI YouTube Downloader")
label1.pack()

entrylabel = Label(root, text="Youtube Address")
entrylabel.pack()

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack()

entrylabel2 = Label(root, text="File Name")
entrylabel2.pack()

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.pack()

btn1 = Button(root, text="Download", command=btncmd)
btn1.pack()

btn2 = Button(root, text="Close", command=closecmd)
btn2.pack()

label2 = Label(root, text="Title: ")
label2.pack()

label3 = Label(root, text="Length: ")
label3.pack()

label4 = Label(root, text="Rating: ")
label4.pack()

Label6 = Label(root, text="Author: ")
Label6.pack()

Label7 = Label(root, text="Publish Date: ")
Label7.pack()

Label8 = Label(root, text="Description: ")
Label8.pack()

label5 = Label(root, text="")
label5.pack()

root.mainloop()

