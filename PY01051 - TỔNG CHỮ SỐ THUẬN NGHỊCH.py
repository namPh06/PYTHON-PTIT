def tn (s):
    return s == s[::-1]
def check (s):
    tong = 0
    for x in s:
        tong += int (x)
    if not tn (str(tong)):
        return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    tong = 0 
    for x in s :
        tong += int (x)
    if check (s) and len(str(tong)) > 1 :
        print ("YES")
    else :  
        print ("NO")
