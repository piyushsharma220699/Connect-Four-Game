# PIYUSH SHARMA
# 4 CONNECT GAME
import numpy as npy
import pygame
import sys
import math
from pygame import mixer
from sys import exit
from pygame.locals import *
import random

ROWLENGTH=6
COLUMNLENGTH=8
LENGTHOFBOX=100
STARTGAME=False

def getboard(row,col):
    board=npy.zeros((row,col))
    return board

pygame.init()
pygame.display.set_caption("Let's 4 Connect")
icon=pygame.image.load('logo.png')
pygame.display.set_icon(icon)
height=(ROWLENGTH+1)*LENGTHOFBOX
width=(COLUMNLENGTH)*LENGTHOFBOX
size=(width,height)
screen=pygame.display.set_mode(size)
font=pygame.font.SysFont("comicsansms", 60)
smallfont=pygame.font.SysFont("comicsansms", 35)


def introduction(startgame):
    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            pygame.draw.rect(screen,(0,0,0),(col*LENGTHOFBOX,row*LENGTHOFBOX, (col+1)*LENGTHOFBOX, (row+1)*LENGTHOFBOX))
    
    label=font.render("LET'S PLAY 4 CONNECT",1,(0,0,255))
    text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
    screen.blit(label, text_rect)
    pygame.display.update()
    runit=True
    while runit:
        pygame.draw.rect(screen,(0,255,0),(200,150,400,100))
        pygame.draw.rect(screen,(0,255,0),(200,350,400,100))
        pygame.draw.rect(screen,(255,0,0),(200,550,400,100))
        mouse=pygame.mouse.get_pos()
        
        if 200+400>mouse[0]>200 and 150+100>mouse[1]>150:
            pygame.draw.rect(screen,(0,255,220),(200,150,400,100))
        if 200+400>mouse[0]>200 and 350+100>mouse[1]>350:
            pygame.draw.rect(screen,(0,255,220),(200,350,400,100))
        if 200+400>mouse[0]>200 and 550+100>mouse[1]>550:
            pygame.draw.rect(screen,(255,0,220),(200,550,400,100))
        
        label=smallfont.render("1 PLAYER",1,(0,0,0))
        text_rect=label.get_rect(center=(400,200))
        screen.blit(label, text_rect)
        label2=smallfont.render("2 PLAYER",1,(0,0,0))
        text_rect2=label2.get_rect(center=(400,400))
        screen.blit(label2, text_rect2)
        label3=smallfont.render("QUIT",1,(0,0,0))
        text_rect3=label3.get_rect(center=(400,600))
        screen.blit(label3, text_rect3)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                runit=False

            if event.type==MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if 200+400>mouse[0]>200 and 150+100>mouse[1]>150:
                    looponeplayer()
                    runit=False
                if 200+400>mouse[0]>200 and 350+100>mouse[1]>350:
                    startgame=True
                    runit=False
                    pygame.time.wait(200)
                if 200+400>mouse[0]>200 and 550+100>mouse[1]>550:
                    runit=False

        pygame.display.update()

    return startgame

def valid_location(board,input):
    return board[ROWLENGTH-1][int(input)] == 0

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
    while num<=3 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row][col+index]:
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
    while num<=3 and row+index<=ROWLENGTH-1 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row+index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True
    
    index=1
    num=1
    while num<=3 and row+index<=ROWLENGTH-1 and col-index>=0 and board[row][col]==board[row+index][col-index]:
        num=num+1
        index=index+1
    
    index=1
    while num<=3 and row-index>=0 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row-index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True

    return False
    
