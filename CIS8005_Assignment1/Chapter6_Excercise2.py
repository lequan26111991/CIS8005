''' Chapter 6 Excercise 2 '''
def sumDigit(n): #Create function
    if n == 0: # skip when number is 0
        return 0
    else:
        return (n % 10) + sumDigit(n // 10) # Add mode of n to recursive function
def main(): # Main function
    x = eval(input("Please enter your number: "))
    print("Sum of its number is:",sumDigit(x))
    
main()