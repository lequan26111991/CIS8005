'''Chapter4 Excercise24'''
from random import *
chose = randint(1,52)

#Get (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,Jack, Queen, King)

if chose <= 4:
    rank = "Ace"
elif chose > 4 and chose <= 8:
    rank = "2"
elif chose > 8 and chose <= 12:
    rank = "3"
elif chose > 12 and chose <= 16:
    rank = "4"
elif chose > 16 and chose <= 20:
    rank = "5"
elif chose > 20 and chose <= 24:
    rank = "6"
elif chose > 24 and chose <= 28:
    rank = "7"
elif chose > 28 and chose <= 32:
    rank = "8"
elif chose > 32 and chose <= 36:
    rank = "9"
elif chose > 36 and chose <= 40:
    rank = "10"
elif chose > 40 and chose <= 44:
    rank = "Jack"
elif chose > 44 and chose <= 48:
    rank = "Queen"  
else:
    rank = "King" 
    
# Get suit Clubs, Diamonds, Hearts, Spades
if chose % 4 == 1:
    suit = "Clubs"
elif chose % 4 == 2:
    suit =  "Diamonds"
elif chose % 4 == 3:
    suit =  "Hearts" 
else:
    suit =  "Spades"   

#Print the result
print("The card you picked is the",rank,"of",suit)

        