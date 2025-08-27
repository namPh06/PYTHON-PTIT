from math import*
max_n = 10**6 + 1
prime = [True]* (max_n )
def sang():
    prime[0] = prime[1] = False, False
    for i in range (2, isqrt(max_n) + 1):
        if prime[i]:
            for j in range ( i* i , max_n , i):
                prime[j] = False
sang()
t = int (input())
for _ in range (t):
    n = int (input())
    k = 0
    for i in range (n):
        if gcd(i, n) == 1:
            k += 1
    if prime[k] == True:
        print ("YES")
    else :
        print ("NO")