t  = int (input())
for _ in range (t):
    n = int (input())
    a = list (map(int , input().split()))
    cnt = [0]*1000001
    for x in  a:
        cnt[x] += 1
    res = 0
    for x in  a:
        if cnt[x] > n / 2:
            res = max (res, cnt[x])
    if res ==  0:
        print ("NO")
    else :
        ans = 10**6 + 2
        for x in a :
            if cnt[x] == res:
                ans = min (ans , x)
        print (ans)     