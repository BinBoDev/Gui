from  tkinter import *
def click():
    print("Click button")
window = Tk()

button = Button(window,
                text= "Click me 👆",
                command= click,
                font=("Comic Sans",30),
                fg= 'green',
                bg= 'black',
                activeforeground= 'Red',
                activebackground='Blue'

                )
button.pack()
window.mainloop()