def fibo (n):
    f = [0]*93
    f[1] = 1
    f[2] = 1
    for i in range (2, 93):
        f[i] = f[i-1] + f[i-2]
    return f[n]
t  = int (input())
for _ in range (t):
    a , b = map (int, input().split())
    for i in range (a , b + 1):
        print (fibo(i) , end = ' ')
    print ()