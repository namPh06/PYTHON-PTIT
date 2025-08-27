def check (s):
    if len(s) % 2 == 0:
        return False
    if s[0] == s[1]:
        return False
    for i in range (len(s) - 2):
        if s[i] != s[i+2]:
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    check1 = False
    check2 = False
    check3 = True
    if len(s) % 2 != 0:
        check1 = True
    if s[0] != s[1]:
        check2 = True
    for i in range (0 , len(s) - 2 , 2):
        if s[i] != s[i+2]:
            check3 = False
            break
    if check1  == True and check2 == True and check3 == True: 
        print ("YES")
    else :
        print ("NO") 