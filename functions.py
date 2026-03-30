#- Print grid (step 4 and 11)
#- Bring in coordinates and error check (steps 5/6 and 12/13)

list = [ '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' ]

def print_grid():
    print("   1 2 3 4 5", end = ' ')
    for i in range(0, 20):
        if i % 5 == 0:
            print('\n', "ABCD"[i//5], end = ' ')
        
        print(list[i], end = ' ')



def coordinateInput():
    while True:
        coordinate = input("\nEnter coordinates (e.g. A1): ")
        if len(coordinate) != 2:
            print("Invalid input. Please enter a letter followed by a number (e.g. A1).")
            continue
        
        row = coordinate[0].upper()
        col = coordinate[1]

        if row not in "ABCD" or col not in "12345":
            print("Invalid input. Please enter a letter between A and D and a number between 1 and 5. (e.g. A1)")
            continue
        
        finalCoordinate = row + col

        return finalCoordinate


def findWinner():
    if p1Score > p2Score:
        print("Player 1 wins!")
    elif p2Score > p1Score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

print_grid()