# $ pip install pytube

from pytube import YouTube

link = "https://youtube.com/shorts/HfQwuPnANmU?feature=share"
myYouTube = YouTube(link)

# print(myYouTube.title)
# print(myYouTube.thumbnail_url)

videos = myYouTube.streams.all()
# videos = myYouTube.streams.filter(only_audio=True) # For Audio Only
streamList = list(enumerate(videos))
for i in streamList:
    print(i)

print()
streaming = int(input("Enter: "))
videos[streaming].download()
print("Video Download Successfully!")

# ******For Playlist Download******

from pytube import Playlist

# py = Playlist("url:here")
# print(f'Downloading : {py.title}')
# for video in py.videos:
#     video.streams.first().download()