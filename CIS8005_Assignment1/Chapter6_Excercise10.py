''' Chapter 6 Excercise 10 '''

# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime
        divisor += 1
    return True # number is prime
def printPrimeNumbers(limit):
    NUMBER_OF_PRIMES = 50 # Number of primes to display
    NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness
    # Repeatedly find prime numbers
    while number < limit:
        # Print the prime number and increase the count
        if isPrime(number):
            count += 1 # Increase the count
            print(number, end = " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Print the number and advance to the new line
                print()

        # Check if the next number is prime
        number += 1
def main():
    print("The prime numbers are less than 10000")
    printPrimeNumbers(10000)
main() # Call the main function
