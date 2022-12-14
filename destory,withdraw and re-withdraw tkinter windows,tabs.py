from tkinter import*
import random
def destroy():
    root.destroy()
def withdraw():
    root.withdraw()
def rando():
    CoNum = random.randint(0,70)
    l1 = Label(root,text = CoNum)
    l1.pack()
root = Tk()
b1 = Button(root,text = "destroy",command = destroy) #destroys the window
b1.pack()
b2 = Button(root,text = "withdraw",command = withdraw)#doesnt destroy window but takes it off screen and saves it contents
b2.pack()
b3 = Button(root,text = "random",command = rando)
b3.pack()

def destroy2():
    root2.destroy()
def ret():
    root.deiconify()
root2 = Tk()
b3 = Button(root2,text = "return", command = ret)# re-withdraws the window
b3.pack()
b1 = Button(root2,text = "destroy",command = destroy2) #destroys the window
b1.pack()
root2.mainloop()
root.mainloop()