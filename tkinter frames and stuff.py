from tkinter import*
def sumbit():
    print("username",username.get())#gets the user input from the entry box and outputs it
    print("firstname",firstname.get())
    print("lastname",lastname.get())

def clear():
    username.delete(0,END)# it deletes all the character input from character 0 to the END
    firstname.delete(0,END)
    lastname.delete(0,END)
    username.focus_set()
    username.focus_set()
    
root = Tk()
root.geometry("270x420")
root.title("student detail")
root.resizable(False,False)
root.configure(background = "light blue")

frame_heading = Frame(root)
frame_heading.grid (row = 0,column = 0, columnspan = 2, padx=30,pady =5)

frame_entry = Frame(root)
frame_entry.grid(row = 1, column= 0 , columnspan = 2, padx =25, pady =10)

Label (frame_heading,text="student details form",font = ("Arial",16))\
      .grid(row= 0, column = 0,padx= 0, pady = 5)  # \ indicates that the statement continues on the next line
Label(frame_entry,text="username: ")\
                                  .grid(row = 0, column = 0, padx = 10, pady = 10)
Label(frame_entry,text="firstname: ")\
                                   .grid(row = 1, column =0 ,padx = 10, pady = 10)
Label(frame_entry,text = "last name: ")\
                       .grid(row = 2, column= 0, padx = 10, pady = 10)
username = Entry(frame_entry,width = 15, bg = "white")
username.grid (row = 0, column = 1, padx = 5, pady = 5)

firstname = Entry(frame_entry,width = 15,bg = "white")
firstname.grid (row = 1, column = 1, padx = 5, pady = 5)

lastname = Entry(frame_entry, width = 15,bg = "white")
lastname.grid (row = 2, column = 1, padx = 5, pady = 5)

submit_button = Button(root, text = "submit", width =7, command = sumbit)
submit_button.grid(row = 2, column = 0,padx = 0,pady =5)

clear_button = Button(root, text ="clear", width = 7, command = clear)
clear_button.grid(row =2 , column = 1, padx = 0, pady = 5)



root.mainloop()
