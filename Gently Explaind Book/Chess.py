



def getChessSquareColor(row,col):
    
    
    # Not needed for assertions 
    #row = int(input("Enter the row:"))
    #col = int(input("Enter the column:"))
    
    if row >0 and row <= 8 and col > 0 and col<=8:
            if row % 2 != 0:
                if col % 2 != 0:
                    return "white"
                else:
                    return "black"
                    
            else:
                if col % 2 != 0 :
                    return "black"
                else:
                    return "white" 

    else:
        return "none"
        
        
assert getChessSquareColor(1, 1) == 'white' 
assert getChessSquareColor(2, 1) == 'black' 
assert getChessSquareColor(1, 2) == 'black' 
assert getChessSquareColor(8, 8) == 'white' 
assert getChessSquareColor(0, 8) == 'none'
assert getChessSquareColor(2, 9) == 'none'

