''' Chapter 5 Excercise 11 '''

#Prompt number of students
number = eval(input("Please enter number of student: "))
highest = 0 # highest
shighest = 0 #second highest
i=0
while i < number:
    score = eval(input("Please enter score of student "+str(i)+" ")) # prompt score
    if score > highest:
        shighest = highest #second highest become highest
        highest = score # new score become highest
    if score < highest and score > shighest:
        shighest = score
    i+=1
print("Highest score is:",highest," and second highest score is:",shighest)
