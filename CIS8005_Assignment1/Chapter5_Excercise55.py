'''Chapter 5 Excercise 55 '''

from turtle import *
 
def box(x,y,size,fill_color): #drawbox
    penup() 
    goto(x,y) 
    pendown() 
    fillcolor(fill_color)
    begin_fill()  # Start filling color
 
    for i in range(0,4):
        forward(size) 
        right(90) 
 
    end_fill() # Fill square
 
 
def chess_board():
    color = "black" # first square is black
    x = 0 
    y = 0 
    size = 30 #size of each square
    for i in range(1,9): 
        for j in range(1,9):
            box(x + j * size, y + i * size, size, color)
            
            if color == 'white': # switch after a column
               color = 'black' 
            else: 
               color = 'white' 
            
        if color == 'white': # switch after a row
           color = 'black' 
        else: 
           color = 'white'
 
 

chess_board()
done()
