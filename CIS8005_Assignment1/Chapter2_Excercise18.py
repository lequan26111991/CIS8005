''' Chapter 2 Exercise 18 '''
from time import *
#Input
Zone = eval(input("Enter the time zone offset to GMT: "))
#Get the seconds from 1970
second = time()
#Get the current second 
csecond = second % 60 
#Get all minute
minute = second // 60 
#Get the current minute from all minute
cminute = minute % 60
#Get all hour
hour = minute // 60
#Get current hour from all hour
chour = hour % 24
#Add Zone to current hour
chour += Zone
#If current time is 24, put hour back to 0
hour %= 24
#Print result
print("The current time is", int(chour),":",int(cminute),":",int(csecond))
