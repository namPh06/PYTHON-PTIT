def check (s):
    se = set()
    for x in s :
        se.add(x)
    if len(se) != 2 :
        return False
    for i in range (len(s) - 2):
        if s[i] != s[i+2]:                                              
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check (s):
        print ("YES")
    else :
        print ("NO")