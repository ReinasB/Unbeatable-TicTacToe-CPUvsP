import numpy as np

simulations = 0
def printBoard():
    for row in range(3):
        print(boardLines)
        for col in range(3):
            if col < 2:
                print(f" {gameboard[row][col]} |", end='')
            else:
                print(f" {gameboard[row][col]} ")
        if row < 2:
            print(boardLines)
            print("-----------")
    print(boardLines)

def isMovesLeft(board) : 

	for i in range(3) : 
		for j in range(3) : 
			if (board[i][j] != 'X' and board[i][j] != 'O') : 
				return True
	return False

def checkWin(b):
	
	# Checking for Rows for X or O victory. 
	for row in range(3) :	 
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :		 
			if (b[row][0] == 'X') : 
				return 10
			elif (b[row][0] == 'O') : 
				return -10

	# Checking for Columns for X or O victory. 
	for col in range(3) : 
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) : 
		
			if (b[0][col] == 'X') : 
				return 10
			elif (b[0][col] == 'O') : 
				return -10

	# Checking for Diagonals for X or O victory. 
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) : 
	
		if (b[0][0] == 'X') : 
			return 10
		elif (b[0][0] == 'O') : 
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) : 
	
		if (b[0][2] == 'X') : 
			return 10
		elif (b[0][2] == 'O') : 
			return -10

	# Else if none of them have won then return 0 
	return 0  

#def invalidInput(board):
    #newMove = input("Enter your move number: ")
    #move(newMove,True,board)

def algo(board,depth,ComputerNeedsMax):
	global simulations
	score = checkWin(board)
	simulations+=1
	if(score == 10):
		return score
	if(score == -10):
		return score
	if(isMovesLeft(board) == False):
		return 0
	if(ComputerNeedsMax == True):
		best = -1000
		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = computer
					best = max(best,algo(board,depth+1,not ComputerNeedsMax))
					board[i][j] = temp
		return best
	else:
		best = 1000

		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = player
					best = min(best,algo(board,depth+1,not ComputerNeedsMax))
					board[i][j] = temp
		return best
	
def algoF(board,depth,ComputerNeedsMax):
	global simulations
	score = checkWin(board)
	simulations+=1

	if(score == 10):
		return score
	if(score == -10):
		return score
	if(isMovesLeft(board) == False):
		return 0
	if(ComputerNeedsMax == True):
		best = -1000
		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = player
					best = max(best,algoF(board,depth+1,not ComputerNeedsMax))
					board[i][j] = temp
		return best
	else:
		best = 1000

		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = computer
					best = min(best,algoF(board,depth+1,not ComputerNeedsMax))
					board[i][j] = temp
		return best




def findBestMove(board):
	global simulations
	simulations = 0
	if(computer == "X"):
		Value = -1000
		bestMove = (-1,-1)
		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = computer
					moveValue = algo(board,0,False)
					board[i][j] = temp
					if(moveValue > Value):
						bestMove = (i,j)
						Value = moveValue
	else:
		Value = 1000
		bestMove = (-1,-1)
		for i in range(3):
			for j in range(3):
				if(board[i][j] != "X" and board[i][j] != "O"):
					temp = board[i][j]
					board[i][j] = computer
					moveValue = algoF(board,0,True)
					board[i][j] = temp
					if(moveValue < Value):
						bestMove = (i,j)
						Value = moveValue
	print(f"The CPU found {simulations} possible game states, this is the best one:")
	return bestMove

def winner(won):
	if(won == True):
		print("Human is winner, not good...")
	else:
		print("~~~~~Computer is superior~~~~~")

def draw():
	print("~~~~~Draw Game~~~~~")

def move(whosGo,ComputerMove,board):
	if(whosGo == True):
		if(player == "X"):
			printBoard()
			Cmove = input("Enter your move number: ")
			row = int((int(Cmove)-1)/3)
			col = int((int(Cmove)-1)% 3)
			if(board[row][col] != "X" and board[row][col] != "O"):
				board[row][col] = "X"
				print("Your move:")
				printBoard()
				check = checkWin(board)
				if(check == 10):
					winner(True)
				elif(isMovesLeft(board) == False):
					draw()
				else:
					move(not whosGo,not ComputerMove,board)
			else:
				print("Incorrect move")
				move(whosGo,ComputerMove,board)
		#Computer is X computer needs high score
		else:
			print("Computer is moving...")
			moved = findBestMove(board)
			i = moved[0]
			j = moved[1]
			board[i][j] = "X"
			check = checkWin(board)
			if(check == 10):
				printBoard()
				winner(False)
			elif(isMovesLeft(board) == False):
				draw()
			else:
				move(not whosGo,not ComputerMove,board)
	else:
		if(player == "O"):
			printBoard()
			Cmove = input("Enter your move number:")
			row = int((int(Cmove)-1)/3)
			col = int((int(Cmove)-1)% 3)
			if(board[row][col] != "X" and board[row][col] != "O"):
				board[row][col] = "O"
				print("Your move:")
				printBoard()
				check = checkWin(board)
				if(check == -10):
					winner(True)
				elif(isMovesLeft(board) == False):
					draw()
				else:
					move(not whosGo,not ComputerMove,board)
			else:
				print("Incorrect move")
				move(whosGo,ComputerMove,board)
		else:
			print("Computer is moving...")
			moved = findBestMove(board)
			i = moved[0]
			j = moved[1]
			board[i][j] = "O"
			check = checkWin(board)
			if(check == -10):
				printBoard()
				winner(False)
			elif(isMovesLeft(board) == False):
				draw()
			else:
				move(not whosGo,not ComputerMove,board)

#Initialize the Tic Tac Toe board
boardLines = "   |   |   "
gameboard = np.array([['1','2','3'],
                      ['4','5','6'],
                      ['7','8','9']])
player = input("Do you want to play as X or O? ").lower()
if player == "x":
	player = "X"
	computer = "O"
	move(True,False,gameboard)
else:
	print("Computer is X")
	player = "O"
	computer = "X"
	move(True,True,gameboard)
