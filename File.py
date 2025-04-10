from tkinter import *
from tkinter import filedialog
def openfile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Project\\Python\\Gui",
                                          title="Open File",
                                          filetypes= (("text file","*.txt"),
                                                      ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

wd =Tk()
button = Button(wd,text="Open",command=openfile)
button.pack()
wd.mainloop()