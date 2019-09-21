''' Chapter 11 Excercise 25 '''

def isMarkovMatrix(m):

    Marko = True #default is True
    isMarkov = [False] * 3 # default is False for all columns
    for column in range(len(m)):
        total = 0
        for row in range(len(m[column])):
            total += m[row][column] #Add element by column
        if total == 1:
            isMarkov[column] = True

    for x in isMarkov: #if one of the column is not added to 1
        if x == False:
            Marko = False
    return Marko


def main():
    print("Enter a 3-by-3 matrix row")
    list = []
    for i in range(0,3): #split list into 3 smaller lists
        list.append([])
        list[i] = input("Enter input: ")
        list[i] = list[i].split()
        list[i] = [eval(x) for x in list[i]]

    if isMarkovMatrix(list) == True:
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")


main()
