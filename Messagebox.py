from tkinter import *
from tkinter import messagebox
def click():
    # messagebox.showinfo(title="Bian", message="Bian Pham")
    # messagebox.showerror(title="Warning",message="Bian")
    messagebox.askokcancel(title="Bian",message="Bian")

wd = Tk()
button = Button(wd, text="Click", command=click)
button.pack()
wd.mainloop()
