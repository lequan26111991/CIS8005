'''Chapter 11 Excerise 2'''

def sumMajorDiagonal(m):
    total = 0
    for i in range(len(m)): #Loop through row
        for j in range(len(m[i])): #loop though column
            if i == j: #if i and j in same dimension, add to total
                total+=m[i][j]
    return total
    
def main():
    list = []
    for i in range(4):
        value = input("Enter a 4-by-4 matrix row for row "+str(i+1))
        value = value.split() #Split to single value
        value = [eval(x) for x in value] #convert to proper type
        list.append(value)
    print("Sum of the elements in major diagonal is",sumMajorDiagonal(list))
    
main()