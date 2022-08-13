from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
from tkinter import *
import time

root = Tk()
root.title('Youtube Downloader Playlist to MP3')
root.geometry("650x100")
root['bg']='#5d8a82'

e = Entry(root, width=300, borderwidth=3)
e.pack(pady=10, padx=20)

def downloadMp3():

    inicio = time.time()

    #playlist = Playlist('https://www.youtube.com/playlist?list=PLhMZ2YVd_kFv_9K5qU_cJqead4RnwJMLF')
    playlist = Playlist(e.get())
    print("Downloading playlist \'",playlist.title,"\' with", playlist.length, 'videos')

    #mp4Folder = './mp3/'
    mp4Folder = playlist.title + '/'
    os.makedirs(mp4Folder, exist_ok=True)

    #prints each video url, which is the same as iterating through playlist.video_urls
    #for url in playlist:
    #    print("URL:",url)
    #prints address of each YouTube object in the playlist
    #for vid in playlist.videos:
    #    print("Video:",vid)

    for url in playlist:
        try:
            video = YouTube(url)
            video.streams.filter(only_audio=True).first().download(output_path=mp4Folder)
        except:
            print('Error downloading', video.title)

    for file in os.listdir(mp4Folder):
        if re.search('mp4', file):
            file = mp4Folder + file
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            if not os.path.isfile(new_file):
                os.rename(file, new_file)
            print(base + " has been successfully downloaded.")
            
    print("Tiempo de descarga:", time.time()-inicio, "segundos")

open_button = Button(root, text='Download', command=downloadMp3)
open_button.pack(pady=5)

root.mainloop()
