''' Chapter 12 Excercise 16 '''

class Stack(list):
    def __init__(self):
        super().__init__()
        self.__list1 = [] 

    def push(self,string1):
        self.__list1.append(string1)

    def pull(self):
        number = self.__list1.pop()
        return number


stack1 = Stack()
for i in range(5):
    stack1.push((input("Please enter your string "+str(i)+": ")))

for i in range(5):
    print(stack1.pull(), end = " ")

