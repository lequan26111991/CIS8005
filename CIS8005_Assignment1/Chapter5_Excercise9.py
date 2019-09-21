''' Chapter 5 Excercise 9 '''
#Get Tuition and Interest
tuition = 10000
interest = 0.05

#Loop through 14 years
totalcost = 0
i = 0
while i < 14:
    tuition = tuition * 1.05 #Increase 5 % each year
    print("Tuition in",i+1,"year is",round(tuition,2)) #print tuition after 10 years
    if i > 9: #Start from year 10 to calculate all tuition
        totalcost = totalcost + tuition # Sum up total cost
    i+=1
print("The total cost of four years\' worth of tuition starting ten years from now is",round(totalcost,2)) #print 4 years tuition
