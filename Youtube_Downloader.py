# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:08:33 2023

@author: Favourrr
"""

#from tkinter import Tk, Label
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Favour's YT Downloader")

def download():
    Label(root, text='Download in progress...').place(x=125, y=200)
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='Video successfully downloaded').place(x=125, y=200)

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()
Label(root, text='Download YouTube videos here for free...').pack()
Label(root, text='Paste your video link here:', font='san-serif 15 italic').place(x=125, y=80)
link = StringVar()
Entry(root, width='40', textvariable=link).place(x=125, y=120)
Button(root, text='Download', font='arial 12 bold', padx=5, bg='green', command=download).place(x=200, y=150)
    
root.mainloop()