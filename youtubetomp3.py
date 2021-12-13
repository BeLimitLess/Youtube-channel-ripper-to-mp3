from pytube import YouTube
import os
file1 = open('link.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    yt = YouTube(str(line.strip()))
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='.')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
