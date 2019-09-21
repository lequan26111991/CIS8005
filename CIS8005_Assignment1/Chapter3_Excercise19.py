''' Chapter 3 Excercise 19 '''

from turtle import *
#Create inputs
x1,y1,x2,y2 = eval(input("Please enter the coordination of two points: "))

#Move to the first point and write down information
penup()
goto(x1,y1)
pendown()
write("("+str(x1)+","+str(y1)+")")

#Move line to second point
goto(x2,y2)
write("("+str(x2)+","+str(y2)+")")

#Pause
done()