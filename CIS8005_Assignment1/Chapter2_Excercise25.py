''' Chapter 2 Exercise 25 '''
from turtle import *
#Input the values for center, width, height
x,y,w,h = eval(input("Please enter the coordination of the center with width and height: "))
penup()
goto(x,y)

#Go to the bottom of rectangle
right(90)
forward(h/2)
pendown()

#Draw the 1/2 bottom width
left(90)
forward(w/2)

#Draw the first height
left(90)
forward(h)

#Draw the up width
left(90)
forward(w)

#Draw the second height
left(90)
forward(h)

#Draw the last 1/2 bottom
left(90)
forward(w/2)
