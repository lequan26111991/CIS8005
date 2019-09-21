''' Chapter 6 Excercise 18 '''
import random 
def printMatrix(n):
    for row in range(1,n+1): #Loop each row
        for col in range(1,n+1): #Loop through each record
            print(random.randint(0,1), end="") #Print n x n number 
        print(" ")
def main():
    n= eval(input("Please enter n: ")) #Prompt input
    printMatrix(n)
main()
