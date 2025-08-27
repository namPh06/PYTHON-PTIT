from math import*
def nt (n):
    if n < 2:
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
t  = int (input())
for _ in range (t):
    s = input()
    res = s[-4:]
    if nt(int (res)):
        print ("YES")
    else :
        print ("NO")