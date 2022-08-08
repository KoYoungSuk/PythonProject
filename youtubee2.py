from pytube import YouTube
import glob
import os.path


address = input('음악을 추출하고 싶은 유튜브 주소 입력: ')

yt = YouTube(address)

yt.streams.filter(only_audio=True).first().download()

