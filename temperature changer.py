from tkinter import *

var = 0


def fct_temp_plus():
    global var
    var = float(tekstvak_input_user.get())
    var += 1
    tekstvak_input_user.delete(0, END)
    tekstvak_input_user.insert(0, var)


def fct_temp_min():
    global var
    var = float(tekstvak_input_user.get())
    var -= 1
    tekstvak_input_user.delete(0, END)
    tekstvak_input_user.insert(0, var)


window = Tk()
window.geometry("800x400")  # not *
window.title("TEST")

label = Label(window, text="Temp?")
label.place(x=350, y=175)


temp_plus = Button(window, bd=10, width=10, height=1, text="+", command=fct_temp_plus, font=("Helvetica", 12))
temp_plus.place(x=500, y=150)


temp_min = Button(window, bd=10, width=10, height=1, text="-", font=("Helvetica", 12), command=fct_temp_min)
temp_min.place(x=500, y=200)

tekstvak_input_user = Entry(window, width=10)
tekstvak_input_user.insert(0, 19.0)
tekstvak_input_user.place(x=350, y=200)

window.mainloop()