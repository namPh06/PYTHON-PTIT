from math import*
def nt (n):
    if n < 2:
        return False
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
a = []
def seive():
    cnt = 0
    i = 2
    while True:
        if nt (i):
            a.append(i)
            cnt += 1
        i += 1
        if cnt == 1000:
            break
seive()
n , x  = map (int , input().split())
print (x, end = ' ')
tmp = x
for i in range (n):
    tmp += a[i]
    print ( tmp , end = ' ')