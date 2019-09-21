''' Chapter 5 Excercise 30 '''

#prompt the inputs

year,day = eval(input("Please enter year and first day of the year: "))

#Loop through the year and print output
for month in range(1,13):
    if (month == 5 or month == 7 or month == 10 or month == 12):
        day += 30
    elif(month == 2 or month == 4 or month == 6 or month == 9 or month == 11 or month == 8): #"Month 4,6,9,11"
        day += 31
    elif(month == 3): #Month 3
        day +=28
    else: #January
        day +=0
    #Find the current day after sum all day
    if day % 7 == 0:
        today = "Sunday"
    elif day % 7 == 1: 
        today ="Monday"
    elif day % 7 == 2 : 
        today ="Tuesday"
    elif day % 7 == 3: 
        today ="Wednesday"
    elif day % 7 == 4: 
        today ="Thursday"
    elif day % 7 == 5: 
        today ="Friday"
    else: 
        today ="Saturday"

    # Find current Month 
    if month == 1:
        thismonth = "January"
    elif month == 2:
        thismonth = "February"
    elif month == 3:
        thismonth = "March"
    elif month == 4:
        thismonth = "April"
    elif month == 5:
        thismonth = "May"
    elif month == 6:
        thismonth = "June"
    elif month == 7:
        thismonth = "July"
    elif month == 8:
        thismonth = "August"
    elif month == 9:
        thismonth = "September"
    elif month == 10:
        thismonth = "October"
    elif month == 11:
        thismonth = "November"
    elif month == 12:
        thismonth = "December"
    print(thismonth,"1",year,"is",today)
