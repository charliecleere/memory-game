# TODO: 
# Fix the instructions and the display of it. Also maybe give the users the option to view the instructions or not view it. Maybe have starting screen have "Welcome to Memory!", and under that have "1. How to Play" followed by "2. Start Game" at the next line
# Increase modularity (e.g., maybe do a function for displaying the instructions)
# Maybe remove the "e.g." because some people may not know what it means. If you keep it, figure out to do with the comma after "e.g."
# Fix the comments throughout the program and probably add more
# Understand the purpose of the .gitattributes file and what it does
# While the users are playing the game, maybe give them the option to exit
# Maybe give the users the option to play more than one game. If you do this, maybe allow the users to do a series (maybe having them choose if they want to do, e.g., best-of-3 or best-of-7), keep track of the score in the series, and display winner of it


from enum import Enum
import random, os, time, sys

class Coordinates(Enum):
    A1 = 0
    A2 = 1
    A3 = 2
    A4 = 3
    A5 = 4
    B1 = 5
    B2 = 6
    B3 = 7
    B4 = 8
    B5 = 9
    C1 = 10
    C2 = 11
    C3 = 12
    C4 = 13
    C5 = 14
    D1 = 15
    D2 = 16
    D3 = 17
    D4 = 18
    D5 = 19

# Function definitions

# Print score board
def printScoreBoard(p1Score, p2Score):
    print("   P1   P2")
    print(f"   0{p1Score}" if p1Score < 10 else f"{p1Score}", f"  0{p2Score}" if p2Score < 10 else f"{p2Score}" )
    print('-' * 13, end = "\n")

# Print grid
def printGrid(asterisks):
    print("  1 2 3 4 5", end = '')
    for i in range(0, 20):
        if i % 5 == 0:
            print('\n', "ABCD"[i//5], sep = '', end = ' ')
        
        print(asterisks[i], end = ' ')
    
# Bring in coordinates and error check
def coordinateInput(isP1Turn, previousCoordinate, asterisks):
    if isP1Turn == True:
        currentPlayerTurn = "Player 1"
    else:
        currentPlayerTurn = "Player 2"

    while True:
        coordinate = input(f"\n{currentPlayerTurn} enter a coordinate: ")
        if len(coordinate) != 2:
            print("Invalid input. Enter a letter followed by a number (e.g., A1).", end = '')
            continue
        
        row = coordinate[0].upper() # Make the letter uppercase
        col = coordinate[1]

        # Error check to make sure the user inputted a valid coordinate, didn't choose the same coordinate twice or a coordinate that has already been matched
        if row not in "ABCD" or col not in "12345":
            print("Invalid input. Enter a letter between A and D and a number between 1 and 5 (e.g., A1).", end = '')
            continue

        if row + col == previousCoordinate:
            print("Invalid input. Make sure you don't choose the same two coordinates.", end = '')
            continue

        if asterisks[Coordinates[row + col].value] == ' ':
            print("Invalid input. The coordinate you chose has already been matched.", end = '')
            continue
        
        finalCoordinate = row + col

        return finalCoordinate 

# Find who won the game at the end and print it out
def findWinner(p1Score, p2Score):
    if p1Score > p2Score:
        print("\nPlayer 1 wins!")
    elif p2Score > p1Score:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")

def main():
    asterisks = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] # List that starts as asterisks but will change throughout the game
    specialChars = ['!', '@', '#', '$', '%', '&', '?', '=', '+', '~', '!', '@', '#', '$', '%', '&', '?', '=', '+', '~'] # List of all special characters that will be used
    random.shuffle(specialChars) # Randomize game board

    isP1Turn = True
    p1Score = 0
    p2Score = 0

    # Welcome message and instructions
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Memory Game! The goal of the game is to find all 10 matches. The player with the most matches at the end wins.")
    print("On your turn, you will choose two coordinates (e.g., A1 and B4). If the special characters behind those coordinates match, you get a point and go again. If not, it's the next player's turn.")
    print("Good luck!")
    input("\nPress Enter to start the game...")


    while (p1Score + p2Score) < 10: 
        os.system('cls' if os.name == 'nt' else 'clear')
        printScoreBoard(p1Score, p2Score)
        printGrid(asterisks)
        firstCoordinate = coordinateInput(isP1Turn, "NA", asterisks)
        specialChars[Coordinates[firstCoordinate].value], asterisks[Coordinates[firstCoordinate].value] = asterisks[Coordinates[firstCoordinate].value], specialChars[Coordinates[firstCoordinate].value]
        os.system('cls' if os.name == 'nt' else 'clear')
        printScoreBoard(p1Score, p2Score)
        printGrid(asterisks)
        secondCoordinate = coordinateInput(isP1Turn, firstCoordinate, asterisks)
        specialChars[Coordinates[secondCoordinate].value], asterisks[Coordinates[secondCoordinate].value] = asterisks[Coordinates[secondCoordinate].value], specialChars[Coordinates[secondCoordinate].value]
        os.system('cls' if os.name == 'nt' else 'clear')
        printScoreBoard(p1Score, p2Score)
        printGrid(asterisks)
        
        # Swaps the elements back so that the following if...else statement can properly tell if the user got a match or not 
        specialChars[Coordinates[firstCoordinate].value], asterisks[Coordinates[firstCoordinate].value] = asterisks[Coordinates[firstCoordinate].value], specialChars[Coordinates[firstCoordinate].value]
        specialChars[Coordinates[secondCoordinate].value], asterisks[Coordinates[secondCoordinate].value] = asterisks[Coordinates[secondCoordinate].value], specialChars[Coordinates[secondCoordinate].value]

        # Check if the user got a match or not and update the score and grid accordingly, then switch turns if they didn't get a match
        if specialChars[Coordinates[firstCoordinate].value] == specialChars[Coordinates[secondCoordinate].value]:
            print("\nYou got a match!")

            if isP1Turn == True:
                p1Score += 1
            else:
                p2Score += 1

            asterisks[Coordinates[firstCoordinate].value] = ' '
            asterisks[Coordinates[secondCoordinate].value] = ' '
        else: 
            print("\nNot a match.")

            if isP1Turn == True:
                isP1Turn = False
            else:
                isP1Turn = True

        time.sleep(2.25)

        # Clears any input typed during the pause
        if os.name == "nt":  # Windows
            import msvcrt
            # Check if any keys were pressed
            while msvcrt.kbhit():
                msvcrt.getch()  # Read and discard them
        else:  # Unix-like systems (Linux, macOS)
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)  # Flush input buffer

    os.system('cls' if os.name == 'nt' else 'clear')
    printScoreBoard(p1Score, p2Score)
    printGrid(asterisks)

    findWinner(p1Score, p2Score) # Call the function that finds who won the game and prints it out

if __name__ == "__main__":
    main()
