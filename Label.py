from tkinter import *
window = Tk()
photo = PhotoImage(file='Bin.png')
label = Label(window,text="Bian Pham",
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief= RAISED,
              bd= 10,
              padx=20,
              pady=20,
              image=photo,
              compound= 'bottom'

              )
label.pack()
#label.place(x=100,y=100)
window.mainloop()