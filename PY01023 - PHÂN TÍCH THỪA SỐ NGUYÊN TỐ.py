from math import*
def phantich (n):
    a = []
    for i in range (2, isqrt (n) + 1):
        if n % i == 0 :
            cnt = 0
            while (n % i == 0):
                cnt += 1
                n //=  i
            a.append (f"{i}^{cnt}")
    if n > 1 :  
        a.append (f"{n}^1")
    return "1 * " + " * ".join(a)
t = int(input())
for _ in range(t):
    n = int (input())
    print (phantich(n))