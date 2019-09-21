''' Chapter 10 Excercise 16 '''

def sortList(listnum):
    
    # Split the string and convert to list of integers
    listnum = listnum.split()
    lst = [int(x) for x in (listnum)]
    
    # loop through each number and neighbor to sort
    i = 0
    while i < (len(lst) - 1):
        if lst[i] > lst[i+1]: #Swap number if current number > next number
            medium = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = medium
            i = 0 #reset i = 0
        i += 1 # go to next number

    return lst

def main():
    listnum = input("Enter list: ")
    print("Sorted list is : ",sortList(listnum))

main()
            
    
    