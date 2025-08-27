def check (s):
    for i in range (len (s) - 1):
        if s[i] > s[i+1]:
            return False
    return True
t= int (input())
for _ in range (t):
    s = input()
    if check (s):
        print ("YES")
    else: 
        print ("NO")
