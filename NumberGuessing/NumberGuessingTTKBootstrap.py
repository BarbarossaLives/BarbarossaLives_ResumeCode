
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
style = ttk.Style("darkly")

frame_left = ttk.Labelframe(root,bootstyle="primary")
frame_right = ttk.Labelframe(root,bootstyle="primary")

label1 = ttk.Label(frame_left,text="Pick you number ")

frame_left.pack()
frame_right.pack()
label1.pack()



root.mainloop()