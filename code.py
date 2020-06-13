import numpy as npy

def getboard(row,col):
    board=npy.zeros((row,col))
    return board

def valid_location(board,input):
    return board[5][int(input)] == 0

def add_piece_to_board(board,input,player):
    row=0
    while board[int(row)][int(input)] != 0:
        row=row+1
    board[int(row)][int(input)]=player
    return int(row)

def check_if_won(board,temprow,tempcol):
    row=int(temprow)
    col=int(tempcol)
    if row-3>=0 and board[row][col]==board[row-1][col] and board[row][col]==board[row-2][col] and board[row][col]==board[row-3][col]:
        return True
    
    elif col-3>=0 and board[row][col]==board[row][col-1] and board[row][col]==board[row][col-2] and board[row][col]==board[row][col-3]:
        return True
    
    elif col+3<=6 and board[row][col]==board[row][col+1] and board[row][col]==board[row][col+2] and board[row][col]==board[row][col+3]:
        return True
    
    elif row-3>=0 and col-3>=0 and board[row][col]==board[row-1][col-1] and board[row][col]==board[row-2][col-2] and board[row][col]==board[row-3][col-3]:
        return True
    
    elif row-3>=0 and col+3<=6 and board[row][col]==board[row-1][col+1] and board[row][col]==board[row-2][col+2] and board[row][col]==board[row-3][col+3]:
        return True

    elif row+3<=5 and col-3>=0 and board[row][col]==board[row+1][col-1] and board[row][col]==board[row+2][col-2] and board[row][col]==board[row+3][col-3]:
        return True
    
    elif row+3<=5 and col+3<=6 and board[row][col]==board[row+1][col+1] and board[row][col]==board[row+2][col+2] and board[row][col]==board[row+3][col+3]:
        return True

    return False
    

board = getboard(6,7)
someone_won = False
turn = 1

while not someone_won:
    if turn == 1:
        user_input=input("Ask Player 1 to make selection (between 0-6): ")
        print(user_input)

        if valid_location(board,user_input):
            row=add_piece_to_board(board,user_input,1)
            if check_if_won(board,row,user_input):
                print("Player 1 Won!!")
                someone_won=True


    else:
        user_input=input("Ask Player 2 to make selection (between 0-6): ")
        print(user_input)

        if valid_location(board,user_input):
            row=add_piece_to_board(board,user_input,2)
            if check_if_won(board,row,user_input):
                print("Player 2 Won!!")
                someone_won=True

    print(npy.flip(board,0))

    if turn == 1:
        turn=2
    else:
        turn=1