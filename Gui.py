import tkinter
from tkinter import *
from tkinter import Tk, Label, Button, LEFT, RIGHT


def capture():
    print("hello") #the webcam stuff
def crop_lips():
    #execfile('extract_lips.py')
    print("yes")
def load_file():
    print("yes")

gui = Tk()
gui.title('Lips / Face GUI')

#need to position the buttons

canvas = Canvas(gui, width = 100, height = 100)
canvas.pack()
img = PhotoImage(file="emotions.png")
canvas.create_image(20, 20, image=img)

crop_lips_button = Button(gui, text = "Crop Lips", command = crop_lips)
crop_lips_button.pack()

capture_button = Button(gui, text = "Capture", command=capture)
capture_button.pack(side = LEFT)

load_file_button = Button(gui, text = "Load File", command=load_file)
load_file_button.pack(side = RIGHT)

gui.geometry("400x400")
gui.mainloop()


