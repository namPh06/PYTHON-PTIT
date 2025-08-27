from math import*
l , r = map (int , input().split())
a = []
for i in range (l , r + 1):
    a.append(i)
n = len (a)
b = []
for i in range (n):
    for j in range (i+1, n):
        for k in range ( j+ 1, n):
            if gcd(a[i],a[j]) == 1 and gcd (a[j] , a[k]) == 1 and gcd (a[i], a[k]) == 1:
                b.append(f"({a[i]}, {a[j]}, {a[k]})")
for x in b :
    print (x)