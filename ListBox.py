from tkinter import *
def AddItem():
    if(entryInput.get() != "" and CheckAdd(entryInput.get())):
        listBox.insert(listBox.size(),entryInput.get())
        listBox.config(height=listBox.size())
        entryInput.delete(0,END)
    else:
        print(f"Da ton tai item + {entryInput.get()} + !")
def CheckAdd(addItem):
    items = listBox.get(0,END)
    for item in items:
        if(addItem == item):
            return False
    return True
def DelItem():
    listBox.delete(listBox.curselection())
    listBox.config(height=listBox.size())
wd = Tk()
listBox = Listbox(wd)
listBox.pack()
listBox.insert(0,"Bong")
listBox.insert(1,"Bin")
listBox.insert(2,"Tan")
listBox.insert(3,"Dung")
listBox.config(height=listBox.size())
entryInput = Entry(wd)
entryInput.pack()
addButton = Button(wd,text="Add",command=AddItem)
addButton.pack()
delButton = Button(wd,text="del",command=DelItem)
delButton.pack()

wd.mainloop()