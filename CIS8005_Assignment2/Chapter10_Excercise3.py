'''Chapter 10 Excercise 3'''

#Create container list for integers and count
integers = []

#Get input and bring them into integers list
inputlist = input("Enter integer between 1 and 100: ")
integers = inputlist.split()

#Make list is list of integers
integers = [int(x) for x in integers]
locate = len(integers) * [0]
count = len(integers) * [0]

# Check through the whole list
for number in range(len(integers)):
    if integers[number] not in (locate): # If element is not a part of located list , add to locate and mark as 1
        locate[number] = integers[number]
        count[number] = 1
    else: #If it is already a part of it, find from the beginning and increase its count
        for i in range(number):
            if locate[i] == integers[number]:
               count[i] += 1
        count.pop() # remove the empty element in count for found a duplicated value 
        locate.pop() # remove the empty element in locate for found a duplicated value 

for j in range(len(locate)):
    if count[j] == 1:
        print(locate[j],"occurs",count[j],"time")
    else:
        print(locate[j],"occurs",count[j],"times")  
        
