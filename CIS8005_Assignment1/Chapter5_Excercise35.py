''' Chapter 5 Excercise 35 '''
sum = 0
#Loop through all 10000 integers
for number in range(1,10001):
    for divisor in range(1,number): #Loop through range of possible divisor
        if (number % divisor == 0):
            sum += divisor
    if (sum == number): #if sum of all divisor = number, then print
        print(number,"is a perfect number")
    sum = 0 #Reset sum for the next number
