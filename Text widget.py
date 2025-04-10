from tkinter import *
def click():
    input = text.get("1.0",END)
    print(input)
wd = Tk()
text = Text(wd,bg="light yellow")
text.pack()
button = Button(wd,text="Submit",command=click)
button.pack()
wd.mainloop()