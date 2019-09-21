''' Chapter 6 Excercise 29 '''

# Return true if the card number is valid
def isValid(number): 
    return (getSize(number) >= 13 and getSize(number) <= 16) and (prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 37) or prefixMatched(number, 6)) and ((sumOfDoubleEvenPlace(number) +  sumOfOddPlace(number)) % 10 == 0)

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum = 0  
    for i in range(2, getSize(number), 2): #Loop through all even place
        divisor = 10**i
        remainder = 10**(i-1)
        sum += getDigit(((number % divisor)//remainder) * 2) #return the digit between i and i-1 *2 and check by getDigit
    return round(sum) 

# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number): 
    if (number < 9): 
        return number 
    else:
        return number / 10 + number % 10 

# Return sum of odd place digits in number
def sumOfOddPlace(number):
     sum = 0  
     for i in range(1,  getSize(number) - 1, 2): #Loop through all odd place 
        divisor = 10**i 
        remainder = 10 **(i-1)
        sum += (number % divisor)//remainder #return the digit between i and i-1
     return round(sum) 

# Return true if the digit d is a prefix for number  
def prefixMatched(number,d):
    return getPrefix(number, getSize(d)) == d 
  
# Return the number of digits in digit 
def getSize(digit): 
    return len(str(digit)) 
  
# Return the first d number of digits from number. If the number of digits in number is less than d, return number. 
def getPrefix(number , d):
    if (getSize(number) > d): 
        divisor = 10**(getSize(number) - d ) #Get 10^ of number of digits after first digits
        return number // divisor
    else:
        return number 

#Main method
def main(): 
    number = eval(input("Please enter credit card numbers"))
    if isValid(number) == True:
        print(number,"is valid")
    else:
        print(number,"is not valid")
main()
