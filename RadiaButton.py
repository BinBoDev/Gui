from tkinter import *
food = ["🍕Pizza","🌭Hotdog","🍔Hamberger"]
def check():
    if(x.get() == 0):
        print("Ban  chon Pizza")
    elif(x.get()==1):
        print("Ban chon Hotdog")
    elif(x.get()==2):
        print("Ban chon Hamberger")


wd = Tk()
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(wd,text= food[index],
                              variable=x,value=index,
                              padx=10,
                              command=check
                              )
    radiobutton.pack(anchor= W)
wd.mainloop()