from math import*
def nt (n):
    if n < 2:
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0 :
            return False
    return True
def check (n):
    tong = 0
    for x in n :
        tong += int (x)
    if nt (tong):
        return True
    return False
def check2 (n):
    for x in n :
        if (not nt (int (x))):
            return False
    return True
t = int (input())
for _ in range (t):
    n = input()
    if nt (int (n)) and check (n) and check2 (n):
        print ("Yes")
    else :
        print ("No")
