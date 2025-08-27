def check (s):
    res = 0
    for x in s :
        if x != '6' and x != '8':
            return False
        elif x == '8':
            res += 1
        else :
            res = 0
        if res == 3:
            return False
    return True
s = input()
if (check(s)):
    print("YES")
else :
    print ("NO")