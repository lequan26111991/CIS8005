''' Chapter 5 Excercise 36 '''

from random import *
#Get user choice and computer choice
userwin = 0
comwin = 0

while userwin < 3 and comwin < 3: 
    choice = eval(input("scissor (0), rock (1), paper (2):"))
    cchoice = randint(0,2)

    #Make decision base on choices
    #User scissor cases
    if choice == 0 and cchoice == 1:
        print("The computer is rock. You are scissor. Computer won.")
        comwin = comwin + 1 #add 1 count for computer win
    elif choice == 0 and cchoice == 0:
        print("The computer is scissor. You are scissor. It is a draw.")
    elif choice == 0 and cchoice == 2:
        print("The computer is paper. You are scissor. You won.")
        userwin = userwin + 1 #add 1 count for user win 

    #User rock cases
    if choice == 1 and cchoice == 2:
        print("The computer is paper. You are rock. Computer won.")
        comwin = comwin + 1 #add 1 count for computer win
    elif choice == 1 and cchoice == 1:
        print("The computer is rock. You are rock. It is a draw.")
    elif choice == 1 and cchoice == 0:
        print("The computer is scissor. You are rock. You won.")
        userwin = userwin + 1 #add 1 count for user win 

    #User paper cases
    if choice == 2 and cchoice == 0:
        print("The computer is scissor. You are paper. Computer won.")
        comwin = comwin + 1 #add 1 count for computer win
    elif choice == 2 and cchoice == 2:
        print("The computer is paper. You are paper. It is a draw.")
    elif choice == 2 and cchoice == 1:
        print("The computer is rock. You are paper. You won.")
        userwin = userwin + 1 #add 1 count for user win

if userwin == 3:
    print("Game Over ! You won three times")
else:
    print("Game Over ! Computer won three times")
