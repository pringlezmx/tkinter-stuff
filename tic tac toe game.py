from tkinter import*
import time
global boxes, player, found, winner, count, foundD
winner = ""
found = False
foundD = False
boxes = ["i"]*9
count = 0
'''maybe tell which playes go it is on the screen'''
#win
def retur():
    Label(boxS, text = winner+" won",font = ("Arial",16))\
           .grid(row = 0, column = 0, padx = 10, pady = 10)
    if found == True:
        show.deiconify()
#draw
def returD():
    Label(boxS, text = "draw",font = ("Arial",16))\
           .grid(row = 0, column = 0, padx = 10, pady = 10)
    if foundD == True:
        show.deiconify()

def store():
    global player
    player = playerE.get()
    '''in the future add a validation check for x and o'''

entrie = Tk()
entrie.geometry("300x200")
entrie.resizable(False,False)
boxe = Frame(entrie)
boxe.pack()
Label(boxe, text = "which player is starting",font = ("Arial",16))\
           .grid(row = 0, column = 0, padx = 10, pady = 10)
playerE = Entry(entrie, width=30, bg='White')
playerE.pack(pady=10)
buttone = Button(entrie,text = "sumbit", width = 7,command = lambda:[store(),entrie.destroy()])
buttone.pack()
entrie.mainloop()


show = Tk()
show.geometry("300x200")
show.resizable(False,False)
show.withdraw()
boxS = Frame(show)
boxS.pack()
#Label(boxS, text = winner+" won",font = ("Arial",16))\
           #.grid(row = 0, column = 0, padx = 10, pady = 10)

buttonS = Button(show,text = "Close", width = 7,command = lambda:[show.destroy()])
buttonS.pack()


root = Tk()
root.geometry("1000x1000")
root.resizable(False,False)
root.configure(bg = "black")


box1 = Frame(root,width=315,height=315)
box1.grid(row = 0, column = 0,columnspan = 1,padx= 0 ,pady =0)
box1.grid_propagate(False)
box2 = Frame(root,width=315,height=315)
box2.grid(row = 0, column = 1,columnspan = 1,padx= 28 ,pady =0)
box2.grid_propagate(False)
box3 = Frame(root,width=315,height=315)
box3.grid(row = 0, column = 2,columnspan = 1,padx= 0 ,pady =0)
box3.grid_propagate(False)

box4 = Frame(root,width=315,height=315)
box4.grid(row = 1, column = 0,columnspan = 1,padx= 0 ,pady =28)
box4.grid_propagate(False)
box5 = Frame(root,width=315,height=315)
box5.grid(row = 1, column = 1,columnspan = 1,padx= 28 ,pady =28)
box5.grid_propagate(False)
box6 = Frame(root,width=315,height=315)
box6.grid(row = 1, column = 2,columnspan = 1,padx= 0 ,pady =28)
box6.grid_propagate(False)

box7 = Frame(root,width=315,height=315)
box7.grid(row = 2, column = 0,columnspan = 1,padx= 0 ,pady =0)
box7.grid_propagate(False)
box8 = Frame(root,width=315,height=315)
box8.grid(row = 2, column = 1,columnspan = 1,padx= 28 ,pady =0)
box8.grid_propagate(False)
box9 = Frame(root,width=315,height=315)
box9.grid(row = 2, column = 2,columnspan = 1,padx= 0 ,pady =0)
box9.grid_propagate(False)

