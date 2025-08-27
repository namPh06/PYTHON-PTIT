t = int (input())
for _ in range (t):
    N , M , K = map (int , input().split())
    a = list (map (int , input().split()))
    b = list (map (int , input().split()))
    c = list (map (int , input().split()))
    i , j , k = 0 , 0 , 0
    ans = []
    while i < N and j < M and k < K:
        if a[i] == b[j] and b[j] == c[k]:
            ans.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else :
            k += 1
    if len(ans) == 0:
        print ("NO")
    else :
        for x in  ans :
            print (x, end = ' ')
    print ()