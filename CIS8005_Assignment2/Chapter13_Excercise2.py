''' Chapter 13 Excercise 2 '''
lines = 0
words = 0
character = 0

filename = input("Please enter file name")
file1 = open(filename,"r")
list = file1.readlines()

# Get lines
for i in range(len(list)):
    lines +=1
    list[i] = list[i].split()

#Get words 
for i in range(len(list)):
    for j in range(len(list[i])):
        words +=1

#Get Character
for i in range(len(list)):
    for j in range(len(list[i])):
        for h in range(len(list[i][j])):
            character +=1

print(character,"characters")
print(words,"words")
print(lines,"lines")
