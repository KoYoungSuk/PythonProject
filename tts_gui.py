from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def btncmd():
    audioname = entry1.get()
    speechtext = entry2.get()
    label2.config(text = "Input Command: " + str(speechtext))
    language = 'en'
    try:
        root = Tk().withdraw()
        title = 'Save TTS Audio File As...'
        ftypes = [("MP3 Files(*.mp3)", "*.mp3"), ("Windows Media Audio Files(*.wma)", "*.wma"), ("All Files(*.*)", "*.*")   ]
        audioname2 = filedialog.asksaveasfilename(filetypes=ftypes, title=title, initialfile=audioname)
        sp = gTTS(lang=language, text=speechtext, slow=False)
        sp.save(audioname2)
        label3.config(text = "Status: Success!")
        messagebox.showinfo("TTS", "Success!")
    except Exception as e:
        label3.config(text = "Status: Error!")
        messagebox.showerror("TTS", e)
def closecmd():
    sys.exit()

root = Tk()
root.title("TTS GUI Test")
root.geometry("400x200")
root.resizable(False, False)

label1 = Label(root, text = "TTS GUI Test")
label1.grid(row=0, column=0)

audiolabel = Label(root, text="Audio File Name")
audiolabel.grid(row=1, column=0)

entry1 = Entry(root, width=30, border=1, relief='solid')
entry1.grid(row=1, column=1)

lyricslabel = Label(root, text="Lyrics")
lyricslabel.grid(row=2, column=0)

entry2 = Entry(root, width=30, border=1, relief='solid')
entry2.grid(row=2, column=1)

btn1 = Button(root, text="Generate", command=btncmd)
btn1.grid(row=6, column=3)

btn2 = Button(root, text="Close", command=closecmd)
btn2.grid(row=7, column=3)

label2 = Label(root, text = "Input Command: ")
label2.grid(row=4, column=0)

label3 = Label(root, text = "Status: ")
label3.grid(row=5, column=0)

root.mainloop()