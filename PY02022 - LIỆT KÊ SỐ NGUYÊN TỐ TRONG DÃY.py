from math import*
def nt (n):
    if n < 2 :
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
n = int (input())
a = list (map (int , input().split()))
cnt = [0]*1000001
for x in a :
    if nt (x):
        cnt [x] += 1
for x in a :
    if cnt[x] > 0:
        print (x , cnt[x])
        cnt[x] = 0