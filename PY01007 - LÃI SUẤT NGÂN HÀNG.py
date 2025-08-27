from math import*
t = int (input())
for _ in range (t):
    n , x , m = map (float , input().split())
    base = 1 + x/100
    # print (base)
    res = m / n
    # print (res)
    ans = int (log(res,base))
    print (ans + 1)
