from math import*
def tn (n):
    return n == n[::-1]
def latnguoc (n):
    n = str (n)
    return int (n[::-1])
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
    n  = int (input())
    used = [True]* 1000001
    for i in range (n):
        if prime[i] == True and not tn (str(i)) and prime[latnguoc(i)]:
            if ( i < n and latnguoc(i) < n):
                if used[i] == True and used[latnguoc(i)] == True:
                    print (i , latnguoc(i) , end = ' ')
                    used[i] = False
                    used[latnguoc(i)] = False
    print ()