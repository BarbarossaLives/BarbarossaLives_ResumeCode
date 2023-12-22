

import time

def intro():
    print('''Let's create some Mad-Libs.  I have 5 different ones.  Which one would you like to try?''')
    choice_intro = input("Enter 1,2,3,4 or 5>>")
    return choice_intro
    
    
def madlib_1():

    print("Let's choose the words to fill in the blanks.  This Mad-lib has 9 missing words.")
    adj_1 = input("Enter an adjective of your choice.")
    plural_noun = input("Enter a plural noun.")
    place = input("Enter a place.")
    noun_1 = input("Enter a noun.")
    noun_2 = input("Enter another noun.")
    noun_3 = input("Enter a third noun.")
    animal = input("Choose an animal.")
    adj_2 = input("Choose another adjective.")
    adj_3 = input("Lastly please choose one last adjective.")
    print("Preparing the Mad Lib...")
    time.sleep(2)
    print(f"Once upon a(n) {adj_1} day in the land of {place}, a brave {noun_1} set out on a(n) {adj_2} adventure. They carried a trusty {noun_2} and a bag filled with {plural_noun}. As they journeyed through the {adj_3} forest, they encountered a friendly {animal}, who offered to be their guide. Together, they embarked on a(n) {adj_3} quest to find the legendary {noun_3}")
    
def madlib_2():
    print("Let's create a Mad-lib. This one has 10 missing words.")
    noun_1 = input("Please enter a noun.")
    adj_1 = input("Enter an adjective.")
    occ = input("Choose an occupation.")
    name= input("Enter your name.")
    noun_2 = input("Enter another noun.")
    activity = input("Pick an activity.")
    noun_3 = input("Now we need another noun.")
    adj_2 = input("Pick another adjective.")
    noun_4 = input("Choose another noun.")
    adj_3 = input("And one more adjective.")
    print("Preparing the Mad Lib...")
    time.sleep(2)
    
    print(f"In a quaint little {noun_1}, there lived a(n) {adj_1} {occ} named {name}. They were known throughout the town for their incredible {noun_2} and their love of {activity}. One day, a mysterious {noun_3} arrived at their doorstep, containing a {adj_2} map leading to a hidden treasure. Without hesitation, {name} gathered their {noun_4}] and set off on a(n) {adj_3} journey.")
    
def madlib_3():
    print("Can you come up with 7 words for this Mad-lib.")
    
    noun_1 = input("Choose a Noun:")
    plural_noun_1 = input("Pick a plural noun:")
    adj_1 = input("Choose an adjective:")
    noun_2 = input("Pick another noun:")
    plural_noun_2 = input("We need another plural noun:")
    verb_1 = input("Now pick a verb:")
    noun_3 = input("One more noun and we are done:")
    print("Preparing the Mad Lib...")
    time.sleep(2)
    
    print(f"On a stormy {noun_1}, a group of {plural_noun_1} found themselves stranded on a deserted {adj_1} island. With only a[n] {noun_2} and a box of {plural_noun_2} to sustain them, they had to work together to {verb_1} their way off the island. Each member of the group had a unique {noun_3}, which proved to be incredibly useful in their quest for rescue.")
    
def madlib_4():
    print("Give me some words to make our Mad-lib with.  This one needs 12 words.")
    
    adj_1 = input("Grad an adjective:")
    print("Conjuction Juction!!")
    name = input("Pick a name, any name:")
    activity = input("Pick an activity you like to do:")
    noun_1 = input("Pick a noun:")
    noun_2 = input("And another one, noun that is:")
    noun_3 = input("Wow, we need another noun:")
    print("What's your function?")
    adj_2 = input("We will need another adjective:")
    name_2 = input("Another name please:")
    adj_3 = input("Isn't this fun?  Pick another adjective:")
    noun_4 = input("This one needs lots of nouns.  Pick another noun:")
    noun_5 = input("One last noun please:")
    name_3 = input("Last thing.  We need one last name")
    print("Preparing the Mad Lib...")
    time.sleep(2)
    
    print(f"In a faraway kingdom, there lived a(n) {adj_1} princess named {name}. She was known for her love of {activity} and her incredible {noun_1}. One day, a {noun_2} appeared in her {noun_3}, containing a magical {adj_2} mirror. The mirror revealed a prophecy that {name_2} would embark on a(n) {adj_3} journey to save the kingdom from a looming {noun_4}. With the help of a trusty {noun_5}, {name_3} set out to fulfill her destiny.")


def madlib_5():
    print("We need 11 words to make the Mad-lib work.")
    place_1 = input("First we need a place:")
    adj_1 = input("Next pick an adjective:")
    noun_1 = input("Now we need a noun:")
    name_1 = input("How about a name:")
    plural_noun_1 = input("Pick a plural noun, please:")
    noun_2 = input("More nouns and more nouns, pick one now:")
    adj_2 = input("We need another adjective:")
    noun_3 = input("Last noun, I promise:")
    adj_3 = input("Another adjective:")
    activity = input("Activity please:")
    adj_4 = input("Last one, pick an adjective:")
    time.sleep(2)
    
    print(f"In a bustling {place_1}, there was a {adj_1} shop run by a quirky {noun_1} named {name_1}. The shop was filled with all sorts of {plural_noun_1}, from enchanted {noun_2} to mysterious {adj_2} potions. One day, a curious {noun_3} entered the shop and asked for a {adj_3} potion to help them with their upcoming {activity}. Little did they know, this potion would lead them on a(n) {adj_4} adventure filled with unexpected twists and turns.")
    
    
def choices(choice):

    if int(choice) == 1:
        madlib_1()
    
    if int(choice) == 2:
        madlib_2()
        
    if int(choice) == 3:
        madlib_3()
        
    if int(choice) == 4:
        madlib_4()
        
    if int(choice) == 5:
        madlib_5() 
        



play_again = "y"
while play_again == "y":
    choice = intro()
    choices(choice)
    play_again=input("Do you want to play again? (y/n)")
    
print("Thanks for playing")