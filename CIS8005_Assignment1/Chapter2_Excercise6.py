''' Chapter 2 Excercise 6 '''
#input
number = eval(input("Enter a number between 0 and 1000: "))
#get thousand digit
thousand = number//1000
#get hundred digit
hundred = (number-(thousand*1000))//100
#get tenth digit
tenth = (number-(thousand*1000)-(hundred*100))//10
#get last digit
lastdigit = (number-(thousand*1000)-(hundred*100))%10
print("Sum of the digits is: ",thousand+hundred+tenth+lastdigit)
