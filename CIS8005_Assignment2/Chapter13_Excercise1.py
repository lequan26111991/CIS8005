''' Chapter 13 Excercise 1 '''

def main():
    #Create a file for testing
    file1 = open("text.txt", 'w')
    file1.write("Good morning, how are you?\n")
    file1.write("Good morning Quan, how are you?\n")
    file1.close()

    #Start problem with input
    filename = input("Enter a filename: ")
    filestring = input("Enter the string to be remove: ")
    
    #get the lines in file
    file2 = open(filename,"r")
    list1 = file2.readlines()
 
    for i in range(len(list1)):
        list1[i] = list1[i].replace(filestring,"")
    file2.close()

    #Write back new line
    file3 = open(filename,"w")
    for i in range(len(list1)):
        file3.write(list1[i])
    file3.close()

    #print the new result
    file4 = open(filename,"r")
    print(file4.readlines())
    file4.close()

main()
