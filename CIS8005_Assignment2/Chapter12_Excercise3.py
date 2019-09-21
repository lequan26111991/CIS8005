''' Chapter 12 Excercise 3 '''

class Account:
    
    def __init__(self,iden = 0, balance = 100.00, rate = 0.00):
        self.__id = iden
        self.__balance = balance
        self.__rate = rate
        
    #Accessor for ID    
    def getId(self):
        return self.__id
    
    #Accessor for Balance
    def getBalance(self):
        return self.__balance
    
    #Accessor for rate
    def getRate(self):
        return self.__rate
    
    #Mutator for ID
    def setID(self, rate):
        self.__rate = rate
    
    #Mutator for Balance
    def setBalance(self, balance):
        self.__balance = balance
    
    #Mutator for Rate
    def setrate(self, rate):
        self.__rate = rate
    
    #Monthly Interest Rate
    def getMonthlyInterestRate(self):
        return self.__rate / 12
    
    #Monthly Interest
    def getMonthlyInterest(self):
        return self.__balance * ((self.__rate / 100) / 12) 
    
    #Withdraw the amount
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
    
    #Withdraw the amount
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        

class ATM(Account): #Create atm account associate with Account parent type
    def __init__(self, id ,balance):
        super().__init__(iden = id, balance = balance)
    def mainMenu(self): # Main Menu for only child account
        return "Main menu\n 1: Check balance\n 2: Withdraw\n 3: Deposit\n 4: Exit"

    

def main():
    list1 =[]
    for i in range(10):
        list1.append(ATM(i,100))
    choice = 4
    while choice == 4: # Keep program in loop with choice = 4
        id = eval(input("Input your ID: "))
        for j in range(len(list1)):
            if list1[j].getId() == id:
               print(list1[j].mainMenu())
               choice = eval(input("Enter a choice:" ))
            if choice == 1:
               print(list1[j].getBalance())
               choice = 4
            elif choice == 2:
               value = eval(input("Enter amount to withdraw: "))
               list1[j].withdraw(value)
               choice = 4
            elif choice == 3:
               value = eval(input("Enter amount to Deposit: "))
               list1[j].deposit(value)
               choice = 4
            else:
               choice = 4

main()

             



