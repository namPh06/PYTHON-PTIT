from math import*
def check (s):
    tong  = 0
    for x in s :
        tong += int (x)
    if tong % 10 != 0 :
        return False
    for i in range (len(s) -  1):
        if abs (int (s[i]) - int (s[i + 1])) != 2:
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check (s):
        print ("YES")
    else:
        print("NO")