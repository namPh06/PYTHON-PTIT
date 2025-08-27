from math import*
def check(s):
    tmp = s[::-1]
    for i in range (len(s)):
        if abs (ord (s[i]) - ord(s[i-1])) != abs (ord (tmp[i]) - ord (tmp[i-1])) :
            return False
    return True
t  = int (input())
for _ in range (t):
    s = input()
    if check (s) :
        print ("YES")
    else :
        print ("NO")