''' Chapter 8 Excercise 17 '''
import math

class Point:
    def __init__(self,x = 0 ,y = 0):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self,x2,y2):
        distance = math.sqrt((x2 - self.__x) ** 2) + math.sqrt((y2 - self.__y) ** 2)
        return distance
    
    def isNearBy(self,p):
        if self.distance(p.getX(),p.getY()) > 5:
            print ("Two points are not near each other.")  
        else:
            print("Two points are near each other.")
    def __str__(self):
        return str("("+str(self.__x)+","+str(self.__y)+")")
    
def main():
    x1,y1,x2,y2 = eval(input("Please enter x1, y1, x2, y2: "))
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    print("Distance between two points",p1.__str__(),"and",p2.__str__(),"is",p1.distance(p2.getX(),p2.getY()))
    p1.isNearBy(p2)

main()
    