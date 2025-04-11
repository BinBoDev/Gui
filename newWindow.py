from tkinter import *
def openWindow():
    # new_Window = Toplevel()
    new_Window = Tk()
    wd.destroy()
wd = Tk()
button = Button(wd,text="New Window",command=openWindow).pack()

wd.mainloop()