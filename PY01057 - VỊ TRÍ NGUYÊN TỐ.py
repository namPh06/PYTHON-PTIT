from math import*
def nt (n):
    if n < 2:
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def check (n):
    for i in range (len(s)):
        if nt (i):
            if not nt (int (s[i])):
                return False
        else :
            if nt (int (s[i])):
                return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check(s):
        print ("YES")
    else :
        print("NO")