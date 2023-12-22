import PySimpleGUI as sg
import random
import time


#layout of the MainGUI
layout = [[sg.Text("Welcome to Barbarossa Lives Mad-lib program")],
         [sg.Text("There are 5 Mad -libs to choose from.  Which one would you like to try?",size=(33,3))],
         [sg.Button(" 1 ",key="-1-"),sg.Text("  "),sg.Button(" 2 ",key="-2-"),sg.Text("   "),sg.Button(" 3 ", key="-3-"),sg.Text("   "),sg.Button(" 4 ",key="-4-"),sg.Text("   "),sg.Button(" 5 ",key="-5-")],
         [sg.Text(" "*50)],
         [sg.Text("",key="-MADLIB-",size=(33,10))],
         [sg.Button("Exit")]]

#Layouts for the pop-up windows for each of the Mad-lib choices along with assignment of the inputs to variables 
def madlib_1_box():
    layout = [[sg.Text("Fill out the words to use in this Mad-lib.")],
              [sg.Text("Enter as adjective of your choice:", size=24),sg.InputText(key="-ADJ-1-",size=15)],
              [sg.Text("Enter a place:", size=24),sg.InputText(key="-PLACE-",size=15)],
              [sg.Text("Enter a noun:",size=24),sg.InputText(key="-NOUN-1-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-2-",size=15)],
              [sg.Text("Enter another noun:",size=24),sg.InputText(key="-NOUN-2-",size=15)],
              [sg.Text("Enter a plural noun:", size=24),sg.InputText(key="-PLURAL-NOUN-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-3-",size=15)],
              [sg.Text("Enter an animal:",size=24),sg.InputText(key ="-ANIMAL-",size=15)],
              [sg.Text("Enter one last adjective:",size=24),sg.InputText(key ="-ADJ-4-",size=15)],
              [sg.Text("Enter a third noun:",size=24),sg.InputText(key="-NOUN-3-",size=15)],   
              [sg.CButton("Submit")]]
    
    window = sg.Window('Mad-Lib 1', layout)
    # Loop for each of the pop-up boxes
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            adj_1 = values["-ADJ-1-"]
            place = values["-PLACE-"]
            noun_1 = values["-NOUN-1-"]
            adj_2 = values["-ADJ-2-"]
            noun_2 = values["-NOUN-2-"]
            plural_noun = values["-PLURAL-NOUN-"]
            adj_3 = values["-ADJ-3-"]
            animal = values["-ANIMAL-"]
            adj_4 = values["-ADJ-4-"]
            noun_3 = values["-NOUN-3-"]
            madlib1 = (f"Once upon a(n) {adj_1} day in the land of {place}, a brave {noun_1} set out on a(n) {adj_2} adventure. They carried a trusty {noun_2} and a bag filled with {plural_noun}. As they journeyed through the {adj_3} forest, they encountered a friendly {animal}, who offered to be their guide. Together, they embarked on a(n) {adj_4} quest to find the legendary {noun_3}")
            return (madlib1)
 
