''' Chapter 2 Exercise 14 '''
#Input all points
x1,y1,x2,y2,x3,y3 = eval(input("Please enter three points: "))
#Calculate all sides
s1 = ((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)) ** 0.5  
s2 = ((x3-x2) * (x3-x2) + (y3-y2) * (y3-y2)) ** 0.5 
s3 = ((x1-x3) * (x1-x3) + (y1-y3) * (y1-y3)) ** 0.5
#Calculate s
s = (s1+s2+s3)/2
#Calculate area and display result
area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5
print("The area of the triangle is:", area)
