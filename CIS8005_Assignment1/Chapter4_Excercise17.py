'''Chapter 4 Excercise 17'''

from random import *
#Get user choice and computer choice
choice = eval(input("scissor (0), rock (1), paper (2):"))
cchoice = randint(0,2)

#Make decision base on choices
#User scissor cases
if choice == 0 and cchoice == 1:
    print("The computer is rock. You are scissor. Computer won.")
elif choice == 0 and cchoice == 0:
    print("The computer is scissor. You are scissor. It is a draw.")
elif choice == 0 and cchoice == 2:
    print("The computer is paper. You are scissor. You won.")

#User rock cases
if choice == 1 and cchoice == 2:
    print("The computer is paper. You are rock. Computer won.")
elif choice == 1 and cchoice == 1:
    print("The computer is rock. You are rock. It is a draw.")
elif choice == 1 and cchoice == 0:
    print("The computer is scissor. You are rock. You won.")

#User paper cases
if choice == 2 and cchoice == 0:
    print("The computer is scissor. You are paper. Computer won.")
elif choice == 2 and cchoice == 2:
    print("The computer is paper. You are paper. It is a draw.")
elif choice == 2 and cchoice == 1:
    print("The computer is rock. You are paper. You won.")