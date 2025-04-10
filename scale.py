from tkinter import *
def Show():
    print(f"Nhiet do laf {scale.get()}")
wd = Tk()
scale = Scale(wd,from_=100,to=0,
              length=600,
              tickinterval=10,
              resolution=1,
              troughcolor= "red",
              fg= "Blue",
              bg= "yellow"

              )
scale.pack()
button = Button(wd,text="submit",command=Show,)
button.pack()
wd.mainloop()