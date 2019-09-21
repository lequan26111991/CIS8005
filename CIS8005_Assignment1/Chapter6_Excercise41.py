'''  Chapter 6 Excercise 41 '''

import turtle
import random
import math
# Draw a line from (x1, y1) to (x2, y2)

turtle.penup()
def drawLine(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a string s at the specified location (x, y)
def writeText(s, x, y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(s) # Write a string
# Draw a point at the specified location (x, y)
def drawPoint(x, y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(3)
    turtle.end_fill() # Fill the shape
# Draw a circle centered at (x, y) with the specified radius
def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Pull the pen down
    turtle.circle(radius)

# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def main():
    drawCircle(50,0,50) # Draw Circle
    count1 = 0
    while count1 < 10:
        x1 = random.randint(4,96) # Possible coordinate of x1 (already minus r = 3 of each dot) 
        y1 = random.randint(-46,46) # Possible coordinate of y1 (already minus r = 3 of each dot) 
        d1 = math.sqrt((x1-50)**2 + y1**2) #calculate the distance between center and random coordinator
        if(d1 < 50): #If distance smaller than radius of circle 
            drawPoint(x1, y1) # Draw point
            count1 +=1

    drawRectangle(-75,0,100,100)
    count2 = 0
    while count2 < 10:
        x2 = random.randint(-121,-21) # Possible coordinate of x2 (already minus r = 3 of each dot) 
        y2 = random.randint(-46,46) # Possible coordinate of y2 (already minus r = 3 of each dot) 
        d2 = math.sqrt((x2+75)**2 + y2**2) #calculate the distance between center and random coordinator
        if(d2 < 50): #If distance smaller than radius of circle inside retangle
            drawPoint(x2, y2) # Draw point
            count2 +=1

main()
