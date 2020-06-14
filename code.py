import numpy as npy
import pygame
import sys
import math

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
    
    index=1
    num=1
    while num<=3 and index<=3 and col-index>=0 and board[row][col]==board[row][col-index]:
        num=num+1
        index=index+1
    
    index=1
    while num<=3 and col+index<=6 and board[row][col]==board[row][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True
    
    index=1
    num=1
    while num<=3 and row-index>=0 and col-index>=0 and board[row][col]==board[row-index][col-index]:
        num=num+1
        index=index+1

    index=1
    while num<=3 and row+index<=5 and col+index<=6 and board[row][col]==board[row+index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True
    
    index=1
    num=1
    while num<=3 and row+index<=5 and col-index>=0 and board[row][col]==board[row+index][col-index]:
        num=num+1
        index=index+1
    
    index=1
    while num<=3 and row-index>=0 and col+index<=6 and board[row][col]==board[row-index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True

    return False
    
def draw_board(board):
    for r in range(6):
        for c in range(7):
            pygame.draw.rect(screen,(0,0,255),(c*100,(r+1)*100, 100, 100)) 
            pygame.draw.circle(screen,(0,0,0),(c*100+50,(r+1)*100+50),45)

    for r in range(6):
        for c in range(7):
            if(board[r][c]==1):
                pygame.draw.circle(screen,(255,0,0),(c*100+50,700-(r+1)*100+50),45)
            elif(board[r][c]==2):
                pygame.draw.circle(screen,(0,255,0),(c*100+50,700-(r+1)*100+50),45)
    
    pygame.display.update()

board = getboard(6,7)
someone_won = False
turn = 1

pygame.init()
height=700
width=700
size=(width,height)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font=pygame.font.SysFont("comicsansms", 80)

while not someone_won:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
        
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,(0,0,0),(0,0,700,100))
            position=event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen,(255,0,0),(position,50),50)
            elif turn == 2:
                pygame.draw.circle(screen,(0,255,0),(position,50),50)
        
        pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if turn == 1:
                position=event.pos[0]
                user_input=int(math.floor(position/100))

                if valid_location(board,user_input):
                    row=add_piece_to_board(board,user_input,1)
                    if check_if_won(board,row,user_input):
                        pygame.draw.rect(screen,(0,0,0),(0,0,700,100))
                        label=font.render("PLAYER 1 WINS",1,(255,0,0))
                        screen.blit(label, (30,10))
                        someone_won=True


            else:
                position=event.pos[0]
                user_input=int(math.floor(position/100))

                if valid_location(board,user_input):
                    row=add_piece_to_board(board,user_input,2)
                    if check_if_won(board,row,user_input):
                        pygame.draw.rect(screen,(0,0,0),(0,0,700,100))
                        label=font.render("PLAYER 2 WINS",1,(0,255,0))
                        screen.blit(label, (30,10))
                        someone_won=True

            draw_board(board)

            if turn == 1:
                turn=2
            else:
                turn=1
        
    if someone_won:
        pygame.time.wait(5000)
