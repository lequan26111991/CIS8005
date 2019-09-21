''' Chapter 12 Excercise 2 '''

class Location:
    def __init__(self): #Constructor for class 
        self.maxvalue = 0
        self.row = 0
        self.column = 0
    def locateLargest(self,a):
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] > self.maxvalue: #if class variable is smaller than current value return value and indexes
                    self.maxvalue = a[i][j] 
                    self.row = i
                    self.column = j
        print("The location of the largest element is "+str(self.maxvalue)+" at ("+str(self.row)+"," + str(self.column)+")")

#Create list and inputs
list1 =[]
r,c = eval(input("Enter the number of rows and columns in the list:"))

# Add input to list member
for i in range(r):
    list1.append(input("Enter row " +str(i)+": "))
    list1[i] = list1[i].split()
    list1[i] = [eval(x) for x in list1[i]] #Split each string to row
        
c1 = Location()
c1.locateLargest(list1)

