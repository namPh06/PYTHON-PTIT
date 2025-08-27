t = int (input())
for _ in range (t):
    s = input()
    res = ""
    for i in range (0, len(s) , 2):
        ch = s[i]
        cnt = int (s[i+1])
        res += ch*cnt
    print (res)

        