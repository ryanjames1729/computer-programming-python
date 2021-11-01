# CDS - Programming
# Caesar Cipher Assignment
#
# Student Name:

import os, time

board = []  # this is a list
playerTurn = "X"

# This function should create a 3x3 board filled with dashes
def createBoard():
  global board
  row1 = ["-", "-", "-"]
  row2 = ["-", "-", "-"]
  row3 = ["-", "-", "-"]
  board = [row1, row2, row3]
  #pass

# This function should print the rows and columns of the board
def printBoard():
  global board
  for i in range(3):
    print("{} | {} | {}".format(board[i][0], board[i][1], board[i][2]))
    if i < 2:
      print("---------")
  #pass


# This function should determine if the board has an open spot at the given row and column value
def checkOpen(r, c):
  
  return True

# This function should switch the player turn to X or O depending on the current player
def switchTurn():
  global playerTurn
  
  pass

# This function should check if any rows have 3 in a row
def checkRows():
  global board
  
  return False

# This function should check if any columns have 3 in a row
def checkColumns():
  global board
  
  return False


# This function should check if any diagonals have 3 in a row
def checkDiagonals():
  global board
  
  return False

# This function is complete - don't change it
def checkForWin():
  
  return False

def boardFull():
  
  return True

createBoard()


while not boardFull() and not checkForWin():
  os.system('clear')
  printBoard()
  move = input("Pick a square to play. Type your answer as a coordinate (row,column): ")
  time.sleep(0.5)

  