''' Chapter 11 Excercise 13 '''

def locateLargest(list):
    #get ininitial number
    locallargest = 0
    row = 0
    column = 0
    #loop though all row and column
    for i in range(len(list)):
         for j in range(len(list[i])):
            if list[i][j] > locallargest: #if local largest is smaller than current element, reassign
                locallargest = list[i][j]
                row = i
                column = j
    return "("+str(row)+","+str(column)+")"

def main():
    list = []
    number = eval(input("Enter the number of row in list: "))
    #enter number of input
    for i in range(number):
        list.append([])
        list[i] = input("Enter a row:")
        #split to sub list
        list[i] = list[i].split()
        list[i] = [eval(x) for x in (list[i])]
    print("The location of the largest element is at", locateLargest(list))

main()
    
