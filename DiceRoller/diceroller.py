import PySimpleGUI as sg
import random
# theme color of the GUI
sg.theme("dark grey")
# Setting the output to zero at the beginning of the program
rolltotal = 0

#Create the first column of the GUI
col_left = [[sg.Text("Die",size=15),],
            [sg.Text("_"*15)],
            [sg.Text("d4",size=15)],
            [sg.Text("d6",size=15)],
            [sg.Text("d8",size=15)],
            [sg.Text("d10",size=15)],
            [sg.Text("d12",size=15)],
            [sg.Text("d20",size=15)],
            [sg.Text("100",size=15)],
            [sg.Button("Roll D20", size=13, key="-ROLLD20-")],
            [sg.Text("0",size=15,key="-D20-")]]


# Create the second column of the GUI            
col_center = [[sg.Text("Number of Dice",size=15)],
              [sg.Text("_"*15)],
              [sg.Input("0",size=15,key="-NUMBERD4-")],
              [sg.Input("0",size=15,key="-NUMBERD6-")],
              [sg.Input("0",size=15,key="-NUMBERD8-")],
              [sg.Input("0",size=15,key="-NUMBERD10-")],
              [sg.Input("0",size=15,key="-NUMBERD12-")],
              [sg.Input("0",size=15,key="-NUMBERD20-")],
              [sg.Input("0",size=15,key="-NUMBERD100-")],
              [sg.Button("ROLL!",size=13,key="-ROLL-")],
              [sg.Button("CLEAR",size=13,key="-CLEAR-")]]


# creating the right column
col_right = [[sg.Text("Dice Total",size=15)],
             [sg.Text("_"*15)],
             [sg.Text("",size=15,key="-TOTALD4-")],
             [sg.Text("",size=15,key="-TOTALD6-")],
             [sg.Text("",size=15,key="-TOTALD8-")],
             [sg.Text("",size=15,key="-TOTALD10-")],
             [sg.Text("",size=15,key="-TOTALD12-")],
             [sg.Text("",size=15,key="-TOTALD20-")],
             [sg.Text("",size=15,key="-TOTALD100-")],
             [sg.Text("",size=15)],
             [sg.Text(f"Roll Total = {rolltotal}",key="-ROLLTOTAL-")]]

#Full layout of the window in PySimpleGUI
layout = [[sg.Column(col_left),sg.Column(col_center),sg.Column(col_right)]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #Gathering the amount of dice enter for each kind
    if event == "-ROLL-":
        d4_number = int(values["-NUMBERD4-"])
        d4=0
        d6_number = int(values["-NUMBERD6-"])
        d6=0
        d8_number = int(values["-NUMBERD8-"])
        d8=0
        d10_number = int(values["-NUMBERD10-"])
        d10=0
        d12_number = int(values["-NUMBERD12-"])
        d12=0
        d20_number = int(values["-NUMBERD20-"])
        d20=0
        d100_number = int(values["-NUMBERD100-"])
        d100=0
        #making sure the initail values are 0
        tot_d4 = 0
        tot_d6 = 0
        tot_d8 = 0
        tot_d10 = 0
        tot_d12 = 0
        tot_d20 = 0
        tot_d100 = 0
        
        
        # getting the random number for each one of the dice for each type 
        while d4 < d4_number:
            tot_d4 = tot_d4 + random.randint(1,4)
            d4 = d4 + 1
            
        while d6 < d6_number:
            tot_d6 = tot_d6 + random.randint(1,6)
            d6 = d6 + 1
            
        while d8 < d8_number:
            tot_d8 = tot_d8 + random.randint(1,8)
            d8 = d8 + 1
            
        while d10 < d10_number:
            tot_d10 = tot_d10 + random.randint(1,10)
            d10 = d10 + 1
            
        while d12 < d12_number:
            tot_d12 = tot_d12 + random.randint(1,12)
            d12 = d12 + 1
            
        while d20 < d20_number:
            tot_d20 = tot_d20 + random.randint(1,20)
            d20 = d20 + 1
            
        while d100 < d100_number:
            tot_d100 = tot_d100 + random.randint(1,100)
            d100 = d100 + 1
            
        #Updating the field with the total for each type of dice    
        window["-TOTALD4-"].update(tot_d4)
        window["-TOTALD6-"].update(tot_d6)
        window["-TOTALD8-"].update(tot_d8)
        window["-TOTALD10-"].update(tot_d10)
        window["-TOTALD12-"].update(tot_d12)
        window["-TOTALD20-"].update(tot_d20)
        window["-TOTALD100-"].update(tot_d100)
        rolltotal = (tot_d4 + tot_d6+ tot_d8 + tot_d10 + tot_d12 + tot_d20 + tot_d100 )
        window["-ROLLTOTAL-"].update(f"Roll Total = {rolltotal}")


    # The clear button resets all the numbers entered
    if event == "-CLEAR-":
        d4=0
        window["-NUMBERD4-"].update("0")
        window["-TOTALD4-"].update("0")
        d6=0
        window["-NUMBERD6-"].update("0")
        window["-TOTALD6-"].update("0")
        d8=0
        window["-NUMBERD8-"].update("0")
        window["-TOTALD8-"].update("0")
        d10=0
        window["-NUMBERD10-"].update("0")
        window["-TOTALD10-"].update("0")
        d12=0
        window["-NUMBERD12-"].update("0")
        window["-TOTALD12-"].update("0")
        d20=0
        window["-NUMBERD20-"].update("0")
        window["-TOTALD20-"].update("0")
        d100=0
        window["-NUMBERD100-"].update("0")
        window["-TOTALD100-"].update("0")
        
        window["-D20-"].update("0")
        window["-ROLLTOTAL-"].update("0")

    # the separate D20 roll
    if event == "-ROLLD20-":
        rolld20 = random.randint(1,20)
        window["-D20-"].update(rolld20)
        