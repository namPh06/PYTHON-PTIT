t = int (input())
for _ in range (t):
    s = input().strip()
    tmp = ""
    a = [] 
    for x in s :
        if x.isdigit():
            tmp += x
        else :
            if tmp != "":
                a.append(int (tmp))
                tmp = ""
    if tmp != "":
        a.append(int (tmp))
    print (min (a))