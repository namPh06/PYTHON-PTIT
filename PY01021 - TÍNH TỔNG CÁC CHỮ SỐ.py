t = int (input())
for _ in range (t):
    s = input().strip()
    tmp = []
    tong = 0
    for x in s :
        if x.isdigit():
            tong += int (x)
        else :
            tmp.append(x)
    tmp.sort()
    a = ""
    for x in tmp:
        a += x
    print (a + str(tong))