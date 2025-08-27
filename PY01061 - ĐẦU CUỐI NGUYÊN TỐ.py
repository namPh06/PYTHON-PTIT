from math import*
def nt (n):
    if n < 2 :
        return False
    for i in range (2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    tmp = s[0:3]
    res = s[-3:]
    if nt(int (tmp)) and nt (int (res)):
        print ("YES")
    else :
        print ("NO")
