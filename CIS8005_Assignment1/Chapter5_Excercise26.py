''' Chapter 5 Excercise 26 '''
#Initiate variables
sum = 0
for total in range(1,99,2): # Loop from 1 to 99 with 2 increment
    sum += (total/(total +2))
print("Sum of all fractions is:",sum)
