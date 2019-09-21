''' Chapter 13 Excercise 3 '''

#Enter file name
filename = input("Enter a filename: ")

#Create file
filewrite = open(filename, 'w')
filewrite.write("23 34 87 22 44 77")
filewrite.close()

#Open and extract score
file = open(filename, 'r')
score = [int(n) for n in file.read().split()]
total = sum(score)
average = total / len(score)
file.close()

#print values
print("There are",len(score)," scores")
print("The total is",total)
print("The average is",average)
