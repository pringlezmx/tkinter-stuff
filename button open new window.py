from tkinter import*
import random

colour = ["red","green","blue"]
root = Tk()
def op():
    root2 = Tk()
    CoNum = random.randint(0,2)
    RaNum = random.randint(0,2)
    print(colour[CoNum], RaNum)
    l1 = Label(root2,text = RaNum, font = ("Arial",10),bg = colour[CoNum])
    l1.pack()
    root2.config(bg = colour[CoNum])
    root2.mainloop()
b1 = Button(root,text = "click",command = op)
b1.pack()
root.mainloop()

