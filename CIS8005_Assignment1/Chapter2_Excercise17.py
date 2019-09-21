''' Chapter 2 Exercise 17 '''
#Weight input
w = eval(input("Enter weight in pounds: "))
h = eval(input("Enter height in inches: "))

#Calculate weight in kilogram and height in meters
kw = w * 0.45359237
ch = h * 0.0254
#Calculate BMI
bmi = kw/(ch*ch)
#Print output
print("BMI is: ", bmi)
