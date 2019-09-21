''' Chapter 14 Excercise 3 '''

def main():
    #Create a file for testing
    file1 = open("text.txt", 'w')
    file1.write("Good morning, how are you?\n")
    file1.write("Good morning Quan, how are you?\n")
    file1.close()

    #Start problem with input
    filename = input("Enter a filename: ")
    
    #get the lines in file
    file2 = open(filename,"r")
    list1 = file2.readlines()

    #Append all list into a big string
    list2 = list1[0]
    for i in range(1,len(list1)):
        list2 += " " + list1[i]

    #split the whole big list into individual list and remove special characters
    list3 =""
    for char in list2:
        if char.isalnum() == True or char == " ":
            list3 = list3 + char
    list3 = list3.split()

    #Create a set to save the occurence
    set1 = set(list3)

    #Start new 0 for each member of set
    set1 = {key:0 for key in set1}

    #get count list of each special character
    for j in range(len(list3)):
        if list3[j] in set1:
            set1[list3[j]] = set1[list3[j]] + 1

    print(set1)
    


main()
