from math import*
def nt (n):
    if n < 2:
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def check (s):
    for i in range (len(s)):
        if i % 2 == 0 :
            if int  (s[i]) % 2 != 0:
                return False
        else :
            if int (s[i]) % 2 == 0:
                return False
    tong = 0
    for x in s :
        tong += int (x)
    if not nt (tong):
        return False
    return True
t = int (input())
for _ in range (t):
    s  = input()
    if check(s):
        print ("YES")
    else :
        print ("NO")