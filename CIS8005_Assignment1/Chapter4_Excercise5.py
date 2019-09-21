''' Chapter 4 Excercise 5 '''
ntoday = int(input("Enter today's day: "))
nfuture = int(input("Enter the number of days elapsed since today:"))

#Find the current date
if ntoday % 7 == 0:
    today = "Sunday"
elif ntoday % 7 == 1: 
    today = "Monday"
elif ntoday % 7 == 2 : 
    today = "Tuesday"
elif ntoday % 7 == 3: 
    today = "Wednesday"
elif ntoday % 7 == 4: 
    today = "Thursday"
elif ntoday % 7 == 5: 
    today = "Friday"
else: 
    today = "Saturday"

#Add value of days elapsed since today
fday = (nfuture + ntoday) % 7
if (fday == 0): 
    future = "Sunday"
elif (fday == 1): 
    future = "Monday"
elif (fday == 2): 
    future = "Tuesday"
elif (fday == 3): 
    future = "Wednesday"
elif (fday == 4): 
    future = "Thursday"
elif (fday == 5): 
    future = "Friday"
else: 
    future ="Saturday"
#print result
print("Today is",today,"and the future day is",future)

