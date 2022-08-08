
from gtts import gTTS

audioname = input('INPUT AUDIO NAME: ')
speechtext = input('INPUT SPEECH TEXT: ')

language = 'en'

sp = gTTS(lang=language, text=speechtext, slow=False)

sp.save(audioname)
