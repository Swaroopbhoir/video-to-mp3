import moviepy.editor as me
from tkinter import *
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filetypes = (
        ('video files', '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
filename=askopenfilename(filetypes=filetypes)
video=me.VideoFileClip(filename)
audio=video.audio
audio.write_audiofile("test/test.wav")