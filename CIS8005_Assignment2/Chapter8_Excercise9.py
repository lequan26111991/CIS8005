'''Chapter 8 Excercise 9 '''

def binaryToHex(binaryValue):
    
    #Convert Binary to Decimal
    decimal = 0
    for digit in range(0,len(binaryValue),1):
        decimal += int(binaryValue[digit]) * 2 ** (len(binaryValue)- 1 - digit)
    
    #Convert Decimal to Hexadecimal
    hex =""
    while decimal > 0:
        digit = decimal % 16 #get hexadecimal value
        if digit > 9: #Convert to Letter if neccessary
            digit = chr(ord("A") + digit - 10)
        else:
            digit = str(digit)
        hex = digit + hex
        decimal = decimal // 16 # Go to next digit
                 
    return hex

def main():
    number = input("Please enter your binary:")
    print(binaryToHex(number))
    
main()