''' Chapter 5 Excercise 16 '''

# Prompt the user to enter two integers
n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))
gcd=0
#Get k is minimum of n1 and n2
if (n1 > n2):
    k = n2
else: 
    k = n1
#Check range
for check in range(k,2,-1):
    if n1 % check == 0 and n2 % check == 0:
       gcd = check
       break
print("The greatest common divisor for",n1, "and", n2, "is", gcd)
