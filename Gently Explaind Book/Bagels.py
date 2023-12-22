# from the "Big book of small Python projects"

# goal to me with these is to get the info in your head through  repetion.
# learn what is does, but the repetion means you arn't looking something up
# differnce between memeroization and learning though doing.add()
# also the typing practice is emensly helpfull.


import random

NUM_DIGITS = 3 # you can change the difficulty by chaning the number of digits
MAX_GUESSES = 10   # again we can change the difficulty

def main():  
    print('''Bagels is a deductive logic game. Here are the rules.
          I am thinking of {} digit number with no repeating digits
          Try to guess the number.  I will give you some clues along the way,
          When I Say:        That Means
            Pico                One digit is correct but in the wrong place
            Fermi               One digit is correct and in the right place
            Bagels              No digit is correct
            
            For example, if the secret number was 248 and your guess was 843, the clue would be Fermi Pico'''.format(NUM_DIGITS))
    
    while True: # Main Game loop
        # this generates and stores the secret number
        secretNum = getSecretNum()
        print (" I got the number for you to guess")
        print("You have {} guesses to get the number".format(MAX_GUESSES))
        
        numGuesses = 1 # initialize the counter
        
        while numGuesses <= MAX_GUESSES:
            guess = "" # initalize the guess vaiable and then check for errors
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("guess #".format(numGuesses))
                guess = input("> ")
                
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1
                
                if guess == secretNum:
                    break # stop asking for guess because you have it right
                if numGuesses > MAX_GUESSES:
                    print("You have run out of guesses.")
                    print("The answer was: ".format(secretNum))
                    
            print("Do you want to try again? (yes/no)")
            if not input("> ").lower().startswith("y"):
                break
            
        print("Thank for playing!")
        
def getSecretNum():
    #creates the secret number
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # gives the clues for each guess
    if guess == secretNum:
        return "You got it"
    
    clues= []
    for i in range (len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        
        elif guess[i] in secretNum:
            clues.append("Pico")
            
    if len(clues) == 0:
        return "Bagels"
    
    else:
            
        # sorts the clues so they always in alphabetical order:
        clues.sort()   
        
        return "" .join(clues)
        
if __name__ == "__main__":
    main()
             
        
            