''' Chapter 10 Excercise 15'''

def isSorted(lst):
    sort1 = True
    
    #split to list of string
    lst = lst.split()
    
    #convert to int
    list = [int(x) for x in (lst)]
    
    #Compare current position to next position to see if it is greater
    for i in range(0,len(list) - 1):
        if list[i] > list[i+1]:
            sort1 = False
    return sort1

def main():
    stringlist = input("Enter list: ")
    
    #Return correct value
    if isSorted(stringlist) == True:
        print("The list is already sorted")
    else:
        print("The list is not sorted")
        
main()