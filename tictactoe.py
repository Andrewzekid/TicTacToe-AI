"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
import copy
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1

    if x_count == 0 and o_count == 0:
        #Board is empty
        return "X"
    else:
        #if there is the same number of X's as O's, its X's turn to move. Else, its O's turn to move
        return "X" if x_count <= o_count else "O"


# def check_O_or_X(cell):
#     """
#     Checks if there is an O or X in the cell provided
#     """
#     if cell == "O":
#         return False
#     elif cell == "X":
#         return True

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i,j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Find the player whose turn it is to make a move
    turn = player(board)

    #Create a deepcopy of the board
    newcopy = copy.deepcopy(board)

    #get the coordinates of the action
    i,j = action

    #See if the action is valid
    if newcopy[i][j] != None:
        #The cell is filled already
        raise Exception("%s,%s is already filled on the board! Please choose a different coordinate." % (i,j))
    else:
        #Assign the new value to the current cell
        newcopy[i][j] = turn
        return newcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # X O X
    # X X X
    # O O X
    for i in range(len(board)):
        #Check rows
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != None):
            #Winner amongst one of the rows
            return board[i][0]
        for j in range(len(board[i])):
            #Winner amongst one of the columns
            #Check columns
            if (board[0][j] == board[1][j] == board[2][j]) and (board[0][j] != None):
                return board[0][j]

    #Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != None):
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != None):
        return board[1][1]
    
    #NO Winner
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if not(board.count(None)):
        #There is atleast one or more unfilled square
    if winner(board):
        return True
    else:
        empty = [j for i in board for j in i if j == None]
        #No empty squares -> Game is over. Else, game is still ongoing
        return True if len(empty) == 0 else False
            



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == "X" else (-1 if winner(board) == "O" else 0)



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Find current player
    # TODO
    current_player = player(board)
    #list of [(i,j,max_value)]
    if terminal(board):
        #If there is no more possible actions
        return None

    elif current_player == "X":
        #Initialize the current maximum at a low value
        current_max = -10
        current_max_action = None
        #It is X's turn
        moves = actions(board)
        for move in moves:
            #return the maximum value of the move
            previous_max = current_max
            current_max = max(current_max,min_value(result(board,move)))
            if current_max > previous_max:
                #Current max has changed, so update the new best action
                current_max_action = move
        return current_max_action

    elif current_player == "O":
        #If it is O's turn
        current_min = 10
        current_min_action = None

        #Get all possible moves
        moves = actions(board)
        for move in moves:
            previous_min = current_min
            current_min = min(current_min,max_value(result(board,move)))

            if current_min < previous_min:
                #We have found a new optimal value
                current_min_action = move
        return current_min_action

            



def max_value(board):
    """
    Returns the maximum value for a given board
    """
    if terminal(board):
        #Game is over
        return utility(board)
    else:
        #Note: v is supposed to be set to -inf but i dont know how :'), so -10 will do
        v = -10
        for action in actions(board):
            v = max(v, min_value(result(board,action)))
        return v
    
def min_value(board):
    """
    Returns the minimum possible value for a given board
    """
    if terminal(board):
        return utility(board)
    else:
        #Note v is supposed to be set to inf but idk how so i will set it to 10
        v = 10
        for action in actions(board):
            v = min(v, max_value(result(board,action)))
        return v