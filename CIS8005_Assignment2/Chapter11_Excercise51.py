''' Chapter 11 Excercise 51 '''

#Get the list one by one
list1 = input("Enter student name's and score: ")
list1 = list1.split()
list1 = [x for x in list1]

for i in range(0, len(list1), 2):
    #Swap name and number position
    list1[i],list1[i+1] = list1[i+1],list1[i]

list2 = []

#Divide into group of pair of number and name and sort based on coma
for j in range(0, len(list1), 2):
    list2.append(list1[j] + " " + list1[j + 1] )
    #Split by coma
    list2.sort()

#Split again into individual two dimentional number
for k in range(len(list2)):
    list2[k] = list2[k].split()

#Swap name and number again to print
for h in range(len(list2)):
    for m in range(len(list2[h])-1):
        list2[h][m],list2[h][m+1] = list2[h][m+1],list2[h][m]
        print(list2[h][m] + " " + list2[h][m+1], end ="")
    print()

