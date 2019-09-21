''' Chapter 5 Excercise 19 '''

number = eval(input("Please enter number of line: ")) #Enter number
number = number+1 #Add 1 more unit to make range of for loop correct

for line in range(1,number):
    for space in range(number - line, 1, -1): # Loop number of space
        print(end=" ") 
    for leftnum in range(line,1,-1): #Loop number of left columns
        print(leftnum, end = "")
    for rightnum in range(1,line + 1): #Loop number of right columns
        print(rightnum, end = "")
    print(" ")
