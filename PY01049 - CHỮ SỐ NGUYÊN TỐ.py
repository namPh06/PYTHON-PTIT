from math import*
def nt (n):
    if n < 2 :
        return False
    for i in range (2, isqrt(n) + 1 ):
        if n % i == 0 :
            return False
    return True
def solve (n):
    if not nt (len (n)):
        return False
    cnt1 , cnt2 = 0, 0
    for x in s :
        if nt(int (x)):
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 < cnt2:
        return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if solve (s):
        print ("YES")
    else :
        print ("NO")