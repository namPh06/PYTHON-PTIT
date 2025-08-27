def check (s):
    a = ['0', '1' ,'2']
    for x in s :
        if x not in a:
            return False
    return True
t = int (input())
for _ in range (t):
    s = input()
    if check (s):
        print ("YES")
    else :
        print ("NO")