def madlib_2_box():
    layout = [[sg.Text("Fill out the words to use in this Mad-lib.")],
              [sg.Text("Enter a noun:",size=24),sg.InputText(key="-NOUN-1-",size=15)],
              [sg.Text("Enter as adjective of your choice:", size=24),sg.InputText(key="-ADJ-1-",size=15)],
              [sg.Text("Choose an occupation:",size=24).sg.InputText(key="-OCC-",size=15)],
              [sg.Text("Choose a name:",size=24).sg.InputText(key="-NAME-",size=15)],
              [sg.Text("Enter another noun:",size=24),sg.InputText(key="-NOUN-2-",size=15)],
              [sg.Text("Enter an activity:", size=24),sg.InputText(key="-ACTIVITY-",size=15)],
              [sg.Text("Enter a third noun:",size=24),sg.InputText(key="-NOUN-3-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-2-",size=15)],
              [sg.Text("Enter a fourth noun:",size=24),sg.InputText(key="-NOUN-4-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-3-",size=15)],
              [sg.CButton("Submit")]]    
    window = sg.Window('Mad-Lib 2', layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            noun_1 = values["-NOUN-1-"]
            adj_1 = values["-ADJ-1-"]
            occ = values["-OCC-"]
            name = values["-NAME-"]
            noun_2 = values["-NOUN-2-"]
            activity = values["-ACTIVITY-"]
            noun_3 = values["-NOUN-3-"]
            adj_2 = values["-ADJ-2-"]
            noun_4 = values["-NOUN-4-"]
            adj_3 = values["-ADJ-3-"]

            madlib2 = (f"In a quaint little {noun_1}, there lived a(n) {adj_1} {occ} named {name}. They were known throughout the town for their incredible {noun_2} and their love of {activity}. One day, a mysterious {noun_3} arrived at their doorstep, containing a {adj_2} map leading to a hidden treasure. Without hesitation, {name} gathered their {noun_4}] and set off on a(n) {adj_3} journey.")
            return (madlib2)     

def madlib_3_box():
    layout = [[sg.Text("Fill out the words to use in this Mad-lib.")],
              [sg.Text("Enter a noun:",size=24),sg.InputText(key="-NOUN-1-",size=15)],
              [sg.Text("Enter a plural noun:", size=24),sg.InputText(key="-PLURAL-NOUN-1-",size=15)],
              [sg.Text("Enter as adjective of your choice:", size=24),sg.InputText(key="-ADJ-1-",size=15)],
              [sg.Text("Enter another noun:",size=24),sg.InputText(key="-NOUN-2-",size=15)],
              [sg.Text("Enter another plural noun:", size=24),sg.InputText(key="-PLURAL-NOUN-2-",size=15)],
              [sg.Text("Enter a verb:", size=24),sg.InputText(key="-VERB-1-",size=15)],
              [sg.Text("Enter a third noun:",size=24),sg.InputText(key="-NOUN-3-",size=15)],
              [sg.CButton("Submit")]]    
    window = sg.Window('Mad-Lib 3', layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            noun_1 = values["-NOUN-1-"]
            plural_noun_1 = values["-PLURAL-NOUN-1-"]
            adj_1 = values["-ADJ-1-"]
            noun_2 = values["-NOUN-2-"]
            plural_noun_2 = values["-PLURAL-NOUN-2-"]
            verb_1 = values["-VERB-1-"]
            noun_3 = values["-NOUN-3-"]

            madlib3 = (f"On a stormy {noun_1}, a group of {plural_noun_1} found themselves stranded on a deserted {adj_1} island. With only a[n] {noun_2} and a box of {plural_noun_2} to sustain them, they had to work together to {verb_1} their way off the island. Each member of the group had a unique {noun_3}, which proved to be incredibly useful in their quest for rescue.")  

def madlib_4_box():
    layout = [[sg.Text("Fill out the words to use in this Mad-lib.")],
              
              [sg.Text("Enter as adjective of your choice:", size=24),sg.InputText(key="-ADJ-1-",size=15)],
              [sg.Text("Pick a name:", size=24),sg.InputText(key="-NAME-",size=15)],
              [sg.Text("Enter an activity:", size=24),sg.InputText(key="-ACTIVITY-",size=15)],
              [sg.Text("Enter a noun:",size=24),sg.InputText(key="-NOUN-1-",size=15)],
              [sg.Text("Enter another noun:",size=24),sg.InputText(key="-NOUN-2-",size=15)],
              [sg.Text("Enter a third noun:",size=24),sg.InputText(key="-NOUN-3-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-2-",size=15)],
              [sg.Text("Choose another name:",size=24).sg.InputText(key="-NAME-2-",size=15)],
              [sg.Text("Enter a fourth noun:",size=24),sg.InputText(key="-NOUN-4-",size=15)],
              [sg.Text("Enter a fifth noun:",size=24),sg.InputText(key="-NOUN-5-",size=15)],
              [sg.Text("Choose another name:",size=24).sg.InputText(key="-NAME-3-",size=15)]
              [sg.CButton("Submit")]]    
    window = sg.Window('Mad-Lib 4', layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            adj_1 = values["-ADJ-1-"]
            name = values["-NAME-"]
            noun_1 = values["-NOUN-1-"]
            noun_2 = values["-NOUN-2-"]
            activity = values["-ACTIVITY-"]
            noun_3 = values["-NOUN-3-"]
            adj_2 = values["-ADJ-2-"]
            name_2 = values["-NAME-2-"]
            adj_3 = values["-ADJ-3-"]
            noun_4 = values["-NOUN-4-"]
            noun_5 = values["-NOUN-5-"]
            name_3 = values["-NAME-3-"]
            

            madlib4 = (f"In a faraway kingdom, there lived a(n) {adj_1} princess named {name}. She was known for her love of {activity} and her incredible {noun_1}. One day, a {noun_2} appeared in her {noun_3}, containing a magical {adj_2} mirror. The mirror revealed a prophecy that {name_2} would embark on a(n) {adj_3} journey to save the kingdom from a looming {noun_4}. With the help of a trusty {noun_5}, {name_3} set out to fulfill her destiny.")
            return (madlib4)
       
def madlib_5_box():
    layout = [[sg.Text("Fill out the words to use in this Mad-lib.")],
              [sg.Text("Pick a place:", size=24),sg.InputText(key="-PLACE-1-",size=15)],
              [sg.Text("Enter as adjective of your choice:", size=24),sg.InputText(key="-ADJ-1-",size=15)],
              [sg.Text("Enter a noun:",size=24),sg.InputText(key="-NOUN-1-",size=15)],
              [sg.Text("Pick a name:", size=24),sg.InputText(key="-NAME-1-",size=15)],
              [sg.Text("Enter a plural noun:", size=24),sg.InputText(key="-PLURAL-NOUN-",size=15)],
              [sg.Text("Enter another noun:",size=24),sg.InputText(key="-NOUN-2-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-2-",size=15)],
              [sg.Text("Enter a third noun:",size=24),sg.InputText(key="-NOUN-3-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-3-",size=15)],
              [sg.Text("Enter an activity:", size=24),sg.InputText(key="-ACTIVITY-",size=15)],
              [sg.Text("Enter another adjective:",size=24),sg.InputText(key ="-ADJ-4-",size=15)]
    ]
             
    window = sg.Window('Mad-Lib 4', layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Submit":
            place_1 = values["-PLACE-1-"]
            adj_1 = values["-ADJ-1-"]
            noun_1 = values["-NOUN-1-"]
            name_1 = values["-NAME-1-"]
            plural_noun = values[-PLURAL-NOUN-]
            noun_2 = values["-NOUN-2-"]
            adj_2 = values["-ADJ-2-"]
            noun_3 = values["-NOUN-3-"]
            adj_3 = values["-ADJ-3-"]
            activity = values["-ACTIVITY-"]
            adj_4 = values["-ADJ-4-"]
            

            madlib5 = (f"In a faraway kingdom, there lived a(n) {adj_1} princess named {name}. She was known for her love of {activity} and her incredible {noun_1}. One day, a {noun_2} appeared in her {noun_3}, containing a magical {adj_2} mirror. The mirror revealed a prophecy that {name_2} would embark on a(n) {adj_3} journey to save the kingdom from a looming {noun_4}. With the help of a trusty {noun_5}, {name_3} set out to fulfill her destiny.")
            return (madlib5)
        
        
#Main window and main game loop
window = sg.Window('My new window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "-1-":
        print("pressed 1")
        madlib1 = madlib_1_box()
        window["-MADLIB-"].update(madlib1)
    if event == "-2-":
        print("pressed 2")
        madlib1 = madlib_2_box()
        window["-MADLIB-"].update(madlib2)
    if event == "-3-":
        print("pressed 3")
        madlib1 = madlib_3_box()
        window["-MADLIB-"].update(madlib3)
    if event == "-4-":
        print("pressed 4")
        madlib1 = madlib_4_box()
        window["-MADLIB-"].update(madlib4)
    if event == "-1-":
        print("pressed 5")
        madlib1 = madlib_5_box()
        window["-MADLIB-"].update(madlib5)