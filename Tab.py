from tkinter import *
from  tkinter import ttk

wd = Tk()
notebook = ttk.Notebook(wd)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
# notebook.pack()
notebook.pack(expand=True,fill="both")
Label(tab1,text="tab1").pack()
Label(tab2,text="tab2").pack()
wd.mainloop()