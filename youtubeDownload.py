import yt_dlp

url = "https://www.youtube.com/watch?v=wWhkeU6GBNc"

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video download successfully!")
