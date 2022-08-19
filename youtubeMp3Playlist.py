from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
from tkinter import *
import time
import moviepy.editor as mp
import ffmpeg
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

root = Tk()
root.title('Youtube Downloader Playlist to MP3')
root.geometry("650x100")
root['bg']='#5d8a82'

mp4Folder = ''

e = Entry(root, width=300, borderwidth=3)
e.pack(pady=10, padx=20)

# Renaming
def convertToMp3():
    for file in os.listdir(mp4Folder):
        if re.search('mp4', file):
            file = mp4Folder + file
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            if not os.path.isfile(new_file):
                os.rename(file, new_file)
            print(base + " has been successfully downloaded.")

def convertToMp32():
    global mp4Folder
    for file in os.listdir(mp4Folder):
        if re.search('mp4', file):
            file = mp4Folder + file
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            ffmpeg_extract_audio(file, new_file)
            print(base + " has been successfully downloaded.")

def downloadPlaylist():
    playlist = Playlist(e.get())
    print("Downloading playlist \'",playlist.title,"\' with", playlist.length, 'videos')

    global mp4Folder
    mp4Folder = playlist.title + '/'
    os.makedirs(mp4Folder, exist_ok=True)

    for url in playlist:
        try:
            video = YouTube(url)
            video.streams.filter(only_audio=True).first().download(output_path=mp4Folder)
        except:
            print('Error downloading', video.title)

def executeApp():
    inicio = time.time()

    try:
        downloadPlaylist()
        convertToMp32()
    except Exception as e:
        print('There was an error:', e)
        raise

    print("Tiempo de descarga:", time.time()-inicio, "segundos")
            
open_button = Button(root, text='Download', command=executeApp)
open_button.pack(pady=5)

root.mainloop()
