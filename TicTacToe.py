#TicTacToe game
import random
print("Welcome to Tic Tac Toe Game")

def drawBoard(board):
    print(board[1] + "      " + board[2] + "    " + board[3])
    print(board[4] + "      " + board[5] + "    " + board[6])
    print(board[7] + "      " + board[8] + "    " + board[9])

def initLetter():
    letter=''
    print("Do you want to be X or O")
    letter = input().upper()

    if letter == 'X':
        return['X','O']
    else:
        return['O','X']

def firstPlayerSelection():
    selectVal = random.randint(0,1)
    if selectVal == 0:
        return 'AI'
    else:
        return 'Player'

def makeMove(board,letter,move):
    board[move] = letter

def playAgain():
    print("Do you want to play again?")
    return input().lower().startswith('y')

def winningCriteria(board,letter):
    b = board
    l = letter
    return (
    (b[1] == b[2] == b[3] == l) or # First Row
    (b[4] == b[5] == b[6] == l) or # Second Row
    (b[7] == b[8] == b[9] == l) or # Third Row
    (b[1] == b[4] == b[7] == l) or # First Column
    (b[2] == b[5] == b[8] == l) or # Second Column
    (b[3] == b[6] == b[9] == l) or # Third Column
    (b[1] == b[5] == b[9] == l) or # Left Diagonal
    (b[3] == b[5] == b[7] == l)    # Right Diagonal
)

def isBoardFull():
    counter = [1,2,3,4,5,6,7,8,9]
    count = 0
    for i in counter:
        if b[i] == 'X' or b[i] == 'O':
            count = count + 1
    if count == 9:
        return True
    else:
        return False

def main():
    player,computer = initLetter()


main()
