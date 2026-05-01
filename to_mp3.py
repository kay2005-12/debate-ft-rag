import os
import subprocess

files = os.listdir("videos")
# print(files) 

for file in files:
    title = file.split('.')[0]
    subprocess.run(["ffmpeg" , "-i",f"videos/{file}",f"audio/{title}.mp3"])
    

