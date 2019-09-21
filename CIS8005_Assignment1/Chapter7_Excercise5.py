''' Chapter 7 Excercise 5 '''
from math import *
# Class of Regular Polygon and constructor
class RegularPolygon:
    def __init__(self, n = 3, size = 1, x = 0, y = 0):
        self.__n = n
        self.__size = size
        self.__x = x
        self.__y = y
    
    #Accessor of N
    def getN(self):
        return self.__n 
    
    #Accessor of size
    def getSize(self):
        return self.__size 
    
    #Accessor of X
    def getX(self):
        return self.__x
    
    #Accessor of Y
    def getY(self):
        return self.__Y
    
    #Mutator of N
    def setN(self,N):
        self.__n = N
    
    #Mutator of size
    def setSize(self,size):
        self.__size = size
        
    #Mutator of X
    def setX(self,x):
        self.__x = x
    
    #Mutator of Y
    def setY(self,y):
        self.__y = y
    
    #Get Perimeter of Polygon
    def getPerimeter(self):
        return (self.__n * self.__size)
    
    #Get Area of Polygon
    def getArea(self):
        return ((self.__n * (self.__size ** 2)) / (4 * tan(pi/self.__n)))
    
#Create Objects
poly1 = RegularPolygon()
poly2 = RegularPolygon(6, 4)
poly3 = RegularPolygon(10, 4, 5.6, 7.8)

#Print perimeter and area of all objects
print("The perimeter of poly1 is",poly1.getPerimeter(),"and its area is",poly1.getArea())
print("The perimeter of poly2 is",poly2.getPerimeter(),"and its area is",poly2.getArea())
print("The perimeter of poly3 is",poly3.getPerimeter(),"and its area is",poly3.getArea())