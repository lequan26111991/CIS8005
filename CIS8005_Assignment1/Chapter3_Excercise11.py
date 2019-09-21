''' Chapter 3 Exercise 11 '''
#Input value of integer
number = eval(input("Enter an integer: "))
#get first digit and convert to thousand
first = (number % 10) * 1000
#get the second digit and convert to hundred
second = ((number % 100)//10) * 100
#get the third digit and convert to tenth
third = ((number % 1000)//100) * 10
#get the forth digit
forth = number // 1000
#Print the result
print("The reverse number is ",first+second+third+forth)
