
from pytube import YouTube

link = input("Enter Your YouTube Video Link :")
yt = YouTube(link)

Ttl = yt.title
print(Ttl)

streamlist = yt.streams.all()

i = 1

for stream in streamlist:
    print(str(i)+":  "+str(stream))
    i += 1

stream_number = int(input("Enter Your Stream Number"))


video = streamlist[stream_number - 1]
print("downloading please wait .................. ")
video.download()
print("downloaded")
