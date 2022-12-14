from tkinter import *

def on_win_request(parent):
    dialog = Toplevel()
    parent.wait_window(dialog)
    # executed only when "dialog" is destroyed
    print("Mini-event loop finished!")

r = Tk()
b = Button(r, text='New Window', command=lambda: on_win_request(r))
b.pack()
b2 = Button(r, text='Hello!', command=lambda: print("hello"))
b2.pack()
r.mainloop()