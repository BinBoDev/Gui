from tkinter import *
def submit():
    username = entry.get()
    print(f"Helo {username}")
def dele():
    entry.delete(0,END)
def backs():
    entry.delete(len(entry.get())-1,END)

window = Tk()
entry = Entry(window,
              font=("Arial",20))
entry.pack(side= LEFT)
submit = Button(window,text= "submit",command= submit)
submit.pack(side = RIGHT)
dell = Button(window,text="del",command=dele)
dell.pack(side=RIGHT)
backs = Button(window,text="backspace",command=backs)
backs.pack(side=RIGHT)

window.mainloop()