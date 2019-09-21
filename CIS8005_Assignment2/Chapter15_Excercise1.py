''' Chapter 15 Excercise 1 '''

def sumDigits(n):

    if n < 10:
        return n #if there is only one digit left
    else:
        return n % 10 + sumDigits(n//10) #recursive for adding value

def main():
    number = eval(input("please enter the number"))
    print(sumDigits(number))

main()

