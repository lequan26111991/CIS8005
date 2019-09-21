''' Chapter 4 Excercise 3 '''
a,b,c,d,e,f = eval(input("Enter a, b, c, d, e, f: "))

#Check if a*f - b*c is 0 or not
if (a * d - b * c) == 0:
    print("The equation has no solution")

#Calculate x and y if denominator is no 0
else:
    x = (e * d - b * f)/ (a * d - b * c)
    y = (a * f - e * c)/ (a * d - b * c)
    print("x is:", x,"y is:", y )
