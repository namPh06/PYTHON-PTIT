from math import*
max_n = 10**5 + 1
prime = [True]* (max_n )
def sang():
    prime[0] = prime[1] = False
    for i in range (2, isqrt(max_n) + 1):
        if prime[i]:
            for j in range ( i* i , max_n , i):
                prime[j] = False
sang()
nt = []
for i in range(max_n):
    if prime[i] == True :
       nt.append(i)
n = int (input())
a = list (map (int, input().split()))
res = 0
for x1 in a :
    tmp = a[-1]
    for x2 in nt :
        tmp = min (tmp , abs (x2 - x1))
    res = max (res, tmp)
print (res) 