t = int (input())
for _ in range (t):
    n = int (input())
    a = []
    cnt = [0]*1001
    for _ in range (n):
        x = int (input())
        a.append(x)
    for x in a:
        cnt[x] += 1
    res = 0
    for x in a:
        res = max (res , cnt[x])
    ans = 10001
    for x in a :
        if cnt[x] == res:
            ans = min (ans, x)
    print (ans)