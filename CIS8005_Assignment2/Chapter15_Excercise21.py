''' Chapter 15 Excercise 21 '''

def binaryToDecimal(binaryString):
    if len(binaryString) == 1:
        return int(binaryString) * 1
    else:
        return (int(binaryString[0]) * (2 **(len(binaryString)-1))) + binaryToDecimal(binaryString[1:len(binaryString) +1])
def main():
    print(binaryToDecimal("1111"))

main()
