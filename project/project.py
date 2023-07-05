import random

# Global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def main():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        winCheck()
        tieCheck(board)
        switchPlayer()
        computer(board)
        winCheck()
        tieCheck(board)


# Print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Take user input
def playerInput(board):
    userInput = int(input("Choose a number 1-9: "))
    if userInput >= 1 and userInput <= 9 and board[userInput-1] == "-":
        board[userInput-1] = currentPlayer
    else:
        print("Invalid input")

# Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Check win or tie
def horizontalCheck(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True

def verticalCheck(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True


def diagonalCheck(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def tieCheck(board):
    global gameRunning
    if "-" not in board and(horizontalCheck(board) or verticalCheck(board) or diagonalCheck(board) != True):
        print("It's a tie!")
        printBoard(board)
        gameRunning = False


def winCheck():
    global gameRunning
    if horizontalCheck(board) or verticalCheck(board) or diagonalCheck(board) == True:
        print(f"The winner is {winner}")
        printBoard(board)
        gameRunning = False


# computer bot
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


if __name__ == "__main__":
    main()