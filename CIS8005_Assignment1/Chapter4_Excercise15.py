''' Chapter 4 Excercise 15 '''
import random

# Generate a lottery number
lottery = random.randint(100,999)
# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery result
ldigit1 = lottery // 100
ldigit2 = (lottery - ldigit1 * 100) // 10
ldigit3 = lottery - ldigit1 * 100 - ldigit2 * 10

# Get digits from guess result
gdigit1 = guess // 100
gdigit2 = (guess - gdigit1 * 100) // 10
gdigit3 = guess - gdigit1 * 100 - gdigit2 * 10

print("The lottery number is", lottery)

# Check the guess result
if guess == lottery:
    print("Exact match: you win $10,000")
elif (ldigit1 == gdigit1 and ldigit2 == gdigit3 and ldigit3 == gdigit2) or \
     (ldigit1 == gdigit2 and ldigit2 == gdigit3 and ldigit3 == gdigit1) or \
     (ldigit1 == gdigit2 and ldigit2 == gdigit1 and ldigit3 == gdigit3) or \
     (ldigit1 == gdigit3 and ldigit2 == gdigit1 and ldigit3 == gdigit2) or \
     (ldigit1 == gdigit3 and ldigit2 == gdigit2 and ldigit3 == gdigit1):
    print("Match all digits: you win $3,000")
elif (gdigit1 == ldigit1 or \
       gdigit1 == ldigit2 or \
       gdigit1 == ldigit3 or \
       gdigit2 == ldigit1 or \
       gdigit2 == ldigit2 or \
       gdigit2 == ldigit3 or \
       gdigit3 == ldigit1 or \
       gdigit3 == ldigit2 or \
       gdigit3 == ldigit3):
        print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
