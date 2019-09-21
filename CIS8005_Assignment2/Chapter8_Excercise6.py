'''Chapter 8 Excercise 6 '''

def countLetters(s):
    count = 0
    for letter in s:
        if letter.isalpha():
            count +=1
    return count
def main():
    str = input("Please enter your string")
    print("Number of letter will be :",countLetters(str))

main()