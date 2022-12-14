import tkinter as tk
import time
 
#start = time.time()
root = tk.Tk()
tk.Label(root, text='Hello World!').pack()
#print(time.time() - start)
time.sleep(10)
root.mainloop()
