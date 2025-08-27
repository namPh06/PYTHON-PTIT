from math import*
t = int (input())
for _ in range (t):
    n = input()
    fac = 0 
    for x in n :
        fac += factorial(int (x))
    if n == str (fac):
        print ("Yes")
    else :
        print ("No")