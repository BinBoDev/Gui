from  tkinter import *
root = Tk()
root.geometry("430x430")
root.title("Bian Pham")
icon = PhotoImage(file='Bin.png')
root.iconphoto(True,icon)
mylabel = Label(root,text="Bian")
mylabel.pack()
root.mainloop()