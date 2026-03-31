# TODO: 
# Fix the instructions (it's hard for the users to understand the game if you explain solely with word, so think about explaining to the users through a visual) and the display/format of it. Also maybe give the users the option to view the instructions or not view it. Maybe have the starting screen have "Welcome to Memory!", and under that have "1. How to Play" followed by "2. Start Game" at the next line, and then "3. Exit" (or Quit)
# Increase modularity (e.g., maybe do a function for displaying the instructions)
# Maybe remove the "e.g." because some people may not know what it means. If you keep it, figure out to do with the comma after "e.g."
# Fix the comments throughout the program and probably add more
# Understand the purpose of the .gitattributes file and what it does
# While the users are playing the game, maybe give them the option to exit, go back to the main menu, restart the game, and/or see the instructions
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
def print_scoreboard(p1_score, p2_score):
    print("   P1   P2")
    print(f"   0{p1_score}" if p1_score < 10 else f"{p1_score}", f"  0{p2_score}" if p2_score < 10 else f"{p2_score}" )
    print('-' * 13, end = "\n")

# Print grid
def print_grid(asterisks):
    print("  1 2 3 4 5", end = '')
    for i in range(0, 20):
        if i % 5 == 0:
            print('\n', "ABCD"[i//5], sep = '', end = ' ')
        
        print(asterisks[i], end = ' ')
    
# Brings in coordinates from the user and error checks
def get_valid_coordinate(is_p1_turn, previous_coordinate, asterisks):
    if is_p1_turn == True:
        current_player_turn = "Player 1"
    else:
        current_player_turn = "Player 2"

    while True:
        coordinate = input(f"\n{current_player_turn} enter a coordinate: ")
        if len(coordinate) != 2:
            print("Invalid input. Enter a letter followed by a number (e.g., A1).", end = '')
            continue
        
        row = coordinate[0].upper() # Make the letter uppercase
        col = coordinate[1]

        # Error check to make sure the user inputted a valid coordinate, didn't choose the same coordinate twice or a coordinate that has already been matched
        if row not in "ABCD" or col not in "12345":
            print("Invalid input. Enter a letter between A and D and a number between 1 and 5 (e.g., A1).", end = '')
            continue

        if row + col == previous_coordinate:
            print("Invalid input. Make sure you don't choose the same two coordinates.", end = '')
            continue

        if asterisks[Coordinates[row + col].value] == ' ':
            print("Invalid input. The coordinate you chose has already been matched.", end = '')
            continue
        
        final_coordinate = row + col

        return final_coordinate 

# Find who won the game at the end and print it out
def find_winner(p1_score, p2_score):
    if p1_score > p2_score:
        print("\nPlayer 1 wins!")
    elif p2_score > p1_score:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")

def main():
    asterisks = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] # List that starts as asterisks but will change throughout the game
    special_chars = ['!', '@', '#', '$', '%', '&', '?', '=', '+', '~', '!', '@', '#', '$', '%', '&', '?', '=', '+', '~'] # List of all special characters that will be used
    random.shuffle(special_chars) # Randomize game board

    is_p1_turn = True
    p1_score = 0
    p2_score = 0

    # Welcome message and instructions
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Memory Game! The goal of the game is to find all 10 matches. The player with the most matches at the end wins.")
    print("On your turn, you will choose two coordinates (e.g., A1 and B4). If the special characters behind those coordinates match, you get a point and go again. If not, it's the next player's turn.")
    print("Good luck!")
    input("\nPress Enter to start the game...")


    while (p1_score + p2_score) < 10: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print_scoreboard(p1_score, p2_score)
        print_grid(asterisks)
        first_coordinate = get_valid_coordinate(is_p1_turn, "NA", asterisks)
        special_chars[Coordinates[first_coordinate].value], asterisks[Coordinates[first_coordinate].value] = asterisks[Coordinates[first_coordinate].value], special_chars[Coordinates[first_coordinate].value]
        os.system('cls' if os.name == 'nt' else 'clear')
        print_scoreboard(p1_score, p2_score)
        print_grid(asterisks)
        second_coordinate = get_valid_coordinate(is_p1_turn, first_coordinate, asterisks)
        special_chars[Coordinates[second_coordinate].value], asterisks[Coordinates[second_coordinate].value] = asterisks[Coordinates[second_coordinate].value], special_chars[Coordinates[second_coordinate].value]
        os.system('cls' if os.name == 'nt' else 'clear')
        print_scoreboard(p1_score, p2_score)
        print_grid(asterisks)
        
        # Swaps the elements back so that the following if...else statement can properly tell if the user got a match or not 
        special_chars[Coordinates[first_coordinate].value], asterisks[Coordinates[first_coordinate].value] = asterisks[Coordinates[first_coordinate].value], special_chars[Coordinates[first_coordinate].value]
        special_chars[Coordinates[second_coordinate].value], asterisks[Coordinates[second_coordinate].value] = asterisks[Coordinates[second_coordinate].value], special_chars[Coordinates[second_coordinate].value]

        # Check if the user got a match or not and update the score and grid accordingly, then switch turns if they didn't get a match
        if special_chars[Coordinates[first_coordinate].value] == special_chars[Coordinates[second_coordinate].value]:
            print("\nYou got a match!")

            if is_p1_turn == True:
                p1_score += 1
            else:
                p2_score += 1

            asterisks[Coordinates[first_coordinate].value] = ' '
            asterisks[Coordinates[second_coordinate].value] = ' '
        else: 
            print("\nNot a match.")

            if is_p1_turn == True:
                is_p1_turn = False
            else:
                is_p1_turn = True

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
    print_scoreboard(p1_score, p2_score)
    print_grid(asterisks)

    find_winner(p1_score, p2_score) # Call the function that finds who won the game and prints it out

if __name__ == "__main__":
    main()