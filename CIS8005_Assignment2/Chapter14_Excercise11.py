''' Chapter 14 Excercise 11 '''

#Enter file name
filename = input("Enter a filename: ")

#Create file
filewrite = open(filename, 'w')
filewrite.write("Hi, My name is Quan, how are you doing?")
filewrite.write("i am a stuudent")
filewrite.close()

#Open and extract score
file = open(filename, 'r')
lists = file.readlines()

file.close()
vow = 0
cons = 0
for i in range(len(lists)):
    for char in lists[i]:
        if char.isalpha() == True: #get only character
            if char.upper() in ["A","E","I","U"]:
                vow += 1 #count vowel
            else:
                cons += 1 #count consonants

print("number of consonants is",cons,"and number of vowels is",vow)