#placeing x or o
def change1():
    global player, count
    count += 1
    if player == "x":
        Label(box1,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[0] = "x"
        player = "o"
    elif player == "o":
        Label(box1,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[0] = "o"
        player = "x"
def change2():
    global player, count
    count += 1
    if player == "x":
        Label(box2,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[1] = "x"
        player = "o"
    elif player == "o":
        Label(box2,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[1] = "o"
        player = "x"
def change3():
    global player, count
    count += 1
    if player == "x":
        Label(box3,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[2] = "x"
        player = "o"
    elif player == "o":
        Label(box3,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[2] = "o"
        player = "x"
def change4():
    global player, count
    count += 1
    if player == "x":
        Label(box4,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[3] = "x"
        player = "o"
    elif player == "o":
        Label(box4,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[3] = "o"
        player = "x"
def change5():
    global player, count
    count += 1
    if player == "x":
        Label(box5,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[4] = "x"
        player = "o"
    elif player == "o":
        Label(box5,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[4] = "o"
        player = "x"
def change6():
    global player, count
    count += 1
    if player == "x":
        Label(box6,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[5] = "x"
        player = "o"
    elif player == "o":
        Label(box6,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[5] = "o"
        player = "x"
def change7():
    global player, count
    count += 1
    if player == "x":
        Label(box7,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[6] = "x"
        player = "o"
    elif player == "o":
        Label(box7,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[6] = "o"
        player = "x"
def change8():
    global player, count
    count += 1
    if player == "x":
        Label(box8,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[7] = "x"
        player = "o"
    elif player == "o":
        Label(box8,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[7] = "o"
        player = "x"
def change9():
    global player, count
    count += 1
    if player == "x":
        Label(box9,text="x",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[8] = "x"
        player = "o"
    elif player == "o":
        Label(box9,text="o",font = ("Arial",140)).grid(row=0,column=0,padx =110,pady =30)
        boxes[8] = "o"
        player = "x"
''' make it so it can see if there is three in a row or if every place has a letter in it to end the game,
the first tic tac toe has some code fo checking 3 in a row'''
#check winner
def check():
    global found, winner, count, foundD
    #x rows
    if boxes[0] == "x" and boxes[1] =="x" and boxes[2] == "x":
        found = True
        winner = "x"
    if boxes[3] == "x" and boxes[4] =="x" and boxes[5] == "x":
        found = True
        winner = "x"
    if boxes[6] == "x" and boxes[7] =="x" and boxes[8] == "x":
        found = True
        winner = "x"
    #x columns
    if boxes[0] == "x" and boxes[3] =="x" and boxes[6] == "x":
        found = True
        winner = "x"
    if boxes[1] == "x" and boxes[4] =="x" and boxes[7] == "x":
        found = True
        winner = "x"
    if boxes[2] == "x" and boxes[5] =="x" and boxes[8] == "x":
        found = True
        winner = "x"
    #x diagnals
    if boxes[0] == "x" and boxes[4] =="x" and boxes[8] == "x":
        found = True
        winner = "x"
    if boxes[2] == "x" and boxes[4] =="x" and boxes[6] == "x":
        found = True
        winner = "x"
    #o rows
    if boxes[0] == "o" and boxes[1] =="o" and boxes[2] == "o":
        found = True
        winner = "o"
    if boxes[3] == "o" and boxes[4] =="o" and boxes[5] == "o":
        found = True
        winner = "o"
    if boxes[6] == "o" and boxes[7] =="o" and boxes[8] == "o":
        found = True
        winner = "o"
    #o columns
    if boxes[0] == "o" and boxes[3] =="o" and boxes[6] == "o":
        found = True
        winner = "o"
    if boxes[1] == "o" and boxes[4] =="o" and boxes[7] == "o":
        found = True
        winner = "o"
    if boxes[2] == "o" and boxes[5] =="o" and boxes[8] == "o":
        found = True
        winner = "o"
    #o diagnals
    if boxes[0] == "o" and boxes[4] =="o" and boxes[8] == "o":
        found = True
        winner = "o"
    if boxes[2] == "o" and boxes[4] =="o" and boxes[6] == "o":
        found = True
        winner = "o"
    if count == 9:
        foundD = True
        time.sleep(3)
        root.withdraw()
        returD()   
    if found == True:
        time.sleep(3)
        root.withdraw()
        retur()
#https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
button1 = Button(root, text = "submit", width = 7, command = lambda:[change1(),button1.destroy(),check()])
button1.grid(row = 0, column = 0, padx = 0, pady = 5)
button2 = Button(root, text = "submit", width = 7, command = lambda:[change2(),button2.destroy(),check()])
button2.grid(row = 0, column = 1, padx = 0, pady = 5)
button3 = Button(root, text = "submit", width = 7, command = lambda:[change3(),button3.destroy(),check()])
button3.grid(row = 0, column = 2, padx = 0, pady = 5)
button4 = Button(root, text = "submit", width = 7, command = lambda:[change4(),button4.destroy(),check()])
button4.grid(row = 1, column = 0, padx = 0, pady = 5)
button5 = Button(root, text = "submit", width = 7, command = lambda:[change5(),button5.destroy(),check()])
button5.grid(row = 1, column = 1, padx = 0, pady = 5)
button6 = Button(root, text = "submit", width = 7, command = lambda:[change6(),button6.destroy(),check()])
button6.grid(row = 1, column = 2, padx = 0, pady = 5)
button7 = Button(root, text = "submit", width = 7, command = lambda:[change7(),button7.destroy(),check()])
button7.grid(row = 2, column = 0, padx = 0, pady = 5)
button8 = Button(root, text = "submit", width = 7, command = lambda:[change8(),button8.destroy(),check()])
button8.grid(row = 2, column = 1, padx = 0, pady = 5)
button9 = Button(root, text = "submit", width = 7, command = lambda:[change9(),button9.destroy(),check()])
button9.grid(row = 2, column = 2, padx = 0, pady = 5)


#while loop, stop loop when 3 in a row happens and close the program and show an end screen(who won)
