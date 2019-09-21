''' Chapter 7 Excercise 9 '''

class LinearEquation:
    def __init__(self,a,b,c,d,e,f): 
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    #get a method
    def getA(self):
        return self.__a 
    #get b method
    def getB(self):
        return self.__b
    #get c method
    def getC(self):
        return self.__c
    #get d method
    def getD(self):
        return self.__d 
    #get e method
    def getE(self):
        return self.__e
    #get f method
    def getF(self):
        return self.__f
    
    #get is solvable method
    def isSolvable(self):
        if (self.__a * self.__d - self.__b * self.__c) == 0:
            return False
        else:
            return True
        
    #Method get X
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c) 
    
    #Method get Y
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)

x1,y1,x2,y2 = eval(input("Enter the endpoints of the first line segment: "))
x3,y3,x4,y4 = eval(input("Enter the endpoints of the second line segment: "))

#Calculate all constant from point
a = (y1 - y2)
b = (x2 -x1)
e = (y1 -y2)* x1 -(x1 -x2) * y1
c = (y3 -y4)
d = (x4 -x3)
f = (y3 -y4)* x3 -(x3 -x4) * y3

# Create an object 

e1 = LinearEquation(a,b,c,d,e,f)
#Print result
if e1.isSolvable():
    print("X is",e1.getX(),"and Y is",e1.getY())
else:
    print("The equation has no solution")
