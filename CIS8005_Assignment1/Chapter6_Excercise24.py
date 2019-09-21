''' Chapter 6 Excercise 24 '''
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
    rev = reverse(number)
    if (rev == number):
        return True
    else:
        return False

# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if (number % divisor == 0): # If true, number is not prime
            return False # number is not a prime
        divisor += 1
    return True # number is prime

def printPrimeNumbers(noOfPPrime):
    NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness
    # Repeatedly find prime numbers
    while count < noOfPPrime:
        # Print the prime number and increase the count
        if isPrime(number) and isPalindrome(number):
            count += 1 # Increase the count
            print(number, end = " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Print the number and advance to the new line
                 print("")
        # Check if the next number is prime
        number += 1
def main():
    printPrimeNumbers(100)
main() # Call the main function

