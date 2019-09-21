'''Chapter 4 Excercise 21'''

#Input year, month and day
year = eval(input("Enter year: (e.g., 2008): "))
m= eval(input("Enter month: 1-12: "))
q = eval(input("Enter the day of the month: 1-31: "))

#Convert January and February of a year and minus one year from hint
if m == 1:
    m = m + 12
    year = year - 1
elif m == 2:
    m = m + 12
    year = year - 1
    
#Calculate the century and year of century    
j = year // 100
k = year % 100

#Make Calculation
h = round((q + ( (26 * (m + 1) ) / 10 ) + k + (k / 4) + (j / 4) + (5 * j))) % 7

#Find the current date
if h == 0:
    today = "Saturday"
elif h == 2: 
    today = "Monday"
elif h == 3: 
    today = "Tuesday"
elif h == 4: 
    today = "Wednesday"
elif h == 5: 
    today = "Thursday"
elif h == 6: 
    today = "Friday"
else: 
    today = "Sunday"
    
print("Day of the week is",today)