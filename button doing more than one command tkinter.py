from tkinter import *

root = Tk()
def bg():
    root.configure(bg = "red")
def la():
    l1.configure(text = "hi")
    l1.pack()
l1 = Label(root,text ="")
b1 = Button(root,text= "click", command = lambda:[bg(),la()])
b1.pack()
root.mainloop()