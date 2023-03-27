import random

# function to create an empty board
def create_board():
    board = [[0] * 4 for i in range(4)]
    return board

# function to add a new tile to the board
def add_new_tile(board):
    row, col = random.randint(0, 3), random.randint(0, 3)
    while board[row][col] != 0:
        row, col = random.randint(0, 3), random.randint(0, 3)
    board[row][col] = 2

# function to print the board
def print_board(board):
    for row in board:
        print(row)

# function to check if the game is over
def is_game_over(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return False
            if col < 3 and board[row][col] == board[row][col + 1]:
                return False
            if row < 3 and board[row][col] == board[row + 1][col]:
                return False
    return True

# function to move tiles left
def move_left(board):
    for row in range(4):
        # merge tiles
        for col in range(3):
            if board[row][col] != 0 and board[row][col] == board[row][col + 1]:
                board[row][col] *= 2
                board[row][col + 1] = 0
        # move tiles
        for col in range(4):
            if board[row][col] == 0:
                for k in range(col + 1, 4):
                    if board[row][k] != 0:
                        board[row][col] = board[row][k]
                        board[row][k] = 0

# function to move tiles right
def move_right(board):
    for row in range(4):
        # merge tiles
        for col in range(3, 0, -1):
            if board[row][col] != 0 and board[row][col] == board[row][col - 1]:
                board[row][col] *= 2
                board[row][col - 1] = 0
        # move tiles
        for col in range(3, -1, -1):
            if board[row][col] == 0:
                for k in range(col - 1, -1, -1):
                    if board[row][k] != 0:
                        board[row][col] = board[row][k]
                        board[row][k] = 0

# function to move tiles up
def move_up(board):
    for col in range(4):
        # merge tiles
        for row in range(3):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col]:
                board[row][col] *= 2
                board[row + 1][col] = 0
        # move tiles
        for row in range(4):
            if board[row][col] == 0:
                for k in range(row + 1, 4):
                    if board[k][col] != 0:
                        board[row][col] = board[k][col]
                        board[k][col] = 0

# function to move tiles down
def move_down(board):
    for col in range(4):
        # merge tiles
        for row in range(3, 0, -1):
            if board[row][ col] != 0 and board[row][col] == board[row - 1][col]:
                board[row][col] *= 2
                board[row - 1][col] = 0
    # move tiles
    for row in range(3, -1, -1):
        if board[row][col] == 0:
            for k in range(row - 1, -1, -1):
                if board[k][col] != 0:
                    board[row][col] = board[k][col]
                    board[k][col] = 0


# main game loop
def play_game():
    board = create_board()
    add_new_tile(board)
    add_new_tile(board)
    while True:
        print_board(board)
        move = input("Enter move (left, right, up, down) or 'q' to quit: ")
        if move == "q":
            print("Thanks for playing!")
            break
        elif move in ["left", "right", "up", "down"]:
            if move == "left":
                move_left(board)
            elif move == "right":
                move_right(board)
            elif move == "up":
                move_up(board)
            elif move == "down":
                move_down(board)
            if is_game_over(board):
                print_board(board)
                print("Game over!")
                break
            else:
                add_new_tile(board)
        else:
            print("Invalid input. Please enter 'left', 'right', 'up', 'down', or 'q' to quit.")

# start the game
play_game()
