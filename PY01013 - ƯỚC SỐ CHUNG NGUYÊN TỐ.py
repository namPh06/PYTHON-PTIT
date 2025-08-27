from math import*
def nt (n ):
    if n < 2:
        return False
    for i in range (2 , isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
t = int (input())
for _ in range (t):
    a , b = map (int , input().split())
    res = gcd (a,b)
    tong = 0
    for x in str(res):
        tong += int (x)
    if nt (tong):
        print ("YES")
    else :
        print ("NO")