def draw_board(board):
    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            pygame.draw.rect(screen,(0,0,255),(col*LENGTHOFBOX,(row+1)*LENGTHOFBOX, (col+1)*LENGTHOFBOX, (row+2)*LENGTHOFBOX)) 
            pygame.draw.circle(screen,(0,0,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))

    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            if(board[row][col]==1):
                pygame.draw.circle(screen,(255,0,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((ROWLENGTH+1)*LENGTHOFBOX-(row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))
            elif(board[row][col]==2):
                pygame.draw.circle(screen,(0,255,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((ROWLENGTH+1)*LENGTHOFBOX-(row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))
    
    pygame.display.update()

def loopit(height,width,endgame):
    board = getboard(ROWLENGTH,COLUMNLENGTH)
    draw_board(board)
    pygame.display.update()
    mixer.music.load('startsound.ogg')
    mixer.music.play()
    someone_won=False
    turn=1
    while not someone_won:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                endgame=True
                return endgame
            
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                position=event.pos[0]
                if turn == 1:
                    pygame.draw.circle(screen,(255,0,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
                elif turn == 2:
                    pygame.draw.circle(screen,(0,255,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
            
            pygame.display.update()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if turn == 1:
                    position=event.pos[0]
                    user_input=int(math.floor(position/LENGTHOFBOX))

                    if valid_location(board,user_input):
                        row=add_piece_to_board(board,user_input,1)
                        mixer.music.load('insertsound.wav')
                        mixer.music.play()
                        if check_if_won(board,row,user_input):
                            pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                            label=font.render("PLAYER 1 WINS!!!",1,(255,0,0))
                            text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
                            screen.blit(label, text_rect)
                            someone_won=True


                else:
                    position=event.pos[0]
                    user_input=int(math.floor(position/LENGTHOFBOX))

                    if valid_location(board,user_input):
                        row=add_piece_to_board(board,user_input,2)
                        mixer.music.load('insertsound.wav')
                        mixer.music.play()
                        if check_if_won(board,row,user_input):
                            pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                            label=font.render("PLAYER 2 WINS!!!",1,(0,255,0))
                            text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
                            screen.blit(label, text_rect)
                            someone_won=True

                draw_board(board)
                

                if turn == 1:
                    turn=2
                else:
                    turn=1
                
                if someone_won:
                    mixer.music.load('winsound.mp3')
                    mixer.music.play()
                    pygame.time.wait(5000)


def looponeplayer():
    board = getboard(ROWLENGTH,COLUMNLENGTH)
    draw_board(board)
    pygame.display.update()
    mixer.music.load('startsound.ogg')
    mixer.music.play()
    someone_won=False
    turn=1
    while not someone_won:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                endgame=True
                return endgame
            
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                position=event.pos[0]
                if turn == 1:
                    pygame.draw.circle(screen,(255,0,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
                elif turn == 2:
                    pygame.draw.circle(screen,(0,255,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
            
            pygame.display.update()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if turn == 1:
                    position=event.pos[0]
                    user_input=int(math.floor(position/LENGTHOFBOX))

                    if valid_location(board,user_input):
                        row=add_piece_to_board(board,user_input,1)
                        mixer.music.load('insertsound.wav')
                        mixer.music.play()
                        if check_if_won(board,row,user_input):
                            pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                            label=font.render("PLAYER 1 WINS!!!",1,(255,0,0))
                            text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
                            screen.blit(label, text_rect)
                            someone_won=True
                        
                    if turn == 1:
                        turn=2
                    else:
                        turn=1
                    draw_board(board)
                    pygame.display.update()


        if turn==2 and not someone_won:
            pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
            pygame.display.update()
            col=random.randint(0,COLUMNLENGTH-1)
            if valid_location(board,col):
                pygame.time.wait(1000)
                row=add_piece_to_board(board,col,2)
                mixer.music.load('insertsound.wav')
                mixer.music.play()
                if check_if_won(board,row,col):
                    pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                    label=font.render("COMPUTER WINS!!!",1,(0,255,0))
                    text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
                    screen.blit(label, text_rect)
                    someone_won=True

                draw_board(board)        
                if turn == 1:
                    turn=2
                else:
                    turn=1
        
        if someone_won:
            mixer.music.load('winsound.mp3')
            mixer.music.play()
            pygame.time.wait(5000)
        
    restartgamewithAI()



# def score_position(board,piece):
#     score=0
#     for row in range(ROWLENGTH):
#         row_array=[int(i) for i in list(board[row,:])]
#         for col in range(COLUMNLENGTH-3):
#             window=row_array[col:col+WINDOW_LENGTH]

#             if window.count(piece)==4:
#                 score+=100
#             elif window.count(piece)==3 and window.count(EMPTY)==1:
#                 score+=10
    
#     for col in range(COLUMNLENGTH):
#         col_array=[int(i) for i in list(board[col,:])]
#         for col in range(ROWLENGTH-3):
#             window=col_array[row:row+WINDOW_LENGTH]

#             if window.count(piece)==4:
#                 score+=100
#             elif window.count(piece)==3 and window.count(EMPTY)==1:
#                 score+=10
    
#     return score

# def alphabetapruning(board,depth,alpha,beta,maximizingplayer)
# {
#     if 

#     if maximizingplayer:
#         value= -math.inf
#         for i=0 to board[0].size():
#             if valid_location(board,i):
#                 board_copy=board.copy()
#                 add_piece_to_board(board,i,AI)
#                 new_score=alphabetapruning(board_copy,depth-1,alpha,beta,False)[1]
#                 if new_score>value:
#                     value=new_score
#                     column=col
#                 alpha=max(alpha,value)
#                 if alpha>=beta:
#                     break    
#         return column,value
    
#     else:
#         value=math.inf
#         for i=0 to board[0].size():
#             if valid_loaction(board,i):
#                 board_copy=board.copy()
#                 add_piece_to_board(board,i,PLAYER)
#                 new_score=alphabetapruning(board_copy,depth-1,alpha,beta,True)[1]
#                 if new_score<value:
#                     value=new_score
#                     column=col
#                 beta=min(beta,value)
#                 if alpha>=beta:
#                     break    
#         return column,value
# }

def restartgame(restart):
    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            pygame.draw.rect(screen,(0,0,0),(col*LENGTHOFBOX,row*LENGTHOFBOX, (col+1)*LENGTHOFBOX, (row+1)*LENGTHOFBOX))
    
    label=font.render("PLAY AGAIN?",1,(0,0,255))
    text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
    screen.blit(label, text_rect)
    pygame.display.update()
    runit=True
    while runit:
        pygame.draw.rect(screen,(0,255,0),(200,200,400,100))
        pygame.draw.rect(screen,(255,0,0),(200,400,400,100))
        mouse=pygame.mouse.get_pos()
        if 200+400>mouse[0]>200 and 200+100>mouse[1]>200:
            pygame.draw.rect(screen,(0,255,220),(200,200,400,100))
        if 200+400>mouse[0]>200 and 400+100>mouse[1]>400:
            pygame.draw.rect(screen,(255,0,220),(200,400,400,100))
        label=smallfont.render("RESTART",1,(0,0,0))
        text_rect=label.get_rect(center=(400,250))
        screen.blit(label, text_rect)
        label2=smallfont.render("QUIT",1,(0,0,0))
        text_rect2=label2.get_rect(center=(400,450))
        screen.blit(label2, text_rect2)        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                runit=False

            if event.type==MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if 200+400>mouse[0]>200 and 200+100>mouse[1]>200:
                    restart=True
                    runit=False
                if 200+400>mouse[0]>200 and 400+100>mouse[1]>400:
                    runit=False

        pygame.display.update()
                    
    return restart


def restartgamewithAI():
    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            pygame.draw.rect(screen,(0,0,0),(col*LENGTHOFBOX,row*LENGTHOFBOX, (col+1)*LENGTHOFBOX, (row+1)*LENGTHOFBOX))
    
    label=font.render("PLAY AGAIN?",1,(0,0,255))
    text_rect=label.get_rect(center=(int((COLUMNLENGTH*LENGTHOFBOX)/2), int(LENGTHOFBOX/2)))
    screen.blit(label, text_rect)
    pygame.display.update()
    runit=True
    while runit:
        pygame.draw.rect(screen,(0,255,0),(200,200,400,100))
        pygame.draw.rect(screen,(255,0,0),(200,400,400,100))
        mouse=pygame.mouse.get_pos()
        if 200+400>mouse[0]>200 and 200+100>mouse[1]>200:
            pygame.draw.rect(screen,(0,255,220),(200,200,400,100))
        if 200+400>mouse[0]>200 and 400+100>mouse[1]>400:
            pygame.draw.rect(screen,(255,0,220),(200,400,400,100))
        label=smallfont.render("RESTART",1,(0,0,0))
        text_rect=label.get_rect(center=(400,250))
        screen.blit(label, text_rect)
        label2=smallfont.render("QUIT",1,(0,0,0))
        text_rect2=label2.get_rect(center=(400,450))
        screen.blit(label2, text_rect2)        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                runit=False

            if event.type==MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if 200+400>mouse[0]>200 and 200+100>mouse[1]>200:
                    looponeplayer()
                    runit=False
                if 200+400>mouse[0]>200 and 400+100>mouse[1]>400:
                    runit=False

        pygame.display.update()



startgame=introduction(False)

while startgame:
    endgame=loopit(height,width,False)
    if endgame:
        break
    else:    
        startgame=restartgame(False)
