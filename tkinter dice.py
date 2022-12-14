import random
from tkinter import*

def roll():
    number = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text=f"{random.choice(number)}{random.choice(number)}")
    l1.pack()
#Unicode Character 'DIE FACE+1' (\u2680= 1), unicode need \ before it.
root=Tk()
root.geometry("700x450")

l1 = Label(root,font=("times",200))

b1= Button(root,text="Roll", command = roll)
b1.place(x=350,y=0)

root.mainloop()
