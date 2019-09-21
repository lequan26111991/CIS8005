''' Chapter 15 Excercise 24 '''

import os

def main():
    # Prompt the user to enter a directory or a file
    dir = input("Enter a directory: ") 
   
def getNoFiles(dir):
    size = 0 
    if not os.path.isfile(dir): 
        list = os.listdir(dir) # List all subfolders
        for i in range(len(list)):
            size += getNoFiles(dir +"\\"+ list[i]) #pass new folder directory to recursion
    else: 
        size += 1 #Count if current directory is file

    return size

main()
