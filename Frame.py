from idlelib.configdialog import font_sample_text
from tkinter import *
wd = Tk()
frame = Frame(wd)
frame.pack()
button =Button(frame,text="W",font=("Arial",25),width=3).pack(side=TOP)
button =Button(frame,text="A",font=("Arial",25),width=3).pack(side=LEFT)
button =Button(frame,text="S",font=("Arial",25),width=3).pack(side=LEFT)
button =Button(frame,text="D",font=("Arial",25),width=3).pack(side=LEFT)
wd.mainloop()