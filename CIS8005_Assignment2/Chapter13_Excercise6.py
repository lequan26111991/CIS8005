''' Chapter 13 Excercise 6 '''
import urllib.request

filename = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt") 
string1 = filename.read().decode()
string1 = string1.split()
print("There are",len(string1),"of words")
