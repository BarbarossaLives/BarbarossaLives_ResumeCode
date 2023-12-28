
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
style = ttk.Style("darkly")

#frame_left = ttk.Labelframe(root,bootstyle="PRIMARY")
#frame_right = ttk.Labelframe(root,bootstyle="SUCCESS")

label1 = ttk.Label(root,text="Pick you number between 1 and 100 ")
label2 = ttk.Label(root,text="The computer has picked a number")
label3 = ttk.Label(root,text="Pick your number.")


root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)

#frame_left.grid(row=1, column=1)
#frame_right.grid(row=1, column=2)
label1.grid(column=0,row=1,padx=10)
label2.grid(column=1,row=1,padx=10)


root.mainloop()