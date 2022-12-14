# make a button do 2things depending on stuff
from tkinter import*

tet = Tk()
def change():
    if tet["background"] == "red":
        tet.configure(background = "sky blue")
    elif tet["background"] != "red":
        tet.configure(background ="red")
tet.configure(background = "skyblue")
button = Button(tet,text = "press", width = 7, background = "light pink", command = change)
button.grid(row = 1, column = 1, padx =50, pady = 50)
tet.mainloop()