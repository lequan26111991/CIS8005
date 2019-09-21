''' Chapter 11 Excercise 10 '''
import random
matrix =[]
for i in range(4):
    matrix.append([])
    for j in range(4):
        matrix[i].append([])
        matrix[i][j] = random.randint(0,1)

print(matrix)


#Check the row
highsumrow = sum(matrix[0])
highsumrowindex = 0
highsumcolumnindex = 0
highsumcolumn = 0

#loop through all row and get the most 1s based in row
for i in range(0,4):
    if sum(matrix[i]) > highsumrow:
        highsumrow = sum(matrix[i])
        highsumrowindex = i
        totalcurrentcolumn = 0

#loop through all columns and get the most 1s based in column
for j in range(0,4):
    totalcurrentcolumn = 0
    for h in range(0,4):
        totalcurrentcolumn += matrix[h][j]
    if totalcurrentcolumn > highsumcolumn:
        highsumcolumn = totalcurrentcolumn
        highsumcolumnindex = j
           

print ("The largest row index:",highsumrowindex,"and total number of 1s is:",highsumrow)
print ("The largest column index:",highsumcolumnindex,"and total number of 1s is:",highsumcolumn)

    
