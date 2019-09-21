''' Chapter 1 Excercise 11 '''
pop = 312032486
yeartosecond = 365 * 24 * 60 * 60
oneyearpop = (yeartosecond // 7 + yeartosecond // 45 - yeartosecond // 13)
#first year population
print("First year Population is", pop + oneyearpop)
#second year population
print("Second year Population is", pop + 2 * oneyearpop)
#third year population
print("Third year Population is", pop + 3 * oneyearpop)
#forth year population
print("Forth year Population is", pop + 4 * oneyearpop)
#fifth year population
print("Fifth year Population is", pop + 5 * oneyearpop)
