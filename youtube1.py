from pytube import YouTube


address = input('다운로드 받고 싶은 유튜브 동영상 주소 입력: ')

yt = YouTube(address)

print(yt.title)

print(yt.length)

print(yt.rating)

yt.streams.first().download()
