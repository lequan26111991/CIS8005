''' Chapter 15 Excercise 23 '''

def permutation(s):
   if len(s) == 1:
     return s

   list1 = [] # resulting list
   for firstchar in s:
        remainmel = displayPermuationHelper(firstchar, s)
        rlist = permutation(remainmel) # permutations of sublist
        for leftchars in rlist:
            list1.append(firstchar + leftchars)
   return list1

def displayPermuationHelper(s1, s2):
    s2 = [x for x in s2 if x != s1] # List of left over char
    return s2

def main():
    print(permutation("abc"))

main()
