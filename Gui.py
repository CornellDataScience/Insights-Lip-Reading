import tkinter
# from tkinter import tkk
from tkinter import *
from tkinter import filedialog
# from tkinter.tkk import *

# from tkinter import Tk, Label, Button, LEFT, RIGHT
import cv2

# import face_recognition
# import extract_lips as el

# TODO: rewrite the extract lips to not use face recognition, analyze if
# certain emotions tend to switch for each other


def load_file(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    #canvas = Canvas(gui)
    # canvas.pack()
    #img1 = PhotoImage(file=filename)
    #canvas.create_image(200, 150, image=img1)
    # call the model on it / the action we want

# rewrite extract_lips.py to not use face_recognition
# check if certain emotions often get switched from what they should be
def capture():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Failed to open webcam")
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5,
                           interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cap.release()
    # add in pressing the X button closes it
    cv2.destroyAllWindows()


def crop_lips():
    # execfile('extract_lips.py')
    load_file()
    # execfile(r'C:\test.py')
    # execute the extract_lips with the specific picture


gui = Tk()
gui.title('Lips / Face GUI')
gui.resizable(False, False)
# style = Style()
# style.configure('Buttons', font='calibri', foreground='blue')
# need to position the buttons
canvas = Canvas(gui)
canvas.pack()
img = PhotoImage(file="basic_emotions.png")
canvas.create_image(200, 150, image=img)

pixelVirtual = PhotoImage(width=1, height=1)
crop_lips_button = Button(gui, anchor=tkinter.CENTER, text="Crop Lips", foreground='blue', image=pixelVirtual,
                          width=50, height=30, compound="c", command=crop_lips)
# crop_lips_button.pack(padx=50)
crop_lips_button.place(x=50, y=300)
# crop_lips_button.pack(side=LEFT)

capture_button = Button(gui, anchor=tkinter.CENTER, text="Capture", foreground='purple', image=pixelVirtual,
                        width=50, height=30, compound="c", command=capture)

# capture_button.pack(padx=50)
capture_button.place(x=175, y=300)
# capture_button.pack()

load_file_button = Button(gui, anchor=tkinter.CENTER, text="Load File", foreground='red', image=pixelVirtual,
                          width=50, height=30, compound="c", command=load_file)
# load_file_button.pack(padx=50)
load_file_button.place(x=300, y=300)
# load_file_button.pack(side=RIGHT)

gui.geometry("400x400")
gui.mainloop()
