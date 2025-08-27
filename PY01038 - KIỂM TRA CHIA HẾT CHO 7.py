def tn (n):
    n = str(n)
    return int (n[::-1])
def solve (n):
    if n % 7 == 0:
        return n
    for _ in range (1000):
        n = int (n)
        n += tn (n)
        if n % 7 == 0:
            return n
    return -1
t = int (input())
for _ in range (t):
    n = int (input())
    print (solve(n))

