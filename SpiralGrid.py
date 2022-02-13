# Ryan Connors
# Genetic Chain Coding Challenge 
# Can be run in command line
# EXAMPLE: 'python SpiralGrid.py 15'


import sys

def main():

    #uses command line argument as gridSize
    if len(sys.argv) > 2:
        sys.exit("Too many arguments. Only enter one number as an argument.")  
    
    #ensure argument is an integer
    try:
        gridSize = int(sys.argv[1])
    except ValueError:
        sys.exit("Enter an integer as an argument.")

    #initialize "empty" grid
    grid = [[' ' for x in range (gridSize)] for y in range(gridSize)]
    
    #set first line length to grid size
    lineLength = gridSize

    #tracks start and end points
    currentY = 0
    currentX = 0
    
    #runs until the line length is less than one
    while lineLength >= 1:

        #fills in X's left --> right
        for y in range(currentX, lineLength):
            grid[currentX][y] = 'X'

        currentX += 2
        lineLength -= 1
        
        #fills in X's up --> down
        for x in range (currentY * -1, lineLength):
            grid[x][currentY-1] = 'X'

        #fills in X's right --> left
        for y in range (currentX, lineLength):
            grid[currentX * -1][y] = 'X'

        currentY -= 2
        lineLength -= 1

        #fills in X's down --> up
        for x in range (currentX, lineLength):
            grid[x][currentY *-1] = 'X'

    #creates and prints strings from 2d array
    for x in range(0, gridSize):
        arrayToString = '['
        for y in range(0, gridSize):
            arrayToString += grid[x][y]
            if y < gridSize-1:
                arrayToString += ' '
        
        arrayToString += ']'
        print(arrayToString)
    

main()
