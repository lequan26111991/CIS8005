'''Chapter 6 Excercise 3 '''

#Count number of tenth 
def count(number):
    tenth = 1
    count = 0
    while number > tenth:
        count +=1
        tenth *= 10
    return count -1 #Reduce 1 unit since last digit won't time 10
    
# Return the reversal of an integer
def reverse(number):
    power = count(number)
    if number < 10:
        return number
    else:
        return (number % 10) * (10**power) + reverse(number // 10)

# Return true if number is a palindrome
def isPalindrome(number):
    #get reserve
    Pal = "Not a Palindrome"
    rev = reverse(number)
    if (rev == number):
        Pal = "a Palindrome"
    return Pal
        
def main(): # Main method
    x = eval(input("Enter number: "))
    print("The reserve number is:",reverse(x))
    print("The number is",isPalindrome(x))
          
main()