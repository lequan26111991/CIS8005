''' Chapter 15 Excercise 3 '''

def gcd(m,n):
    gc = 0
    if m % n == 0:
       gc = n
       return gc
    else:
       return gcd(n, m % n)

def main():
    print(gcd(20,50))

main()
