''' Chapter 5 Excercise 53 '''

from turtle import *
from math import *

#Draw x axis
penup()
backward(500)
pendown()
forward(150)
write("2\u03C0")
pendown()
forward(540)
write("2\u03C0")
forward(300)
#Draw x arrow
right(135)
forward(10)
backward(10)
left(270)
forward(10)
backward(10)
right(135)

#Draw y axis
penup()
backward(490)
right(90)
pendown()
forward(400)
backward(800)
left(180)

#Draw y arrow
right(135)
forward(10)
backward(10)
left(270)
forward(10)
backward(10)
right(135)

#Draw Sine function
penup()
setpos(0,200)
goto(0,200)
color("red")

for angle in range(-450,450): #Start drawing from -450
    y = sin(radians(angle))        
    goto(angle, y * 200) #Draw function
    pendown()
    
#Draw Cosine function
penup()
setpos(0,200)
goto(0,200)
color("blue")

for angle in range(-450,450): #Start drawing from -450
    y = cos(radians(angle))       
    goto(angle, y * 200) #Draw function
    pendown()

    
done()
