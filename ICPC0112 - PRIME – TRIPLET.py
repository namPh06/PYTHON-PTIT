from math import isqrt
max_n = 10**6 + 6
prime = [True] * (max_n)
prime[0] = prime[1] = False
def sang():
    for i in range(2, isqrt(max_n) + 1):
        if prime[i]:
            for j in range(i*i, max_n, i):
                prime[j] = False

sang()
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n-6):
        if (prime[i] and prime[i+2] and prime[i+6]) or (prime[i] and prime[i+4] and prime[i+6]):
            cnt += 1
    print(cnt)
