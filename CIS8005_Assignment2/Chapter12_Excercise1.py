''' Chapter 12 Excercise 1 '''

import math
class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
        " and filled: " + str(self.__filled)

class Triangle(GeometricObject):

    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0, color = "green", filled = True): #Initiate constructor
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        super().__init__(color = color, filled = filled) #pass color and fill to parent class

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3)/2
        area = math.sqrt(s*(s1 - self.__side1) * (s1 - self.__side2) * (s1 - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self): #Overide string method
       return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)

s1,s2,s3 = eval(input("Please enter three sides "))
fill = eval(input("Please enter 1 for fill and 0 for not fill "))
if fill == 1:
    isfilled = True
else:
    isfilled = False
color = input("Please enter a color for triangle ")

t1 = Triangle(s1,s2,s3,color,isfilled)

print("Area of the triangle is: ",t1.getArea())
print("Perimeter of the triangle is: ",t1.getPerimeter())
print("Color of the triangle is: ",t1.getColor())
print("Triangle is filled: ",t1.isFilled())
