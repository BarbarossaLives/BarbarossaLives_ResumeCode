# writeToFile('greet.txt', 'Hello!\n') 
# appendToFile('greet.txt', 'Goodbye!\n') 
# assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'


def writeToFile(file,text):
    program_file = open(file,w)
    program_file.write(text)
    program_file.close(file)
    
    
def appendToFile(file,text):
    program_file = open(file,a)
    program_file.write(text)
    program_file.close(file)
    
    
    
def readFromFile(file):