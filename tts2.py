
from gtts import gTTS
from playsound import playsound

audioname = input('INPUT AUDIO NAME: ')
speechtext = input('INPUT SPEECH TEXT: ')

language = 'en'

sp = gTTS(lang=language, text=speechtext, slow=False)

sp.save(audioname)
playsound(audioname)
