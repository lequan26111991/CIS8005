''' Chapter10 Excercise 26 '''

def merge(list1, list2):
    
    #Extract list1 and list 2 to individual member of list
    list1 = list1.split()
    list2 = list2.split()
    list1 = [int(x) for x in list1]
    list2 = [int(y) for y in list2]
    
    #Create list 3 and add list 1 and list 2 to it
    list3 =[]
    for member in (list1):
        list3.append(member)
    for member in (list2):
        list3.append(member)
    
    #Resort the list
    for i in range(len(list3) - 1):
        currentmin = list3[i]
        currentminindex = i
        for k in range(i + 1, len(list3)):
            if currentmin > list3[k]:
               currentmin = list3[k]
               currentminindex = k 
        if currentminindex != i:
           list3[currentminindex] = list3[i]
           list3[i] = currentmin
            
    return list3
            
def main():
    l1 = input("Please enter list 1")
    l2 = input("Please enter list 2")
    print("The merge list is:",merge(l1,l2))
    
main()
    