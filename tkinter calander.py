from tkinter import*
import calendar

text = calendar.calendar(2021)
cal = Tk()
cal.geometry("550x600")
cal.configure(bg = "white")
cal.title("calendar")
label = Label(cal,text = "Calendar",bg = "dark gray", font = ("times",28))
label.grid(row = 1, column = 1)
label1 = Label(cal,text = text, font = "consolas 10 bold")
label1.grid(row=2,column=1,padx=20)
cal.mainloop()

