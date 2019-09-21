'''Chapter 2 Excercise 7 '''
input_minute = eval(input("Please enter your minute: "))
#find one year and one day in minute
oneyear = 365*24*60
oneday = 24*60
#calculate the result 
result_year = input_minute // oneyear
result_day = (input_minute - result_year * oneyear) // oneday
print(input_minute, "minutes is approximately", result_year, "years and", result_day," days") 

