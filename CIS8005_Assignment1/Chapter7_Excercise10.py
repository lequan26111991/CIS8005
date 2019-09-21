'''Chapter 7 Excercise 10 '''

import time
#Class and constructor
class Time:
    def __init__(self, currenttime):
        self.__hour = int((currenttime // 3600) % 24)
        self.__minute = int((currenttime % 3600) // 60)
        self.__second = int(currenttime % 60)

    #Get hour
    def getHour(self):
        return self.__hour
    
    #Get minute
    def getMinute(self):
        return self.__minute
    
    #Get second
    def getSecond(self):
        return self.__second
    
    #Set time method
    def setTime(self, elapsetime):
        self.__hour =   (self.__hour * 3600 + elapsetime) // 3600 % 24
        self.__minute = (self.__minute * 60 + elapsetime) % 3600 // 60
        self.__second = (self.__second  + elapsetime) % 60

#Create class of time
time1 = Time(time.time())
print("Current time is",time1.getHour(),":",time1.getMinute(),":",time1.getSecond())

#input elapse time and apply elapse
elapse = eval(input("Please enter new elapse time: ")) 
time1.setTime(elapse)
print("The hour:minute:second for the elapsed time is ",time1.getHour(),":",time1.getMinute(),":",time1.getSecond())

