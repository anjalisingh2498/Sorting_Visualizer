
import tkinter as Tkinter
from datetime import datetime
from tkinter import *
import time
# from playsound import playsound
from threading import *
from tkinter import messagebox
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('750x750')
ws.title('Sorting Visualizer')
ws['bg'] = 'white'

f = ("Times bold", 14)
Label(ws, text="Sorting Visualiser",
      background='white',
      foreground='dark slate gray',
      font=('Times 50 bold italic')).grid(column=1, row=0, sticky=N)

img = ImageTk.PhotoImage(Image.open("pic.jpg"))
label = Label(ws, image=img)
label.grid(column=1, row=1, sticky=W, pady=50)

frame = Frame(ws, bg='white')
frame.grid(column=1, row=1, sticky='W', padx=200)

counter = 66600
running = False

def nextPage1():
    ws.destroy()



def nextPage():

    import insertion

def prevPage():
    import pract



Button(
    ws,
    text="Bubble sort",
    font='Times',
    command=prevPage,
    background='cadet blue',
    foreground='white',
    height=2, width=9
).grid(column=0, row=2)

Button(
    ws,
    text="insertion sort",
    font='Times',
    command=nextPage,
    background='cadet blue',
    foreground='white',
    height=2, width=9
).grid(column=1, row=2)
Button(
    ws,
    text="close",
    font='Times',
    command=nextPage1,
    background='cadet blue',
    foreground='white',
    height=2, width=9
).grid(column=2, row=2)

ws.mainloop()