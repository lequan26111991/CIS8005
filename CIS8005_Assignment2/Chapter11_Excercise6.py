'''Chapter 11 Excercise 6'''
import math

def addMatrix(matrix1, matrix2):
    
    #Split matrix to single element
    matrix1 = matrix1.split()
    matrix1 = [eval(x) for x in (matrix1)]
    matrix2 = matrix2.split()
    matrix2 = [eval(y) for y in (matrix2)]
    
    #check possible type of matrix1
    dimension1 = int(math.sqrt(len(matrix1)))
    
    #convert single list to multidimensions list matrixa
    matrixa = []
    for i in range(dimension1):
        matrixa.append([])
        for j in range(dimension1):
            matrixa[i].append([])
            matrixa[i][j] = matrix1[i * dimension1 + j]
            
    #check possible type of matrix of matrix2
    dimension2 = int(math.sqrt(len(matrix2)))
    
    #if different return unable to add
    if dimension2 != dimension1:
        print("Two lists are not able to add due to not the same dimension")
    else:
        #convert single list to multidimensions list matrixb
        matrixb = []
        for i in range(dimension2):
            matrixb.append([])
            for j in range(dimension2):
                matrixb[i].append([])
                matrixb[i][j] = matrix2[i * dimension2 + j]
                
           
    #Add two dimensions

    matrixc =[]
    for i in range(dimension1):
        matrixc.append([])
        for j in range(dimension1):
            matrixc[i].append([])
            matrixc[i][j] = 0
            for h in range(dimension1): # get h to loop through all element of column in maxtrix a and row in matrix b
                matrixc[i][j] += matrixa[i][h] * matrixb[h][j]
            print(str(matrixa[i][j]),end = " ")
        print(end =" ")   
        #Add + sign   
        if(i == round(dimension1/2)-1):
            print("+ ", end = "") 
        else:
            print(end ="  ")   
        #Add b list    
        for k in range(dimension1):       
            print(str(matrixb[i][k]),end = " ")
        print(end =" ")   
        #Add Equal sign    
        if(i == round(dimension1/2)-1):
            print("= ", end = "")
        else:
            print(end ="  ")   
        #Add c matrix
        for h in range(dimension1):       
            print(str(matrixc[i][h]),end = " ")
        print(end =" ")     
        print()

        
def main():
    matrix1 = input("Enter Matrix 1: ")
    matrix2 = input("Enter Matrix 2: ")
    print("the matrix is as follow")
    print(addMatrix(matrix1, matrix2))
    
main()

    
