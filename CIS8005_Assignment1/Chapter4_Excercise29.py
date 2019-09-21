'''Chapter 4 Excercise29'''

from math import *

#input values
x1,y1,r1 = eval(input("Enter circle1\'s center x-, y-coordinates, and radius: "))
x2,y2,r2 = eval(input("Enter circle2\'s center x-, y-coordinates, and radius: "))

#calculate the center distance
cdistance = sqrt((x2-x1)**2 + (y2-y1)**2 )

#Check if circle 2 is overlapped, not overlapped or inside circle 1
if cdistance <= sqrt((r1-r2)**2):
    print("circle2 is inside circle1")
elif cdistance <= r1 +r2:       
    print("circle2 overlaps circle1")
else:    
    print("circle2 does not overlap circle1")