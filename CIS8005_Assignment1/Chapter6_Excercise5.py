''' Chapter 6 Excercise 5 '''

def displaySortedNumbers(num1, num2, num3):
    if (num1 <= num2 and num2 <= num3 ):
        print("The order is:",num1,num2,num3)
    elif (num1 <= num3 and num3 <= num2 ):
        print("The order is:",num1,num3,num2)
    elif (num2 <= num1 and num1 <= num3 ):
        print("The order is:",num2,num1,num3)
    elif (num2 <= num3 and num3 <= num1 ):
        print("The order is:",num2,num3,num1)
    elif (num3 <= num1 and num1 <= num2 ):
        print("The order is:",num3,num1,num2)
    elif (num3 <= num2 and num2 <= num1 ):
        print("The order is:",num3,num2,num1)
def main():
    n1,n2,n3 = eval(input("Enter Three Number: "))
    displaySortedNumbers(n1, n2, n3)
main()
