''' Chapter 4 Excercise 3 '''

from random import *
# Generate random numbers
number1 = randint(0, 100)
number2 = randint(0, 100)
# Prompt the user to enter an answer
answer = eval(input("What is "+ str(number1)+ " + "+ str(number2) + "? "))
# Display result
if (number1+number2 == answer):
    print("Correct! The answer is", answer)
else:    
    print("Wrong! The answer is", number1 + number2)
