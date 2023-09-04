from pytube import YouTube

link = input("link: ")

yt = YouTube(link)


video = yt.streams.get_highest_resolution()

video.download()

print("done!")