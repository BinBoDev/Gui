from tkinter import *
from tkinter import filedialog
def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("text files","*.txt"),
                                               ("HTML files",".html"),
                                               ("all file","*.*")])
    fileText = str(text.get("1.0",END))
    file.write(fileText)
    file.close()
wd = Tk()
text = Text(wd)
text.pack()
button = Button(wd,text="Save",command=saveFile)
button.pack()
wd.mainloop()