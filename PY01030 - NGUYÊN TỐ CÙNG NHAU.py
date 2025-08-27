from math import*
n , k = map (int ,input().split())
l , r = 10**(k-1) , 10**k - 1
cnt  = 0 
for i in range ( l, r):
    if gcd(n ,i) == 1:
        cnt += 1
        print (i , end =' ')
        if cnt % 10 == 0:
            print ()