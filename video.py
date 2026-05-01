import os
from yt_dlp import YoutubeDL

# url
playlist_url = 'https://youtube.com/playlist?list=PLJbAQ-AGdybNNRMavJk-_KjS6HmiOGhk2'

# yt-dlp 
ydl_opts = {
    'format': 'bestaudio[ext=webm]',  # webm format
    'outtmpl': '%(title)s.%(ext)s',  # filename with title
    'noplaylist': False,  # take all videos from playlist
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Here we GO !!!!")