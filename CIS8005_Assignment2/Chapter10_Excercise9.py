''' Chapter 10 Excercise 9 '''
from math import sqrt

# Compute the standard deviation of values
def deviation(x):
    total = 0
    for number in x:
        total += ((number -  mean(x)) ** 2)
    deviation = sqrt(total/(len(x) - 1))
    return deviation
    
# Compute the mean of a list of values
def mean(x):
    total = 0
    for number in (x):
        total += number
    mean = total / len(x)
    return mean

def main():
    #Get the list and split them to individual number
    stringlist = input("Please enter list of number ")
    stringlist = stringlist.split()
    listnum = [float(x) for x in stringlist]
    
    #Print all values
    print("The mean is",round(mean(listnum),2))
    print("The standard deviation is",round(deviation(listnum),5))

main()
    
