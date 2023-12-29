import random
import PySimpleGUI as sg


#Global Variables
player_money = 5000
player_bet = 300


#Set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backside"

deck=[]


#Gui layout  3 columns
sg.theme("DarkBlue12")



layout = [[sg.Push(),sg.Text("Dealer Hand",font = ("Georgia",20)),sg.Push()],
          [sg.Push(),sg.Text("-"*50),sg.Push()],
          [sg.Push(),sg.Text("",size=(20,3),key="--DealerHand--", auto_size_text=True),sg.Push()],
          [sg.Text('')],
          [sg.Push(),sg.Text("Current Bet: " + str(player_bet),font = ("Georgia", 16),key="--player_bet--"),sg.Push()],
          [sg.Text(" ")],
          [sg.Push(),sg.Text("",size=(20,3),key="--playerHand--", auto_size_text=True),sg.Push()],
          [sg.Push(),sg.Text("-"*50),sg.Push()],
          [sg.Push(),sg.Text("Player Hand",font = ("Georgia",20)),sg.Push()],
          [sg.Push(),sg.Button("Hit",size=(10,1)),sg.Button("Stay",size=(10,1)),sg.Push()],
          [sg.Push(),sg.Text("Player Money: " + str(player_money)),sg.Push()],
          [sg.Push(),sg.Input("Amount of Bet",key="--bet_amount--",size=(20,1)),sg.Button("Set Bet",key="--set_bet--"),sg.Push()],
          [sg.Push(),sg.Button("Play",size=(20,1),key="--play--"),sg.Push()],
          [sg.Text("",size=(50,2))],
          [sg.Push(),sg.Text("Messages",key="--messages--"),sg.Push()]]


#Functions

def getDeck():
    '''Return a list of (rank,suit) tuples for all 52 cards'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range (2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards
        for rank in ("J","Q","K","A"):
            deck.append((rank,suit)) # add the face cards
    random.shuffle(deck)
    return deck




# Main Loop
# Create the Window
window = sg.Window('Black Jack', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "--set_bet--" and "--bet_amount" > 0:
        player_bet = int("--bet_amount--`")
        
    
    if event == "--play--" and int(player_bet) > 0:
        getDeck()
        print(deck)
        
    
    #print('You entered ', values[0])

window.close()