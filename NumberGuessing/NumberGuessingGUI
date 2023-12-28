import PySimpleGUI as sg
import random
comp_guess = random.randint(1,100)
L = 1
H = 1000
guess_result = ""
my_number = 0
won = False

frame_layout_left = [[sg.Push(),sg.Text("Pick your number between 1 and 1000"),sg.Push()],
                     [sg.Push(),sg.Text(""),sg.Push()],
                     [sg.Push(),sg.Text("Pick your number"),sg.Push()],
                     [sg.Push(),sg.Input(size = 15,key="--my_number--"),sg.Push()],
                     [sg.Push(),sg.Text("Have the computer guess"),sg.Push()],
                     [sg.Push(),sg.Button("Guess",key="--comp_guess_button--"),sg.Push()],
                     [sg.Push(),sg.Text("The computer guesses:"),sg.Push()],
                     [sg.Push(),sg.Text(comp_guess, key="--comp_guess_text--"),sg.Push()],
                     [sg.Push(),sg.Text("Is the number too high or too low?"),sg.Push()],
                     [sg.Push(),sg.Button("High",key = "--high--"),sg.Button("Low",key = "--low--"),sg.Button("Just Right",key="--right--"),sg.Push()],
                     [sg.Push(),sg.Text('',key="--right_text--"),sg.Push()]]

frame_layout_right = [[sg.Push(),sg.Text("I have picked a number between 1 and 100."),sg.Push()],
                     [sg.Push(),sg.Text("Can you guess it?"),sg.Push()],
                     [sg.Push(),sg.Text("What is your guess?"),sg.Push()],
                     [sg.Push(),sg.Input(key="--player_guess--"),sg.Push()],
                     [sg.Push(),sg.Button("Guess",key="--player_guess_button--"),sg.Push()],
                     [sg.Push(),sg.Text('...',key="--guess_result--"),sg.Push()],
                     [sg.Push(),sg.Button("Try Again!",key="--reset--"),sg.Push()]]

column_left = [[sg.Frame("Computer Guess", frame_layout_left,s=(300,350))]]

column_right = [[sg.Frame("Player guess",frame_layout_right, s=(300,350))]]

layout = [[sg.Column(column_left),sg.Column(column_right)]]

def computer_guess(high,low):
    comp_guess = random.randint(low,high)
    return comp_guess     
    


window = sg.Window('Number Guessing Game', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'quit': # if user closes window or clicks cancel
        break
    if event == "--comp_guess_button--":
        comp_guess = computer_guess(H,L)
        window["--comp_guess_text--"].update(comp_guess)
    if event == "--high--":
        H = comp_guess
        comp_guess = computer_guess(H,L)
        window["--comp_guess_text--"].update(comp_guess)    
    if event == "--low--":
        L = comp_guess
        comp_guess = computer_guess(H,L)
        window["--comp_guess_text--"].update(comp_guess)
    if event == "--right--":
        window["--right_text--"].update("The computer guesses right!!!")   
        H = 1000
        L = 1
    
    if event == "--player_guess_button--":
        print(comp_guess)
        player_guess = values["--player_guess--"]
        print(player_guess)
        player_guess = int(player_guess)
        if player_guess == comp_guess:
            result = "You got it!!"
            window["--guess_result--"].update(result)
            won = True
        if player_guess > comp_guess:
            result = "Your guess is too high."
            window["--guess_result--"].update(result)
        if player_guess < comp_guess:
            result = "Your guess is too low."
            window["--guess_result--"].update(result)
    
    if event == "--reset--" and won == True:
        won = False
        comp_guess = random.randint(1,100) 
    if event == "--reset--" and won == False:
        result = "You need to guess the number first"
        window["--guess_result--"].update(result)
window.close()