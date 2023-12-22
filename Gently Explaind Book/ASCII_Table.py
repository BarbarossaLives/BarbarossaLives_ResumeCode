# creating a printout of the Ascii table


p# using the while loop with the If statement to get valid arguements

while True:
    begin= int(input("What ASCII value should I start with (32-126)?"))
    end = int(input("What ASCII value should I end with (32-126)")) +1
    if begin >= 32 and end <= 126 and end>= begin:
        # with valid date the for loop prints the ASCII value and the character it represents (points to)
        
        for i in range (begin,end):
            print(i,chr(i))
        print("Goodbye")
        break
    else:
        print("The numbers and not valid.")
    
