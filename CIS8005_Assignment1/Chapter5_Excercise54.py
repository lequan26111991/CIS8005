'''Chapter 5 Excercise 54'''

from turtle import *
from math import *

#Draw x axis
penup()
backward(300)
pendown()
forward(600)

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
backward(300)
right(90)
pendown()
forward(300)
backward(600)
left(180)
write("Y")

#Draw y arrow
right(135)
forward(10)
backward(10)
left(270)
forward(10)
backward(10)
right(135)

#Draw function of y =x2
penup()
goto(-200,0)
color("red")
for x in range(-200,200): #Draw start from x = -200
    y = x * x / 200 #Scale down y to 1/200
    goto(x, y) #Draw function
    pendown()
    
done()
