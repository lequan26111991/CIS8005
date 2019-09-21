
''' Chapter 1 Excercise 21 '''

from turtle import *
#Draw all clock's needles
forward(200)
right(180)
forward(350)
right(180)
forward(150)
left(90)
forward(250)

#Draw Circle
penup()
right(180)
forward(650)
left(90)
pendown()
circle(400)

#Draw current hour
penup()
right(90)
forward(20)
pendown()
write("9:15:00")

#Draw 6
penup()
right(180)
forward(40)
pendown()
write("6")

#Draw 12
penup()
forward(760)
pendown()
write("12")

#Draw 3
penup()
right(180)
forward(380)
left(90)
forward(380)
pendown()
write("3")

#Draw 9
penup()
right(180)
forward(760)
pendown()
write("9")

#Pause
done()
