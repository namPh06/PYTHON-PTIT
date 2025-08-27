def check (n):
    for x in n :
        if x != '4' and  x != '7' :
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check (s) == True:
        print ("YES")
    else :
        print ("NO")