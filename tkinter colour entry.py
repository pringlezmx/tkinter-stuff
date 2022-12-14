from tkinter import*
def change():
    col.configure(bg = colour.get())
    
    
col = Tk()
col.geometry("270x420")
col.resizable(False,False)
col.configure(background = "red")
box = Frame(col)
box.grid (row = 0, column = 0, columnspan = 2, padx = 30, pady = 5)
box2 = Frame(col)
box2.grid(row=1, column = 0, columnspan = 2, padx = 25, pady  =10)
Label(box, text = "Choose colour",font = ("Arial",16))\
           .grid(row = 0, column = 0, padx = 10, pady = 10)
Label(box2,text= "enter colour:")\
                 .grid(row = 0, column =0 , padx= 10, pady = 10)

colour = Entry(box2,width = 15,bg= "white")
colour.grid(row = 0, column = 1, padx = 5, pady = 5)

button = Button(col, text = "submit", width = 7, command = change)
button.grid(row = 2, column = 0, padx = 0, pady = 5)

col.mainloop()