''' Chapter 8 Excercise 13'''

def prefix(s1, s2):
    result =""
    x = 0
    y = 0
    while  x < len(s1) - 1 and y < len(s2) -1: #check if either string is done first
        if s1[x] != s2[y]: #Stop comparing if not match
            break
        else:
            result += s1[x] #Concatinate to result if match
        x+=1
        y+=1
    return result 

#Main method       
def main():
    str1 = input("Please enter string 1: ")
    str2 = input("Please enter string 2: ")
    print(prefix(str1,str2))
    
main()
    