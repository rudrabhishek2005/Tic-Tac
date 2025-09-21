# Import necessary module
from datetime import datetime

# Function to save game data to a file
def save_game_data(moves, result):
    with open("../../AppData/Roaming/JetBrains/PyCharmCE2023.2/scratches/game_data.txt", "a") as file:
        file.write(f"Date & Time: {datetime.now()}\n")
        file.write("Moves:\n")
        for i, move in enumerate(moves, 1):
            file.write(f"{i}. {move}\n")
        file.write(f"Result: {result}\n")
        file.write("=" * 30 + "\n")

# Welcome section of the game
def welcome():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    print("Let's start the game :)\n")
    print("Board before the start of the game..")

# Initialize the Tic Tac Toe board
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Write all the winning combinations of the game
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Change the dimension of the board(convert the 2-dimensional array to 1-dimensional array)
def dimension_change(arr):
    return [j for i in arr for j in i]

# Winning function
def winning(wins):
    changed_board = dimension_change(arr)
    for i in wins:
        if changed_board[i[0]] == changed_board[i[1]] == changed_board[i[2]]:
            print(f"Player {1 if changed_board[i[0]] == 'X' else 2} wins :)")
            return 1

# Function to display the board
def board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
            if j < len(arr[i]) - 1:
                print(" | ", end=" ")
        if i < len(arr) - 1:
            print("\n-------------")
    print("\n")

# Function to handle player 1
def player1(moves):
    pos = int(input("Player 1 - Enter position (1-9): "))
    if 1 <= pos <= 9:
        if pos <= 3:
            if arr[0][pos - 1] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player1(moves)
            else:
                arr[0][pos - 1] = "X"
                moves.append(f"Player 1 -> {pos}")
        elif pos <= 6:
            if arr[1][pos - 4] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player1(moves)
            else:
                arr[1][pos - 4] = "X"
                moves.append(f"Player 1 -> {pos}")
        elif pos <= 9:
            if arr[2][pos - 7] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player1(moves)
            else:
                arr[2][pos - 7] = "X"
                moves.append(f"Player 1 -> {pos}")
    else:
        print("Please enter between 1-9")
        player1(moves)
        
# Function to handle player 2
def player2(moves):
    pos = int(input("Player 2 - Enter position (1-9): "))
    if 1 <= pos <= 9:
        if pos <= 3:
            if arr[0][pos - 1] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player2(moves)
            else:
                arr[0][pos - 1] = "O"
                moves.append(f"Player 2 -> {pos}")
        elif pos <= 6:
            if arr[1][pos - 4] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player2(moves)
            else:
                arr[1][pos - 4] = "O"
                moves.append(f"Player 2 -> {pos}")
        elif pos <= 9:
            if arr[2][pos - 7] in ["X", "O"]:
                print("Invalid Position! Please enter again..")
                player2(moves)
            else:
                arr[2][pos - 7] = "O"
                moves.append(f"Player 2 -> {pos}")
    else:
        print("Please enter between 1-9")
        player2(moves)

# Call functions to run the program
def play():
    welcome()
    board(arr)
    moves = []  # List to store the sequence of moves and positions
    j = 0
    result = "Draw"  # Default result is draw

    for i in range(5):
        player1(moves)
        j += 1
        board(arr)
        win = winning(wins)
        if win:
            result = "Player 1 Wins"
            break
        if j >= 9:
            break

        player2(moves)
        j += 1
        board(arr)
        win = winning(wins)
        if win:
            result = "Player 2 Wins"
            break

    # Save game data
    save_game_data(moves, result)

    if result == "Draw":
        print("Match is drawn..")
    else:
        print(result)

# Start the game
if __name__=="__main__":
    
    play()
    
