from  tkinter import *
from tkinter import colorchooser
def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    wd.config(bg= colorHex)
wd = Tk()
wd.geometry("420x420")
button = Button(wd,text="Click",command=click)
button.pack()
wd.mainloop()