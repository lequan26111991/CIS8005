''' Chapter 3 Exercise 9 '''
#Input values for employee's information
employee = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
fed = eval(input("Enter federal tax withholding rate: "))
state = eval(input("Enter state tax withholding rate: "))

#Display results
print("Employee Name:", employee)
print("Hours Worked:", hours)
print("Pay Rate:", rate)
print("Gross Pay:", hours * rate)
print("Deductions:")
print("\tFederal Withholding (",fed * 100,"% ): $",round(hours * rate * fed, 2) )
print("\tState Withholding (",state * 100,"% ): $",round(hours * rate * state, 2) )
print("\tTotal Deduction: $" ,round((hours * rate) * (state + fed), 2) )
print("Net Pay: $", round((hours * rate) - (hours * rate) * (state + fed), 2))
