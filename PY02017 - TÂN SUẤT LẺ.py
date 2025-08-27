t  = int (input())
for _ in range (t):
    n = int (input())
    a = list (map (int , input().split()))
    cnt = {}
    for x in a :
        if x not in cnt:
            cnt[x] = 1
        else :
            cnt[x] += 1
    for x in a :
        if cnt[x] % 2 != 0:
            print (x)
            break
