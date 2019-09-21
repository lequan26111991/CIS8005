''' Chapter 7 Excercise 3 '''

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
        
#Create an account        
account1 = Account(1122,20000,4.5)

#Withdraw 2500
account1.withdraw(2500)
#Deposit 3000
account1.deposit(3000) 

#print values
print("ID of account1 is",account1.getId()) 
print("Balance of account1 is",account1.getBalance()) 
print("Monthly Interest Rate of account1 is",account1.getMonthlyInterestRate()) 
print("Monthly Interest of account1 is",account1.getMonthlyInterest()) 
   
    