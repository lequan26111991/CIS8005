''' Chapter 2 Exercise 21 '''
#Input the value
saving = eval(input("Enter monthly saving amount: "))
#Calculate total saving until the month 6
saving1 = saving * 1.00417
saving2 = (saving + saving1) * 1.00417
saving3 = (saving + saving2) * 1.00417
saving4 = (saving + saving3) * 1.00417
saving5 = (saving + saving4) * 1.00417
saving6 = (saving + saving5) * 1.00417
#print value after 6 months
print("After 6 months, the account value is ", int(saving6 * 100) / 100)
