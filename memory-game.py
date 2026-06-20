from enum import Enum
import random, os, time

# Platform-specific imports for input clearing during pause
try:
    import msvcrt
except ImportError:
    msvcrt = None

try:
    import termios
    import sys
except ImportError:
    termios = None

# Maps grid coordinates (A1–D5) to list indices (0–19)
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

def display_starting_menu():
    print("Welcome to Memory!\n")
    print("1. How to Play")
    print("2. Start Game")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice in ("1", "2", "3"):
            return choice

        print("Invalid. Please enter 1, 2, or 3.")

def print_instructions():
    print("How to Play Memory\n")
    print("The board is a 4x5 grid of coordinates, each of which hides a symbol:\n")
    print("  1 2 3 4 5")
    print("A * * * * *")
    print("B * * * * *")
    print("C * * * * *")
    print("D * * * * *\n")
    print("There are 10 pairs of hidden symbols. The goal is to match the most pairs.\n")
    print("• On your turn, enter two coordinates (such as A1 and B4).")
    print("• If the symbols match, you earn 1 point and take another turn.")
    print("• If they do not match, it goes to the other player's turn.")
    print("• Matched pairs are removed from the board and cannot be selected again.")
    print("• The player with the most matches when all pairs are found wins.")

def print_scoreboard(p1_score, p2_score):
    print("   P1   P2")
    print(f"   {p1_score:02}   {p2_score:02}")
    print('-' * 13)

def print_grid(asterisks):
    print("  1 2 3 4 5", end = '')
    for i in range(0, 20):
        if i % 5 == 0:
            print('\n', "ABCD"[i//5], sep = '', end = ' ')
        
        print(asterisks[i], end = ' ')
    
def get_valid_coordinate(is_p1_turn, previous_coordinate, asterisks):
    current_player_turn = "Player 1" if is_p1_turn else "Player 2"

    while True:
        coordinate = input(f"\n{current_player_turn} enter a coordinate: ")
        
        if len(coordinate) != 2:
            print("Invalid. Enter a letter followed by a number (example: A1).", end = '')
            continue
        
        row = coordinate[0].upper()
        col = coordinate[1]

        if row not in "ABCD" or col not in "12345":
            print("Invalid. Enter a letter between A and D and a number between 1 and 5 (example: B3).", end = '')
            continue

        if row + col == previous_coordinate:
            print("Invalid. Make sure you don't choose the same two coordinates.", end = '')
            continue

        if asterisks[Coordinates[row + col].value] == ' ':
            print("Invalid. The coordinate you chose has already been matched.", end = '')
            continue
        
        final_coordinate = row + col

        return final_coordinate 

def find_winner(p1_score, p2_score):
    if p1_score > p2_score:
        print("\nPlayer 1 wins!")
    elif p2_score > p1_score:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        choice = display_starting_menu()

        if choice == "1":  # How to Play
            os.system('cls' if os.name == 'nt' else 'clear')

            print_instructions()

            input("\nPress Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == "2":  # Start Game

            asterisks = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
            special_chars = ['!', '@', '#', '$', '%', '&', '?', '=', '+', '~', '!', '@', '#', '$', '%', '&', '?', '=', '+', '~']
            random.shuffle(special_chars)

            is_p1_turn = True
            p1_score = 0
            p2_score = 0

            # Main game loop (runs until all 10 pairs are found)
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

                # Check for match
                # Update score and grid if matched
                # Switch turns if not matched
                if special_chars[Coordinates[first_coordinate].value] == special_chars[Coordinates[second_coordinate].value]:
                    print("\nYou got a match!")

                    if is_p1_turn:
                        p1_score += 1
                    else:
                        p2_score += 1

                    asterisks[Coordinates[first_coordinate].value] = ' '
                    asterisks[Coordinates[second_coordinate].value] = ' '
                else: 
                    print("\nNot a match.")

                    if is_p1_turn:
                        is_p1_turn = False
                    else:
                        is_p1_turn = True

                time.sleep(2.25)

                # Clears any input typed during the pause
                if os.name == "nt" and msvcrt:  # Windows
                    while msvcrt.kbhit():
                        msvcrt.getch()
                elif termios:  # Unix-like systems (Linux, macOS)
                    termios.tcflush(sys.stdin, termios.TCIFLUSH)

            os.system('cls' if os.name == 'nt' else 'clear')
            print_scoreboard(p1_score, p2_score)
            print_grid(asterisks)

            find_winner(p1_score, p2_score) # Call the function that finds who won the game and prints it out
            
            input("\nPress Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == "3":  # Exit
            break

if __name__ == "__main__":
    main()