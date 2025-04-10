from tkinter import *
def check():
    if(x.get()==1):
        {
            print("Check")
        }
    else:
        print("un Check")
wd = Tk()
x= IntVar()
checkBt = Checkbutton(wd,text='check',variable=x,
                      onvalue=1,
                      offvalue=0,
                      command=check)
#Tùy giá trị trả về mà có BooleanVar
checkBt.pack()

wd.mainloop()