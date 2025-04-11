from tkinter import *
def openFile():
    print("File Open")
def saveFile():
    print("Save File")
def exitFile():
    print("Exit File")
wd = Tk()
menubar = Menu(wd)
wd.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=exitFile)
wd.mainloop()
