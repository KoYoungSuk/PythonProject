from gtts import gTTS
from tkinter import *

def btncmd():
    audioname = entry1.get()
    speechtext = entry2.get()
    label2.config(text = "Input Command: " + str(speechtext))
    language = 'en'
    try:
        sp = gTTS(lang=language, text=speechtext, slow=False)
        sp.save(audioname)
        label3.config(text = "Status: Success!")
    except Exception as e:
        label3.config(text = "Status: " + str(e))
def closecmd():
    quit()

root = Tk()
root.title("TTS GUI Test")
root.geometry("400x200")
root.resizable(False, False)

label1 = Label(root, text = "TTS GUI Test")
label1.pack()

audiolabel = Label(root, text="Audio File Name")
audiolabel.pack()

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.pack()

lyricslabel = Label(root, text="Lyrics")
lyricslabel.pack()

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.pack()

btn1 = Button(root, text="Generate", command=btncmd)
btn1.pack()

btn2 = Button(root, text="Close", command=closecmd)
btn2.pack()

label2 = Label(root, text = "Input Command: ")
label2.pack()

label3 = Label(root, text = "Status: ")
label3.pack()

root.mainloop()