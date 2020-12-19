import tkinter
# from tkinter import tkk
from tkinter import *
from tkinter import filedialog
# from tkinter.tkk import *

# from tkinter import Tk, Label, Button, LEFT, RIGHT
import cv2

gui = Tk()
gui.title('Insights-README GUI(')
gui.resizable(False, False)


def introduction():
    intro_text = "The current project, entitled Insights-ReadME was designed to produce a real-time end to end lip reading system, one that relies solely on visual information to produce a textual output representative of speech utterances. Although proving too large in scope to be implemented in a single semester, this first phase of the project sought to generate useful features from video data to enrich future lip reading models, while also setting the framework for a lip-reading architecture, and providing the visual interface that would be needed to use it. To accomplish the first part of this goal, we trained convolutional neural networks (CNNs) on datasets of faces with ground truth emotion and age labels to generate a model that upon video input would approximate a subject’s emotion and age. In the context of our eventual lip reading, this allows several benefits. Namely, in contrast to traditional systems that depend on continuous stream of data from which to draw text, an alternative could employ NLP (with age and emotion characteristics behind utterances as features) to not only output current words being said, but also predict ones that are going to be uttered. In addition to the generation of this model, the given project found and attained the usage rights to a dataset developed specifically for the purposes of lip-reading and developed most of the tools necessary to pre-process that data. Those tools as well as the model output are displayed in the final program. Consequently, this leaves Insights-ReadME poised to implement the lip-reading model itself in future semesters. "
    introduction = Toplevel(gui)
    introduction.title("Introduction")
    introduction.geometry("450x500")
    label = Label(introduction, text=intro_text,
                  wraplength=400, justify="left")
    label.pack()


def future():
    future_text = "The models we built this semester serve as infrastructure to better implement our Automatic Lip Reader. As such, the combination of these models and other natural language processing features would allow us to not only process individual, random frames taken of a video but also consider the linguistic, situational, and social environments the speaker is speaking in. The emotions an individual is feeling greatly influences the words they choose to say, and this information would consequently improve the accuracy of our Automatic Lip Reader in predicting the speaker’s next words and phrases. Furthermore, we were considering constructing other computer vision models as well, such as an age prediction model. While this feature is also rather subjective, dependent only on visual appearance, the general ability to judge one’s age can provide valuable information on the vernacular they regularly use. As an academic project, this was a very informative introduction to convolutional neural networks and machine learning algorithms!"
    future = Toplevel(gui)
    future.title("Next Steps")
    future.geometry("450x300")
    label = Label(future, text=future_text,
                  wraplength=400, justify="left")
    label.pack()


def capture():
    exec(open('emotions_disp.py').read())


def crop_lips():
    exec(open('frames.py').read())
    exec(open('extract_lips.py').read())


canvas = Canvas(gui, width=400, height=400)
img = PhotoImage(file="emotionemojis.png")
img2 = PhotoImage(file="kevinangry.png")
img3 = PhotoImage(file="croppedlips.png")

canvas.create_image(205, 100, image=img, anchor="center")

canvas.create_image(290, 290, image=img2, anchor="se")
canvas.create_image(190, 280, image=img3, anchor="se")
canvas.pack()
pixelVirtual = PhotoImage(width=1, height=1)

introduction_button = Button(gui, anchor=tkinter.CENTER, text="Intro", foreground='black', image=pixelVirtual,
                             width=75, height=30, compound="c", command=introduction)
introduction_button.place(x=33, y=300)

crop_lips_button = Button(gui, anchor=tkinter.CENTER, text="Crop Lips", foreground='blue', image=pixelVirtual,
                          width=75, height=30, compound="c", command=crop_lips)
crop_lips_button.place(x=133, y=300)

capture_button = Button(gui, anchor=tkinter.CENTER, text="Capture", foreground='purple', image=pixelVirtual,
                        width=75, height=30, compound="c", command=capture)
capture_button.place(x=233, y=300)

future_button = Button(gui, anchor=tkinter.CENTER, text="Next Steps", foreground='red', image=pixelVirtual,
                       width=75, height=30, compound="c", command=future)
future_button.place(x=333, y=300)


gui.geometry("450x400")
gui.mainloop()
