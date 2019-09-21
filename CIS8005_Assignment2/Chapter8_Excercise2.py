''' Chapter 8 Excercise 2'''
# Function to check String
def checkString(str1,str2):
    if str2.find(str1) != -1:
        print("String 1 is a substring of String 2")
    else:
        print("String 1 is a not a substring of String 2")

#Main Method for prompt user inputs
def main():
    str1 = input("Please enter your string 1: ")
    str2 = input("Please enter your string 2: ")
    checkString(str1,str2)
    
main()