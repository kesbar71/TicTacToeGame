# A Simple Tic-Tac-Toe game in Python
# Author: Keshav Barker
# Date: 2023-08-09
# Version: 1.0
# Description: A simple Tic-Tac-Toe game in Python
# Usage: python TTT.py
# Notes: skill building exercise    

# Import modules
import random
import sys
import os

# Define global variables
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = ''
computer = ''
turn = ''
winner = ''
gameOver = False

# Define functions
def drawBoard():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def chooseLetter():
    global player, computer
    letter = ''
    while letter != 'X' and letter != 'O':
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        player = 'X'
        computer = 'O'
    else:
        player = 'O'
        computer = 'X'
    print('You chose ' + player + '. The computer will be ' + computer + '.')
    return player, computer

def whoGoesFirst():
    global turn
    if random.randint(0, 1) == 0:
        turn = 'computer'
    else:
        turn = 'player'
    print('The ' + turn + ' will go first.')
    return turn

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or # Across the top
    (board[3] == letter and board[4] == letter and board[5] == letter) or # Across the middle
    (board[6] == letter and board[7] == letter and board[8] == letter) or # Across the bottom
    (board[0] == letter and board[3] == letter and board[6] == letter) or # Down the left side
    (board[1] == letter and board[4] == letter and board[7] == letter) or # Down the middle
    (board[2] == letter and board[5] == letter and board[8] == letter) or # Down the right side
    (board[0] == letter and board[4] == letter and board[8] == letter) or # Diagonal
    (board[2] == letter and board[4] == letter and board[6] == letter)) # Diagonal

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ''
    while move not in '0 1 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (0-8)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
        
def getComputerMove(board, computer):
    if computer == 'X':
        player = 'O'
    else:
        player = 'X'

    # Check if computer can win in the next move
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer, i)
            if isWinner(copy, computer):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, player, i)
            if isWinner(copy, player):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 4):
        return 4

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [1, 3, 5, 7])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# Main program
print('You suck at Tic-Tac-Toe! Let\'s prove it!')

while True:
    # Reset the board
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player, computer = chooseLetter()
    turn = whoGoesFirst()
    gameOver = False

    while not gameOver:
        if turn == 'player':
            # Player's turn
            drawBoard()
            move = getPlayerMove(board)
            makeMove(board, player, move)

            if isWinner(board, player):
                drawBoard()
                print('You won! You\'re not as bad as I thought!')
                gameOver = True
            else:
                if isBoardFull(board):
                    drawBoard()
                    print('The game is a tie. You\'re still not as bad as I thought.')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn
            move = getComputerMove(board, computer)
            makeMove(board, computer, move)

            if isWinner(board, computer):
                drawBoard()
                print('I won! You suck!')
                gameOver = True
            else:
                if isBoardFull(board):
                    drawBoard()
                    print('The game is a tie. You\'re still not as bad as I thought.')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

# End of program