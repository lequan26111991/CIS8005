'''Chapter 8 Excercise 3'''

def checkValidPassword(password):
    isvalid = True
    countdigit = 0
    if len(password) < 8:
        isValid = False
    else:    
        for char in password:
            if char.isalnum() == False:
                isValid = False
            if char.isdigit() == True:
                countdigit += 1
            if countdigit < 2:
                isvalid = False
        
    return isvalid    
def main():
    str = input("Please enter a password: ")
    valid = checkValidPassword(str)
    if valid == True:
        print("Valid Password")
    else:
        print("Invalid Password")
main()
            
    
        
    