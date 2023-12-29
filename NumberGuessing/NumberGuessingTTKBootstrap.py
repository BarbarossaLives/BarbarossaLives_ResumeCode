import random
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
root.minsize(width=700,height=350)
root.title("Number Guessing Game")
style = ttk.Style("darkly")
H=100
L=1
comp_guess = 0
comp_number = random.randint(1,100)
print(comp_number)
player_guess = tk.StringVar()

def guess_number(L,H):
    global comp_guess
    comp_guess = random.randint(L,H)
    label_L5.config(text=comp_guess)
    return comp_guess
def high():
    global H
    H = comp_guess
    print(H)
def low():
    global L
    L = comp_guess 
    print(L)   
def right():
    label_L6.config(text = "The Computer got it right")
    global H 
    H = 100
    global L 
    L = 1
    
def player_guess_func():
    global player_guess
    p_guess = player_guess.get()
    print(type(p_guess))
    print("guess = " + str(p_guess))
    p_guess = int(p_guess)
    if p_guess > comp_number:
        label_R3.config(text="You guess is too high.")
        print(p_guess)
    elif p_guess < comp_number:
        label_R3.config(text="Your guess is to low.")
        print(p_guess)
    else:
        label_R3.config(text="You got it right. ")
        
        
def try_again():
    global comp_number
    comp_number = random.randint(1,100)
    

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)
root.rowconfigure(0,weight=3)
root.rowconfigure(1,weight=3)
root.rowconfigure(2,weight=3)
root.rowconfigure(3,weight=3)
root.rowconfigure(4,weight=3)
root.rowconfigure(5,weight=3)
root.rowconfigure(6,weight=3)
root.rowconfigure(7,weight=3)
root.rowconfigure(8,weight=3)
root.rowconfigure(9,weight=1)

label_L1 = ttk.Label(root,text="Pick your number between 1 and 100",font=("Georgia",14))
label_L2 = ttk.Label(root,text="Type your number:",font=("Georgia",14))
input_L1 = ttk.Entry(root)
label_L3 = ttk.Label(root,text="Have the computer guess.",font=("Georgia",14))
button_L1 = ttk.Button(root,text="Guess",bootstyle="secondary",command=lambda:guess_number(L,H))
label_L4 = ttk.Label(root,text="The computer guesses:",font=("Georgia",14))
label_L5 = ttk.Label(root,text="...",font=("Georgia",14)) #use label_L5.update
label_L6 = ttk.Label(root,text="Is the number too high, low or right?",font=("Georgia",14))
button_L2 =  ttk.Button(root,text="High",bootstyle="secondary",command=high)
button_L3 = ttk.Button(root,text="Low",bootstyle="secondary",command=low)
button_L4 = ttk.Button(root,text="Just Right",bootstyle="secondary",command=right)
label_R1 = ttk.Label(text="I have picked a number between 1 and 100",font=("Georgia",14))
label_R2 = ttk.Label(text="Can you guess it?",font=("Georgia",14))
input_R1 = ttk.Entry(root,textvariable=player_guess )
button_R1 = ttk.Button(root,text="My Guess",bootstyle="secondary", command=player_guess_func)
label_R3 = ttk.Label(root,text="...",font=("Georgia",14)) #use label_L5.update
button_R2 = ttk.Button(root,text="Try Again",bootstyle="secondary",command=try_again)

label_L1.grid(column=0,row=1,columnspan=3,padx=10)
input_L1.grid(column=0,row=2,columnspan=3,padx=10)
label_L2.grid(column=0,row=3,columnspan=3,padx=10)
label_L3.grid(column=0,row=4,columnspan=3,padx=10)
button_L1.grid(column=0,row=5,columnspan=3,padx=10)
label_L4.grid(column=0,row=6,columnspan=3,padx=10)
label_L5.grid(column=0,row=7,columnspan=3,padx=10)
label_L6.grid(column=0,row=8,columnspan=3,padx=10)
button_L2.grid(column=0,row=9)
button_L3.grid(column=1,row=9)
button_L4.grid(column=2,row=9)
label_R1.grid(column=3,row=1)
label_R2.grid(column=3,row=2)
input_R1.grid(column=3,row=3)
button_R1.grid(column=3,row=4)
label_R3.grid(column=3,row=5)
button_R2.grid(column=3,row=6)


root.mainloop()