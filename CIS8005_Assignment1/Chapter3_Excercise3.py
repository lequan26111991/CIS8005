''' Chapter 3 Exercise 3 '''

from math import *
#Atlanta location of Zip 30303
x1 = radians(-84.3920200)
y1 = radians(33.7524500)
#Orlando location of Zip 32803
x2 = radians(-81.3366300)
y2 = radians(28.5566962)
#Savannah location of Zip 31418
x3 = radians(-81.0715600)
y3 = radians(31.9713900)
#Charlotte location of zip 28214
x4 = radians(-80.8958503)
y4 = radians(35.2875069)

# Earth radius
radius = 6371.01

# Distance from Atlanta to Orlando
d1 = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
# Distance from Atlanta to Savannah
d2 = radius * acos(sin(x1) * sin(x3) + cos(x1) * cos(x3) * cos(y1 - y3))
# Distance from Savannah to Orlando
d3 = radius * acos(sin(x3) * sin(x2) + cos(x3) * cos(x2) * cos(y3 - y2))

# Distance from Atlanta to Charlotte
d4 = radius * acos(sin(x1) * sin(x4) + cos(x1) * cos(x4) * cos(y1 - y4))
# Distance from Charlotte to Orlando
d5 = radius * acos(sin(x4) * sin(x2) + cos(x4) * cos(x2) * cos(y4 - y2))

#Calculate all sides from Atlanta to Savannah to Orlando
s1 = (d1+d2+d3)/2
#Calculate area of first triangle
area1 = (s1*(s1-d1)*(s1-d2)*(s1-d3)) ** 0.5

#Calculate all sides from Atlanta to Charlotte to Orlando
s2 = (d1+d3+d4)/2
#Calculate area of second triangle
area2 = (s2*(s2-d1)*(s2-d3)*(s2-d4)) ** 0.5

print("Total area form by 4 cities: Atlanta, Savannah, Orlando, and Charlotte is", area1 + area2, "km2")






