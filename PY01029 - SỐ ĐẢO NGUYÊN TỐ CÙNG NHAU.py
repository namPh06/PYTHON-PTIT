from math import*
def check (s):
    tmp = s[::-1]
    if (gcd(int(s) , int (tmp)) != 1):
        return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check (s) :
        print("YES")
    else:
        print ("NO")