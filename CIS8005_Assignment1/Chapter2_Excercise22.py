''' Chapter 2 Exercise 22 '''
#Input the value
year = eval(input("Enter the number of years: "))
#Calculate one year increment of population
pop = 312032486
yeartosecond = 365 * 24 * 60 * 60
oneyearpop = (yeartosecond // 7 + yeartosecond // 45 - yeartosecond // 13)
#first year population
print("The population in", year ,"is", pop + year*oneyearpop)
