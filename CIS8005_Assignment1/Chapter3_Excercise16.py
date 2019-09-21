''' Chapter 3 Excercise 16 '''

from turtle import *

pensize(3) 
penup() 
goto(-200, -50)
pendown() 

'''Draw a Triangle '''
right(60)
circle(40, steps = 3) 

'''Draw a Square '''
left(15)
penup()
goto(-100, -50)
pendown()
begin_fill() 
color("blue")
circle(40, steps = 4) 
end_fill() 

'''Draw a pentagon'''
left(9)
penup()
goto(0, -50)
pendown()
begin_fill() 
color("green")
circle(40, steps = 5) 
end_fill() 

'''Draw a hexagon'''
left(7)
penup()
goto(100, -50)
pendown()
begin_fill() 
color("yellow")
circle(40, steps = 6) 
end_fill() 

'''Draw a octagon'''
penup()
goto(200, -50)
pendown()
begin_fill() 
color("purple")

'''Draw a circle'''
circle(40) 
end_fill() 
color("green")

''' Draw Words'''
penup()
goto(-100, 50)
pendown()
write("Cool Colorful Shapes", font = ("Times", 18, "bold"))

done()

